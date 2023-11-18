from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
from imutils.video import VideoStream
import argparse
import facenet
import imutils
import os
import sys
import math
import pickle
import align.detect_face
import numpy as np
import cv2
import collections
from sklearn.svm import SVC
import csv
import time
import requests
import streamlit as st
import tempfile

output_folder = 'FCRN'

def main(probability_threshold, camera, stframe,phong):
    #ip_camera_url = 'http://192.168.1.90:4747/video'

    with open("key_telegram.txt", "r") as file:
        data = file.read()
    lst_data = data.split(",")
    url = lst_data[0]
    chatID = lst_data[1]

    baseUrl = f'https://api.telegram.org/{url}/sendPhoto'
    MINSIZE = 20
    THRESHOLD = [0.6, 0.7, 0.7]
    FACTOR = 0.709
    IMAGE_SIZE = 200
    INPUT_IMAGE_SIZE = 160

    import streamlit as st

    pkl_file = st.sidebar.file_uploader("Tải lên mô hình nhận diện khuôn mặt", type=["pkl"])
    temp_file2 = tempfile.NamedTemporaryFile(suffix=".pkl", delete=False)
    if pkl_file is not None:
        temp_file2.write(pkl_file.read())

    #CLASSIFIER_PATH = 'Models/model_saved.pkl'
    CLASSIFIER_PATH = temp_file2.name
    print(temp_file2.name)
    FACENET_MODEL_PATH = 'Models/20180402-114759.pb'
    ALIGNMENT_MODEL_PATH ="src/align"

    # Load The Custom Classifier
    with open(CLASSIFIER_PATH, 'rb') as file:
        model, class_names = pickle.load(file)
    print("Custom Classifier, Successfully loaded")

    with tf.Graph().as_default():

        # Cai dat GPU neu co
        gpu_options = tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction=0.6)
        sess = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(gpu_options=gpu_options, log_device_placement=False))

        with sess.as_default():

            # Load the model
            print('Loading feature extraction model')
            facenet.load_model(FACENET_MODEL_PATH)

            # Get input and output tensors
            images_placeholder = tf.compat.v1.get_default_graph().get_tensor_by_name("input:0")
            embeddings = tf.compat.v1.get_default_graph().get_tensor_by_name("embeddings:0")
            phase_train_placeholder = tf.compat.v1.get_default_graph().get_tensor_by_name("phase_train:0")
            embedding_size = embeddings.get_shape()[1]

            pnet, rnet, onet = align.detect_face.create_mtcnn(sess, ALIGNMENT_MODEL_PATH)

            people_detected = set()
            person_detected = collections.Counter()

            cap = cv2.VideoCapture(camera)
            start_time_names = time.time()
            start_time_count = time.time()

            def write_names_to_csv(names):
                with open('detected_names.csv', 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([time.strftime('%Y-%m-%d %H:%M:%S')] + names)

            def write_detection_count_to_csv(count):
                with open('detection_count.csv', 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([time.strftime('%Y-%m-%d %H:%M:%S'), count])

            last_csv_update_time_names = time.time()
            last_csv_update_time_count = time.time()
            current_names = []
            current_count = 0

            while (True):
                _, frame = cap.read()  # Modify this line to unpack the frame data from the tuple
                #frame = imutils.resize(frame, width=800)
                frame = cv2.resize(frame, (800, 600))
                frame = cv2.flip(frame, 1)

                bounding_boxes, _ = align.detect_face.detect_face(frame, MINSIZE, pnet, rnet, onet, THRESHOLD, FACTOR)

                faces_found = bounding_boxes.shape[0]
                try:
                    det = bounding_boxes[:, 0:4]
                    bb = np.zeros((faces_found, 4), dtype=np.int32)
                    for i in range(faces_found):
                        bb[i][0] = det[i][0]
                        bb[i][1] = det[i][1]
                        bb[i][2] = det[i][2]
                        bb[i][3] = det[i][3]
                        print(bb[i][3]-bb[i][1])
                        print(frame.shape[0])
                        print((bb[i][3]-bb[i][1])/frame.shape[0])
                        if (bb[i][3]-bb[i][1])/frame.shape[0]>0.25:
                            cropped = frame[bb[i][1]:bb[i][3], bb[i][0]:bb[i][2], :]
                            scaled = cv2.resize(cropped, (INPUT_IMAGE_SIZE, INPUT_IMAGE_SIZE),
                                                interpolation=cv2.INTER_CUBIC)
                            scaled = facenet.prewhiten(scaled)
                            scaled_reshape = scaled.reshape(-1, INPUT_IMAGE_SIZE, INPUT_IMAGE_SIZE, 3)
                            feed_dict = {images_placeholder: scaled_reshape, phase_train_placeholder: False}
                            emb_array = sess.run(embeddings, feed_dict=feed_dict)

                            predictions = model.predict_proba(emb_array)
                            best_class_indices = np.argmax(predictions, axis=1)
                            best_class_probabilities = predictions[
                                np.arange(len(best_class_indices)), best_class_indices]
                            best_name = class_names[best_class_indices[0]]
                            print("Name: {}, Probability: {}".format(best_name, best_class_probabilities))



                            if best_class_probabilities > probability_threshold:
                                cv2.rectangle(frame, (bb[i][0], bb[i][1]), (bb[i][2], bb[i][3]), (0, 255, 0), 2)
                                text_x = bb[i][0]
                                text_y = bb[i][3] + 20

                                name = class_names[best_class_indices[0]]
                                cv2.putText(frame, name, (text_x, text_y), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                            1, (255, 255, 255), thickness=1, lineType=2)
                                cv2.putText(frame, str(round(best_class_probabilities[0], 3)), (text_x, text_y + 17),
                                            cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                            1, (255, 255, 255), thickness=1, lineType=2)

                                if time.time() - last_csv_update_time_names >= 10:
                                    current_names.insert(0, best_name)
                                    write_names_to_csv(current_names)
                                    last_csv_update_time_names = time.time()
                                    current_names.clear()

                                person_detected[best_name] += 1



                            else:
                                name="Unknown"

                                cv2.putText(frame, name, (text_x, text_y), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                            1, (255, 255, 255), thickness=1, lineType=2)

                                frame_count2=0
                                if time.time() - last_csv_update_time_count >= 30:
                                    write_detection_count_to_csv(faces_found)
                                    last_csv_update_time_count = time.time()
                                    faces_found = 0

                                    frame_filename = os.path.join(output_folder, f"{frame_count2}.png")
                                    cv2.imwrite(frame_filename, frame)
                                    frame_count2 += 1

                                    try:
                                        my_file = open(frame_filename, "rb")

                                        caption_time = time.strftime("%Y-%m-%d %H:%M:%S",
                                                                     time.localtime())  # Lấy thời gian hiện tại
                                        parameters = {
                                            "chat_id": f"{chatID}",
                                            "caption": f"Nhận diện thí sinh_ Thời gian: {caption_time}" + "," + f"Phòng: {phong}"
                                        }

                                        files = {
                                            "photo": my_file
                                        }

                                        resp = requests.get(baseUrl, data=parameters, files=files)
                                        print(resp)
                                    except:
                                        pass


                except:
                    pass
                stframe.image(frame, channels='BGR', use_column_width=True)

                # cv2.imshow('Face Recognition', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()

if __name__=='__main__':
    main()
