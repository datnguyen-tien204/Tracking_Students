import streamlit as st
from PIL import Image

def introduction_admin2():
    PROJECTS = {
        "►Download hướng dẫn sử dụng tại đây": "https://drive.usercontent.google.com/download?id=1LiUsIAs9XLPlv4groAZZ1_v4D5LzkUuB&export=download&authuser=0&confirm=t&uuid=5c09b9c2-fc9b-4aba-a095-4ba65a934191&at=APZUnTVe1COtt804oEsTLDrassMA:1695769418691",
        "►Xem video hướng dẫn sử dụng tại đây": "https://www.youtube.com/watch?v=C86ZXvgpejM&list=PLkDaE6sCZn6Gl29AoE31iwdVwSG-KnDzF"
    }
    PROJECTS2 = {
        "►Download hướng dẫn sử dụng tại đây": "https://drive.usercontent.google.com/download?id=1LiUsIAs9XLPlv4groAZZ1_v4D5LzkUuB&export=download&authuser=0&confirm=t&uuid=5c09b9c2-fc9b-4aba-a095-4ba65a934191&at=APZUnTVe1COtt804oEsTLDrassMA:1695769418691",
        "►Xem video hướng dẫn sử dụng tại đây": "https://www.youtube.com/watch?v=C86ZXvgpejM&list=PLkDaE6sCZn6Gl29AoE31iwdVwSG-KnDzF"
    }
    PROJECTS3={
        "►Download hướng dẫn sử dụng tại đây": "https://drive.usercontent.google.com/download?id=1LiUsIAs9XLPlv4groAZZ1_v4D5LzkUuB&export=download&authuser=0&confirm=t&uuid=5c09b9c2-fc9b-4aba-a095-4ba65a934191&at=APZUnTVe1COtt804oEsTLDrassMA:1695769418691",
        "►Xem video hướng dẫn sử dụng tại đây": "https://www.youtube.com/watch?v=C86ZXvgpejM&list=PLkDaE6sCZn6Gl29AoE31iwdVwSG-KnDzF"
    }
    PROJECTS4 = {
        "►Download hướng dẫn sử dụng tại đây": "https://drive.usercontent.google.com/download?id=15BXaEeZsDxzySEwCnsbFcSsBmO4qEzZL&export=download&authuser=0&confirm=t&uuid=42ed8b45-646b-4a64-91e4-136065f3e25c&at=APZUnTWQ0JpTE5N6zy0qbX6e8zha:1695789336900",
        "►Xem video hướng dẫn sử dụng tại đây": "https://www.youtube.com/watch?v=C86ZXvgpejM&list=PLkDaE6sCZn6Gl29AoE31iwdVwSG-KnDzF"
    }
    PROJECTS5 = {
        "►Download hướng dẫn sử dụng tại đây": "https://drive.usercontent.google.com/download?id=1LiUsIAs9XLPlv4groAZZ1_v4D5LzkUuB&export=download&authuser=0&confirm=t&uuid=5c09b9c2-fc9b-4aba-a095-4ba65a934191&at=APZUnTVe1COtt804oEsTLDrassMA:1695769418691",
        "►Xem video hướng dẫn sử dụng tại đây": "https://www.youtube.com/watch?v=C86ZXvgpejM&list=PLkDaE6sCZn6Gl29AoE31iwdVwSG-KnDzF"
    }
    # st.markdown(
    #                 "<h1 style='font-weight: bold; text-align: center; position: relative; top: -70px;'>Hướng dẫn sử dụng</h1>",
    #                 unsafe_allow_html=True)
    st.info("I. Face-Recognition( Nhận diện khuôn mặt )")
    st.write("""
    Nhận diện khuôn mặt là một công nghệ phát triển nhanh chóng và thu hút nhiều sự chú ý trong những năm gần đây. Công nghệ này liên quan đến việc xác định và xác minh tự động các cá nhân dựa trên đặc điểm khuôn mặt của họ. Công nghệ này dựa vào việc thu thập, phân tích và so sánh các đặc điểm khuôn mặt duy nhất, như khoảng cách giữa đôi mắt, hình dáng mũi. 
    Với sử dụng các thuật toán học sâu, hệ thống nhận diện khuôn mặt đã trở nên rất chính xác và được áp dụng trong nhiều lĩnh vực, bao gồm an ninh, kiểm soát truy cập và thậm chí trên các nền tảng mạng xã hội. Việc áp dụng hệ thống này vào trong thi cử, học tập là một điều tất yếu cần thiết. Hệ thống này giúp kiểm soát và nhận dạng được thí sinh trong phòng thi. Trích xuất ra các thông tin khuôn mặt và khi kết thúc thì sẽ xuất ra Excel để đối chiếu lại khi cần.""")
    for project, link in PROJECTS.items():
        st.write(f"[{project}]({link})")

    st.image('FaceRecognition.jpg')

    st.info("II. Tracking People ( Kiểm soát học sinh)")
    st.write("""Cùng với công nghệ nhận dạng khuôn mặt thì công nghệ kiểm soát học sinh trong các kì thi cử cũng rất phát triển. Công nghệ này sử dụng một trong những mô hình AI hiện đại nhất hiện nay. Hệ thống này sau mỗi 5 phút sẽ tự động chụp ảnh và gửi về Telegram 1 lần để các thầy cô có thể kiểm soát được sinh viên ra vào đồng thời cũng ghi lại thời điểm ra vào với kết quả thời gian thực cứ 10 giây / 1 lần.
    Cùng với việc sử dụng kết hợp cả thuật toán học máy và thuật toán học sâu thì hệ thông theo dõi thí sinh cũng ngày càng trở nên chính xác. Ứng dụng của nó ngày càng được con người tin tưởng và phát triển trở nên rộng rãi trong đời sống và cả làm việc.""")
    for project, link in PROJECTS2.items():
        st.write(f"[{project}]({link})")
    st.image("tracking_people.jpg")

    st.info("III. Cheating Recognition ( Phát hiện gian lận)")
    st.write("""Một lĩnh vực khác cũng đang phát triển rất mạnh và có xu hướng lớn hơn trong tương lai chính là phát hiện gian lận ở thi sinh sử dụng AI. Hệ thống này khi chạy nếu phát hiện bất thương hay vi phạm sẽ đánh dấu đó và chụp ảnh gửi về Telegram để xác định vi phạm. Độ chính xác của hệ thống này ở mức tin cậy và đang trong quá trình
      phát hiển và thử nghiệm thêm. Hệ thống ứng dụng học sâu này ở các nước phát triển trên thế giới như Anh,Pháp, Mỹ và các nước châu Á khác như Nhật Bản, Hàn Quốc,... cũng đã đưa vào sử dùng kết hợp với giáo viên coi thi nhằm đạt hiệu quả cao nhất và đảm bảo được tính công bằng nhất cho kì thi.""")
    for project, link in PROJECTS3.items():
        st.write(f"[{project}]({link})")
    st.image("cheating.jpg")
    st.image("cheat_2.png")

    st.info("IV. Hướng dẫn huấn luyện mô hình")
    st.write(""" Việc huấn luyện mô hình yêu cầu tương thích với các khuôn mặt không có sẵn trong hệ thống. Khi mà hệ thống chưa có khuôn mặt để nhận dạng hoặc khi bạn có thí sinh mới cần thêm vào thì cần phải huấn luyện để 
    mô hình nhận diện được khuôn mặt đó. Nếu bạn đã có tệp huấn luyện ở camera 1 thì có thể xuất file huấn luyện đó vào mô hình này và sử dụng (file .pkl). Để biết thêm về cách huấn luyện hãy xem video hoặc tài liệu PDF của chúng tôi.""")
    for project, link in PROJECTS4.items():
        st.write(f"[{project}]({link})")
    st.image("train_model.png")

    st.info("V. Hướng dẫn quản trị hệ thống")
    st.write("""Phần mềm cũng cung cấp việc quản lí tài khoản cho giáo viên. Việc quản lí này nằm trong mục quản trị hệ thống của tổng quan""")
    for project, link in PROJECTS5.items():
        st.write(f"[{project}]({link})")
    st.image("manage_sys.jpg")

if __name__ == '__main__':
     introduction_admin2()