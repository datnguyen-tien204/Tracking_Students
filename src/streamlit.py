# import streamlit as st
# import tensorflow as tf
# import numpy as np
# import cv2
# import imutils
# import facenet
# import align.detect_face
# import pickle
# import collections
# from sklearn.svm import SVC
# from imutils.video import VideoStream
# import tempfile
# from face_rec_cam2 import detect
# from yolov8 import main2
# # from st2 import streamlit1
# import threading
# from zoom import Camera
#
# import sys
# def main():
#     st.sidebar.markdown("<h1 style='font-weight: bold; text-align: center; position: relative; top: -90px;'>Setting</h1>", unsafe_allow_html=True)
#     st.sidebar.markdown('---')
#     list_of_options = ["",'Đếm số người', 'Nhận diện thí sinh trong phòng','Quan sát phòng']
#
#     # Sử dụng CSS để thiết lập kích thước của phần option tự động điều chỉnh theo kích thước của sidebar
#     option_style = """
#     <style>
#     .sidebar .widget-content {
#         width: 100%;
#     }
#     .sidebar .title-container {
#         top: 0;
#     }
#     .st-title {
#         font-weight: bold;
#         text-align: center;
#         position: absolute;
#         top: 50%;
#         left: 50%;
#         transform: translate(-70%, -90%);
#     }
#     </style>
#     """
#     st.markdown(option_style, unsafe_allow_html=True)
#
#     selected_option = st.sidebar.selectbox("Chọn chế độ", list_of_options)
#     st.sidebar.markdown('---')
#     list_of_options2 = ['Camera 1', 'Camera 2', 'Tuỳ chỉnh']
#     selected_cam = st.sidebar.selectbox("Chọn camera", list_of_options2)
#     st.sidebar.markdown('---')
#     video_file_buffer = st.sidebar.file_uploader("Upload a video", type=["mp4", "mov", 'avi', 'asf', 'm4v'])
#     DEMO_VIDEO = 'test.mp4'
#     tfflie = tempfile.NamedTemporaryFile(suffix='.mp4', delete=False)
#
#     ##We get our input video here
#     vid = None
#     if not video_file_buffer:
#         if selected_cam == 'Camera 1':
#             vid = 0
#             tfflie.name = 0
#
#         elif selected_cam == 'Camera 2':
#             vid = 1
#             tfflie.name = 0
#
#         elif selected_cam == 'Tuỳ chỉnh':
#             with st.sidebar:
#                 show_input = st.empty()  # Tạo một phần tử rỗng để hiển thị / ẩn phần nhập liệu
#                 ip = st.text_input("Nhập địa chỉ IP của camera", key="ip_input")
#                 port = st.text_input("Nhập cổng của IP Camera:", key="port_input")
#                 button_pressed = st.button("Kết nối")
#
#             if button_pressed:
#                 if ip and port:
#                     vid = (f'rtsp://{ip}/{port}')
#                     tfflie.name = 0
#                     # Hiển thị thông báo "Đã kết nối thành công!"
#                     st.success("Đã thực hiện thành công!")
#                     # Ẩn phần nhập IP và port sau khi nút "Kết nối" được nhấn
#                     show_input.empty()
#
#
#         else:
#             vid = cv2.VideoCapture(DEMO_VIDEO)
#             tfflie.name = DEMO_VIDEO
#             dem_vid = open(tfflie.name, 'rb')
#             demo_bytes = dem_vid.read()
#
#             st.sidebar.text('Input Video')
#             st.sidebar.video(demo_bytes)
#
#     else:
#         tfflie.write(video_file_buffer.read())
#         # print("No Buffer")
#         dem_vid = open(tfflie.name, 'rb')
#         demo_bytes = dem_vid.read()
#
#         st.sidebar.text('Input Video')
#         st.sidebar.video(demo_bytes)
#
#     print(tfflie.name)
#     stframe = st.empty()
#
#     if selected_option == 'Nhận diện thí sinh trong phòng':
#         st.title('Student Face-Recognition')
#
#
#         st.markdown("<hr/>", unsafe_allow_html=True)
#         kpi1, kpi2, kpi3 = st.columns(3)
#
#         # stframe.image(im0,channels = 'BGR',use_column_width=True)
#
#         with kpi2:
#             st.markdown("Người phát hiện")
#             kpi2_text = st.markdown("0")
#
#         with kpi3:
#             st.markdown("**Độ chính xác**")
#             kpi3_text = st.markdown("0")
#
#         st.markdown("<hr/>", unsafe_allow_html=True)
#         confidence = 0.8
#         detect(confidence, vid, kpi2_text, kpi3_text, stframe)
#
#     elif selected_option=='Đếm số người':
#         # Thực hiện hành động tương ứng khi chọn "Nhận diện thí sinh trong phòng"
#
#         # Tạo một đoạn mã HTML/CSS để định dạng tiêu đề "Student Counting"
#         st.markdown(
#             """
#             <div style="text-align: center;">
#                 <h1 style="font-size: 36px; font-weight: bold; margin-bottom: -90px;">Student Counting</h1>
#                 <hr style="border: 2px solid black; width: 80%; margin: auto;">
#             </div>
#             """,
#             unsafe_allow_html=True
#         )
#
#         main2(stframe,vid)
#
#     elif selected_option=="Quan sát phòng" :
#         stframe = st.empty()
#         cam = Camera(mirror=True)  # Create a Camera instance
#         cam.stream()  # Start streaming from the camera
#         cam.show(stframe)# Pass the stframe to the show() method
#
#
#
#
#
#
#
# if __name__ == '__main__':
#     main()
#
