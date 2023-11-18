# -*- coding: UTF-8 -*-
import cv2 as cv
import time
from utils import choose_run_mode, load_pretrain_model#, set_video_writer
from Pose.pose_visualizer import TfPoseVisualizer
from Action.recognizer import load_action_premodel, framewise_recognize
from warnings import filterwarnings
filterwarnings(action='ignore', category=DeprecationWarning, message='`np.bool` is a deprecated alias')
import os
import requests
current_struct_time = time.localtime()
formatted_time = time.strftime("%d/%m/%Y %H:%M:%S", current_struct_time)

with open("key_telegram.txt", "r") as file:
    data = file.read()
lst_data = data.split(",")
url = lst_data[0]
chatID = lst_data[1]

baseUrl=f'https://api.telegram.org/{url}/sendPhoto'

def AnTiCheating(model,vid,stframe,phong):

# Load models
    try:
        estimator = load_pretrain_model(model)
        action_classifier = load_action_premodel('Action/framewise_recognition3.h5')


        # phg=phong
        # Initialize parameters
        fps_interval = 1
        start_time = time.time()
        fps_count = 0
        frame_count = 0
        frame_count2=0
        capture_images = False
        output_folder = 'ViPham'


        # Choose video source
        cap = choose_run_mode(vid)


        while cv.waitKey(1) < 0:
            has_frame, show = cap.read()
            if has_frame:
                fps_count += 1
                frame_count += 1

                humans = estimator.inference(show)
                pose = TfPoseVisualizer.draw_pose_rgb(show, humans)
                show,init_label = framewise_recognize(pose, action_classifier)

                height, width = show.shape[:2]
                # Calculate and show FPS
                if (time.time() - start_time) > fps_interval:
                    realtime_fps = fps_count / (time.time() - start_time)
                    fps_count = 0
                    start_time = time.time()
                fps_label = 'FPS:{0:.2f}'.format(realtime_fps)
                cv.putText(show, fps_label, (width-160, 25), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)

                # Show number of detected humans
                num_label = "Human: {0}".format(len(humans))
                cv.putText(show, num_label, (5, height-45), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)

                # Show running time and frame count
                if frame_count == 1:
                    run_timer = time.time()
                run_time = time.time() - run_timer
                time_frame_label = '[Time:{0:.2f} | Frame:{1}]'.format(run_time, frame_count)
                cv.putText(show, time_frame_label, (5, height-15), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)

                #Show Frame
                # cv.imshow('Phat hien gian lan', show)
                stframe.image(show, channels='BGR', use_column_width=True)

                # if init_label == "NemPhao":
                #     if not capture_images:  # Nếu đang không trong trạng thái chụp ảnh
                #         capture_images = True  # Bắt đầu chế độ chụp ảnh
                #         frame_count2 = 0  # Đặt lại đếm số lượng ảnh chụp được
                #
                #     if capture_images:
                #         frame_filename = os.path.join(output_folder, f"{init_label}_{frame_count2}.png")
                #         cv.imwrite(frame_filename, show)
                #         frame_count2 += 1
                #
                #         try:
                #             my_file = open(frame_filename, "rb")
                #             # phong = '413'
                #             parameters = {
                #                 "chat_id": "-984762057",
                #                 "caption": f"Thoi gian: {formatted_time}" + "," + f"Noi dung vi pham: {init_label}','Phong:{phong}"
                #             }
                #
                #             files = {
                #                 "photo": my_file
                #             }
                #             resp = requests.get(baseUrl, data=parameters, files=files)
                #         except:
                #             pass
                #
                # else:
                #     capture_images = False

        # video_writer.release()
        cap.release()
        cv.destroyAllWindows()
    except:
        pass
