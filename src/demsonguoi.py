import streamlit as st
import tempfile
from yolov8 import main2
from getRoom import getRoom

def demsonguoi():
    with open("database_choose.txt", "r") as file:
        data = file.read()
    lst_data = data.split(",")
    server = lst_data[0]
    database = lst_data[1]
    table = lst_data[2]
    
    list_of_options2 = ["", 'Camera 1', 'Camera 2', 'Tuỳ chỉnh']
    selected_cam = st.sidebar.selectbox("Chọn camera", list_of_options2)
    st.sidebar.markdown('---')
    tfflie = tempfile.NamedTemporaryFile(suffix='.mp4', delete=False)

    list_opt_3 = []
    room = getRoom(server, database, table)
    list_opt_3.append("")
    for item in room:
        list_opt_3.append(f"{item[0]}<{item[1]}>")
        print(list_opt_3[0])
    list_opt_3.append("Tuỳ chỉnh")

    ##We get our input video here
    vid = None
    if selected_cam == "":
        st.warning("Hãy chọn camera trước khi sử dụng")


    else:
        if selected_cam == 'Camera 1':
            vid = 0
            tfflie.name = 0
            stframe = st.empty()
            selected_opt3 = st.sidebar.selectbox("Chọn phòng", list_opt_3, key="slt3")
            if selected_opt3 == "":
                st.warning("Hãy chọn phòng trước khi sử dụng")
            elif (selected_opt3 != "Tuỳ chỉnh" and selected_opt3!=""):
                with st.sidebar:
                    feedback = st.text_input("Gửi phản hồi")
                    send_feedback = st.button("Gửi")
                if send_feedback:
                    print(feedback)
                main2(stframe, vid, "yolov8s.pt", selected_opt3)
            elif selected_opt3 == "Tuỳ chỉnh":
                with st.sidebar:
                    show_input = st.empty()  # Tạo một phần tử rỗng để hiển thị / ẩn phần nhập liệu
                    phg2 = st.text_input("Nhập tên phòng", key="phg5")
                    button_pressed = st.button("Chọn")
                if button_pressed:
                    if phg2:
                        with st.sidebar:
                            feedback = st.text_input("Gửi phản hồi")
                            send_feedback = st.button("Gửi")

                        # if the button is clicked, send the feedback and restore the video state
                        if send_feedback:
                            # save the video state
                            print(feedback)
                        main2(stframe, vid, "yolov8s.pt", phg2)

        elif selected_cam == 'Camera 2':
            stframe = st.empty()

            vid = 1
            tfflie.name = 0
            # print(tfflie.name)

            selected_opt3 = st.sidebar.selectbox("Chọn phòng", list_opt_3, key="slt3")
            if selected_opt3 == "":
                st.warning("Hãy chọn phòng trước khi sử dụng")

            elif selected_opt3 != "Tuỳ chỉnh" and selected_opt3!="":
                with st.sidebar:
                    feedback = st.text_input("Gửi phản hồi")
                    send_feedback = st.button("Gửi")

                # if the button is clicked, send the feedback and restore the video state
                if send_feedback:
                    # save the video state
                    print(feedback)
                main2(stframe, vid, "yolov8s.pt", selected_opt3)

            elif selected_opt3 == "Tuỳ chỉnh":
                with st.sidebar:
                    show_input = st.empty()  # Tạo một phần tử rỗng để hiển thị / ẩn phần nhập liệu
                    phg2 = st.text_input("Nhập tên phòng", key="phg5")
                    button_pressed = st.button("Chọn")
                if button_pressed:
                    if phg2:
                        main2(stframe, vid, "yolov8s.pt", phg2)

        elif selected_cam == 'Tuỳ chỉnh':

            with st.sidebar:
                show_input = st.empty()  # Tạo một phần tử rỗng để hiển thị / ẩn phần nhập liệu
                ip = st.text_input("Nhập địa chỉ IP của camera", key="ip_input")
                port = st.text_input("Nhập cổng của IP Camera:", key="port_input")
                button_pressed = st.button("Kết nối")

            if button_pressed:
                if ip and port:
                    vid = (f'rtsp://{ip}/{port}')
                    tfflie.name = 0
                    # Hiển thị thông báo "Đã kết nối thành công!"
                    st.success("Đã thực hiện thành công!")
                    # Ẩn phần nhập IP và port sau khi nút "Kết nối" được nhấn
                    show_input.empty()
                    # print(tfflie.name)
                    stframe = st.empty()

                    selected_opt3 = st.sidebar.selectbox("Chọn phòng", list_opt_3, key="slt3")
                    if selected_opt3 == "":
                        st.warning("Hãy chọn phòng trước khi sử dụng")
                    elif selected_opt3 != "Tuỳ chỉnh" and selected_opt3!="":
                        with st.sidebar:
                            feedback = st.text_input("Gửi phản hồi")
                            send_feedback = st.button("Gửi")

                        # if the button is clicked, send the feedback and restore the video state
                        if send_feedback:
                            # save the video state
                            print(feedback)
                        main2(stframe, vid, "yolov8s.pt", selected_opt3)
                    elif selected_opt3 == "Tuỳ chỉnh":
                        with st.sidebar:
                            show_input = st.empty()  # Tạo một phần tử rỗng để hiển thị / ẩn phần nhập liệu
                            phg2 = st.text_input("Nhập tên phòng", key="phg5")
                            button_pressed = st.button("Chọn")
                        if button_pressed:
                            if phg2:
                                with st.sidebar:
                                    feedback = st.text_input("Gửi phản hồi")
                                    send_feedback = st.button("Gửi")

                                # if the button is clicked, send the feedback and restore the video state
                                if send_feedback:
                                    # save the video state
                                    print(feedback)
                                main2(stframe, vid, "yolov8s.pt", phg2)

