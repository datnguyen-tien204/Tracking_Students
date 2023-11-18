import cv2
import time
last_csv_update_time_count = time.time()
import os
import requests
output_folder = 'QSTP'

with open("key_telegram.txt", "r") as file:
    data = file.read()
lst_data = data.split(",")
url = lst_data[0]
chatID = lst_data[1]

baseUrl = f'https://api.telegram.org/{url}/sendPhoto'

def QSTP(camera,stframe,phong):
    last_csv_update_time_count = time.time()
# Tạo đối tượng VideoCapture và chỉ định nguồn video
    video = cv2.VideoCapture(camera)

    # Kiểm tra xem VideoCapture có mở thành công hay không
    if not video.isOpened():
        print("Không thể mở video")
        exit()

    # Vòng lặp để đọc từng khung hình trong video
    while True:
        # Đọc khung hình tiếp theo từ video
        ret, frame = video.read()

        # Kiểm tra xem có còn khung hình để đọc hay không
        if not ret:
            break

        # Hiển thị khung hình
        stframe.image(frame, channels='BGR', use_column_width=True)

        frame_count2 = 0
        if time.time() - last_csv_update_time_count >= 30:
            last_csv_update_time_count = time.time()

            frame_filename = os.path.join(output_folder, f"{frame_count2}.png")
            cv2.imwrite(frame_filename, frame)
            frame_count2 += 1

            try:
                my_file = open(frame_filename, "rb")

                caption_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # Lấy thời gian hiện tại
                parameters = {
                    "chat_id": f"{chatID}",
                    "caption": f"Quan sát phòng _ Thời gian: {caption_time}" + "," + f"Phòng: {phong}"
                }

                files = {
                    "photo": my_file
                }

                resp = requests.get(baseUrl, data=parameters, files=files)
                print(resp)
            except:
                pass

        # Nhấn phím 'q' để dừng lại
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Giải phóng tài nguyên VideoCapture và đóng cửa sổ hiển thị video
    video.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    QSTP()