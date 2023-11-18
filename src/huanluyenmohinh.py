import streamlit as st
import align_dataset_mtcnn2
import tempfile
import pickle
import classifier2
import time

def huanluyenmohinh():
    list_2 = ["", "Tiền xử lí dữ liệu", "Huấn luyện mô hình"]
    # st.header("Chọn cách huấn luyện")
    selected_l2 = st.selectbox("Chọn cách huấn luyện", list_2)

    if selected_l2 == "":
        st.info("Bạn phải chọn cách huấn luyện")

    if selected_l2 == "Tiền xử lí dữ liệu":
        st.subheader("Chọn thư mục ảnh")

        # text_input_2 = st.empty()
        input_path = st.text_input("Nhập đường dẫn tới folder chứa ảnh", key="text_input")

        if input_path != "":
            # text_input_2.empty()
            # st.info(input_path)
            # dataset_processed = st.empty()
            processed_path = st.text_input(
                "Nhập đường dẫn tới folder chứa ảnh sau khi xử lí xong", key="text_input2")

            if processed_path != "":
                # dataset_processed.empty()
                # st.info(processed_path)

                select_box_imgsz = [182, 190, 200, 210]
                rs = st.selectbox("Chọn kích thước ảnh sau trước cắt khuôn mặt", select_box_imgsz, key="imgsz")

                select_box_margin = [44, 45, 50, 55]
                slbmrg = st.selectbox("Chọn kích thước ảnh sau khi cắt khuôn mặt", select_box_margin,
                                      key="margin")

                select_box_order = ["True", "False"]
                rdorder = st.selectbox("Chọn số lượng ảnh xáo trộn", select_box_order, key="order")

                detect_mlpfaces = ["False", "True"]

                mlp_faces = st.selectbox("Phát hiện nhiều khuôn mặt trong một ảnh", detect_mlpfaces, key="mlpf")

                try:
                    button_pressed = st.button(label="Bắt đầu")
                    if button_pressed:
                        bar = st.progress(0)
                        abc = True
                        while abc:
                            success_count, total_img = align_dataset_mtcnn2.main(input_path, processed_path,
                                                                                 int(rs), int(slbmrg),
                                                                                 bool(rdorder), bool(mlp_faces))
                            a = round((success_count) / (total_img) * 100)
                            bar.progress(a)
                            time.sleep(0.1)
                            if (total_img - success_count == 0):
                                abc = False
                        st.success("Tiền xử lí dữ liệu thành công")


                except ZeroDivisionError:
                    st.error("Trong folder phải có ít nhất một ảnh")
                # except Exception as e:
                #     st.error("Đã xảy ra lỗi",e)
                #     st.info("Hãy khởi động lại")
                finally:
                    st.info("Phải đảm bảo trong folder có ít nhất một ảnh trước khi xử lí")

    if selected_l2 == "Huấn luyện mô hình":
        st.header("Huấn luyện mô hình")
        mode = "TRAIN"
        data_dir = st.text_input("Hãy nhập đường dẫn tới folder ảnh đã tiền xử lí")
        if data_dir != "":
            pb_file = st.file_uploader("Tải lên mô hình", type=["pb"])
            temp_file = tempfile.NamedTemporaryFile(suffix=".pb", delete=False)
            if pb_file is not None:
                temp_file.write(pb_file.read())
                pkl_file = st.file_uploader("Tải lên mô hình phân lớp", type=["pkl"])
                temp_file2 = tempfile.NamedTemporaryFile(suffix=".pkl", delete=False)
                if pkl_file is not None:
                    temp_file2.write(pkl_file.read())
                    batchsize_lst = [90, 100, 110, 200, 300]
                    btch = st.selectbox("Chọn số lượng ảnh huấn luyện trong 1 lần", batchsize_lst, key="bacth2")

                    imgSize_lst = [160, 170, 180, 300]
                    imgst = st.selectbox("Chọn kích cỡ ảnh đầu vào", imgSize_lst, key="imgst")

                    seed_lst = [666, 700, 1000, 1500]
                    seed_2 = st.selectbox("Random seed", imgSize_lst, key="radnseed")

                    min_nrof = 20
                    nrof_train_img = 10

                    print("a", data_dir)

                    try:
                        button2 = st.button("Xử lí", key="btn2")
                        if button2:
                            model2, class_names2, classifier_filename_exp = classifier2.main(mode, str(data_dir),
                                                                                             temp_file.name,
                                                                                             temp_file2.name, int(btch),
                                                                                             int(imgst), int(seed_2),
                                                                                             min_nrof, nrof_train_img)
                            st.success("Tiền xử lí dữ liệu thành công")
                            with open(classifier_filename_exp, 'wb') as outfile:
                                pickle.dump((model2, class_names2), outfile)

                            with open(classifier_filename_exp, "rb") as file:
                                st.download_button(label="Download Model File", data=file, file_name="model_saved.pkl")

                    except ZeroDivisionError:
                        st.error("Trong folder phải có ít nhất một ảnh")
                    except Exception as e2:
                        st.error("Lỗi", e2)