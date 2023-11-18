import streamlit as st
import tempfile
from CheatDetection import AnTiCheating
from getRoom import getRoom

def phathiengianlan():
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

    list_op_options3 = []
    room = getRoom(server, database, table)
    list_op_options3.append("")
    for item in room:
        list_op_options3.append(f"{item[0]}<{item[1]}>")
        print(list_op_options3[0])
    list_op_options3.append("Tuỳ chỉnh")
    
    ##We get our input video here
    vid = None
    if selected_cam == "":
        st.warning("Hãy chọn camera trước khi sử dụng")
    else:
        if selected_cam == 'Camera 1':
            vid = 0
            tfflie.name = 0

            selected_options = st.sidebar.selectbox("Chọn phòng", list_op_options3, key="selected")
            if selected_options == "":
                st.warning("Hãy chọn phòng trước khi sử dụng")
            elif selected_options != "" and selected_options!="Tuỳ chỉnh":
                stframe = st.empty()
                AnTiCheating("mobilenet_thin", vid, stframe, selected_options)
            elif selected_options == "Tuỳ chỉnh":
                with st.sidebar:
                    show_input = st.empty()  # Tạo một phần tử rỗng để hiển thị / ẩn phần nhập liệu
                    phg = st.text_input("Nhập tên phòng: ", key="phg")
                    button_pressed = st.button("Chọn")

                if button_pressed:
                    if phg:
                        st.success("Đã thực hiện thành công!")
                        # Ẩn phần nhập IP và port sau khi nút "Kết nối" được nhấn
                        show_input.empty()

                    stframe = st.empty()

                    # detect(confidence, vid, kpi2_text, kpi3_text, stframe)
                    AnTiCheating("mobilenet_thin", vid, stframe, phg)



        elif selected_cam == 'Camera 2':
            vid = "video12422TN.mp4"
            tfflie.name = 0

            selected_options = st.sidebar.selectbox("Chọn phòng", list_op_options3, key="selected")

            if selected_options == "":
                st.warning("Hãy chọn phòng trước khi sử dụng")
            elif selected_options != "" and selected_options != "Tuỳ chỉnh":
                stframe = st.empty()
                AnTiCheating("mobilenet_thin", vid, stframe, selected_options)
            elif selected_options == "Tuỳ chỉnh":
                with st.sidebar:
                    show_input = st.empty()  # Tạo một phần tử rỗng để hiển thị / ẩn phần nhập liệu
                    phg = st.text_input("Nhập tên phòng: ", key="phg")
                    button_pressed = st.button("Chọn")

                if button_pressed:
                    if phg:
                        st.success("Đã thực hiện thành công!")
                        # Ẩn phần nhập IP và port sau khi nút "Kết nối" được nhấn
                        show_input.empty()

                    stframe = st.empty()

                    # detect(confidence, vid, kpi2_text, kpi3_text, stframe)
                    AnTiCheating("mobilenet_thin", vid, stframe, phg)


        elif selected_cam == 'Tuỳ chỉnh':
            with st.sidebar:
                show_input = st.empty()  # Tạo một phần tử rỗng để hiển thị / ẩn phần nhập liệu
                ip = st.text_input("Nhập địa chỉ IP của camera", key="ip_input2")
                port = st.text_input("Nhập cổng của IP Camera:", key="port_input2")
                button_pressed = st.button("Kết nối")

            if button_pressed:
                if ip and port:
                    vid = (f'http://{ip}:{port}/video')
                    tfflie.name = 0
                    # Hiển thị thông báo "Đã kết nối thành công!"
                    st.success("Đã thực hiện thành công!")
                    # Ẩn phần nhập IP và port sau khi nút "Kết nối" được nhấn
                    show_input.empty()

                selected_options = st.sidebar.selectbox("Chọn phòng", list_op_options3, key="selected")

                if selected_options == "":
                    st.warning("Hãy chọn phòng trước khi sử dụng")
                elif selected_options != "" and selected_options != "Tuỳ chỉnh":
                    stframe = st.empty()
                    AnTiCheating("mobilenet_thin", vid, stframe, selected_options)

                elif selected_options == "Tuỳ chỉnh":
                    with st.sidebar:
                        show_input = st.empty()  # Tạo một phần tử rỗng để hiển thị / ẩn phần nhập liệu
                        phg = st.text_input("Nhập tên phòng: ", key="phg")
                        button_pressed = st.button("Chọn")

                    if button_pressed:
                        if phg:
                            st.success("Đã thực hiện thành công!")
                            # Ẩn phần nhập IP và port sau khi nút "Kết nối" được nhấn
                            show_input.empty()

                        stframe = st.empty()

                        # detect(confidence, vid, kpi2_text, kpi3_text, stframe)
                        AnTiCheating("mobilenet_thin", vid, stframe, phg)