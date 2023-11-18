# importing libraries
import cv2
from ultralytics import YOLO
import numpy as np
import csv
import time
import requests
import time
import os
current_struct_time = time.localtime()
import streamlit as st
from streamlit_server_state import server_state, server_state_lock
formatted_time = time.strftime("%d/%m/%Y %H:%M:%S", current_struct_time)

# global variable stores the people count
count_var = 0
output_folder = 'SoNguoi'
capture_images=False
frame_count2 = 0
with open("key_telegram.txt", "r") as file:
    data = file.read()
lst_data = data.split(",")
url = lst_data[0]
chatID = lst_data[1]

baseUrl = f'https://api.telegram.org/{url}/sendPhoto'


t=0
def main2(stframe,camera,models,phong):

    # access the global variable
    global count_var,t
    model = YOLO(models)
    cap = cv2.VideoCapture(camera)

    def write_detection_count_to_csv(count):
        with open('detection_count.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([time.strftime('%Y-%m-%d %H:%M:%S'), count])

    last_csv_update_time_count = time.time()
    current_names = []
    current_count = 0


    while True:

        # ---------- capturing frames-----------#
        ret, frame = cap.read()
        if not ret:
            break

        # ---------- resizing the frames---------#
        frame = cv2.resize(frame, (800, 600))

        # --------- list that stores the centroids of the current frame---------#
        centr_pt_cur_fr = []

        results = model(frame)
        result = results[0]

        classes = np.array(result.boxes.cls.cpu(), dtype="int")
        confidence = np.array(result.boxes.conf.cpu())

        bboxes = np.array(result.boxes.xyxy.cpu(), dtype="int")
        idx = []
        for i in range(0, len(classes)):
            if classes[i] == 0:
                idx.append(i)

        # print("these are indexes:",idx)

        # ----------- bounding boxes for person detections---------------#
        bbox = []
        for i in idx:
            temp = bboxes[i]
            bbox.append(temp)

        box_multi_list = [arr.tolist() for arr in bbox]
        for box in box_multi_list:
            (x, y, x2, y2) = box

            cv2.rectangle(frame, (x, y), (x2, y2), (0, 0, 255), 2)
            cx = int((x + x2) / 2)
            cy = int((y + y2) / 2)
            centr_pt_cur_fr.append((cx, cy))
            cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

        # counting of total people in the footage
        head_count = len(centr_pt_cur_fr)

        # counting the number of faces with count_var variable
        count_var = head_count
        print(head_count)

        # displaying the face count on the screen for experiment purpose
        cv2.putText(frame, f'{head_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

        # cv2.imshow("frame", frame)
        stframe.image(frame, channels='BGR', use_column_width=True)




        #Telegram
        # baseUrl = 'https://api.telegram.org/bot6217962481:AAElrXjC0iR3wg1csX7ex-jaURJk1EbNOdk/sendPhoto'

        frame_count2 = 0
        if time.time() - last_csv_update_time_count >= 10:
            write_detection_count_to_csv(head_count)
            last_csv_update_time_count = time.time()

            frame_filename = os.path.join(output_folder, f"{frame_count2}.png")
            cv2.imwrite(frame_filename, frame)
            frame_count2 += 1

            try:
                my_file = open(frame_filename, "rb")

                caption_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # Lấy thời gian hiện tại
                parameters = {
                    "chat_id": f"{chatID}",
                    "caption": f"Đếm số người _ Thời gian: {caption_time}" + "," + f"Số người: {head_count},'Phòng:{phong}"
                }

                files = {
                    "photo": my_file
                }

                resp = requests.get(baseUrl, data=parameters, files=files)
                print(resp)
            except:
                pass

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main2()

