def main():
    import streamlit as st
    from streamlit_option_menu import option_menu
    import streamlit_authenticator as stauth

    from huanluyenmohinh import huanluyenmohinh
    from thongkesudung import thongkesudung
    from demsonguoi import demsonguoi
    from nhandienthisinh import nhandienthisinh
    from quansatphong import quansatphong
    from phathiengianlan import phathiengianlan
    from Auth import database as db
    from Auth.authenticate import authentication
    from streamlit_extras.app_logo import add_logo
    from introduction import introduction
    from introduction_admin import introduction_admin2

# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
    st.set_page_config(page_title="Home",page_icon="house",layout="centered")
    EXAMPLE_NO = 1

    hide_login = False
    def Authentication_Admin(names, usernames, hashed_passwords):
        authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "Home", "abcdef", cookie_expiry_days=0)

        name, authentication_status, username = authenticator.login("Login", "main")
        if authentication_status == False:
            st.error("Username/password is incorrect")

        if authentication_status == None:
            st.warning("Hãy nhập mật khẩu và tài khoản")

        if authentication_status:
            hide_login = True
            authenticator.logout("Logout", "sidebar")

            def streamlit_menu(example=1):
                if example == 1:
                    # 1. as sidebar menu
                    with st.sidebar:
                        selected = option_menu(
                            menu_title="Main Menu",  # required
                            options=["Tổng quan", "Đếm số người", "Nhận diện thí sinh trong phòng", "Quan sát phòng",
                                     "Phát hiện gian lận"],  # required
                            icons=["house", "pentagon", "distribute-horizontal", "display", "camera"],  # optional
                            menu_icon="cast",  # optional
                            default_index=0,  # optional
                        )
                    return selected

            selected = streamlit_menu(example=1)

            if selected == "Tổng quan":
                # Hiển thị tiêu đề "Tổng quan" ở giữa và đầu trang
                st.markdown(
                    "<h1 style='font-weight: bold; text-align: center; position: relative; top: -90px;'>Tổng quan</h1>",
                    unsafe_allow_html=True)

                selected = option_menu(
                    menu_title=None,  # required
                    options=["Huấn luyện mô hình", "Thống kê sử dụng", "Quản trị hệ thống", "Hướng dẫn sử dụng"],
                    # required
                    icons=["gear-fill", "graph-up", "gear-fill", "book-half"],  # optional
                    menu_icon="cast",  # optional
                    default_index=0,  # optional
                    orientation="horizontal"
                )
                if selected == "Huấn luyện mô hình":
                    huanluyenmohinh()

                if selected == "Thống kê sử dụng":
                    thongkesudung()
                if selected=="Hướng dẫn sử dụng":
                    introduction_admin2()

                if selected == "Quản trị hệ thống":
                    sl2 = ["", "Thêm tài khoản", "Xoá tài khoản", "Cập nhật thông tin tài khoản"]
                    sltbt = st.selectbox("Hãy chọn mục cần quản lý", sl2)

                    if sltbt == "Thêm tài khoản":
                        authentication()
                    if sltbt == "Xoá tài khoản":
                        data = db.fetch_all_users("Teacher")
                        keys = []
                        keys.append("")
                        for d in data:
                            keys.append(d['key'])

                        # In danh sách các key
                        print(keys)
                        sldtk = st.selectbox("Chọn tài khoản cần xoá", keys)
                        button_pressed3 = st.button("Xác nhận")
                        if button_pressed3:
                            try:
                                db.delete_user(sldtk, "Teacher")
                                st.success(f"Xoá thành công tài khoản {sldtk}")
                            except:
                                st.error(f"Có lỗi khi xoá tài khoản {sldtk}")
                                pass
                    if sltbt=="Cập nhật thông tin tài khoản":
                        try:
                            l=(db.fetch_all_users("Teacher"))
                            keys_and_names = [(item['key'], item['name']) for item in l]
                            ps_input = st.text_input("Nhập mật khẩu mới: ")
                            ps_input_confirm = st.text_input("Nhập lại mật khẩu mới: ")
                            button_pressed = st.button("Xác nhận")
                            if button_pressed:
                                for key, name in keys_and_names:
                                    if(key==usernames):

                                        if ps_input==ps_input_confirm:
                                            hashed_password = stauth.Hasher(ps_input).generate()
                                            db.insert_user(username, name, hashed_password, "Teacher")
                                            st.success("Cập nhật thành công")
                                            break
                                    if(ps_input!=ps_input_confirm):
                                        st.error("Nhập lại mật khẩu không khớp")
                                        break
                                    #if(ps_input==ps_input_confirm):


                        except:
                            pass


            elif selected == "Đếm số người":
                demsonguoi()
            elif selected == "Nhận diện thí sinh trong phòng":
                nhandienthisinh()
            elif selected == "Quan sát phòng":
                quansatphong()

            elif selected == "Phát hiện gian lận":
                phathiengianlan()
    def Authentication_Teacher(names, usernames, hashed_passwords):
        authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "Home", "abcdef", cookie_expiry_days=0)

        name, authentication_status, username = authenticator.login("Login", "main")
        if authentication_status == False:
            st.error("Username/password is incorrect")

        if authentication_status == None:
            st.warning("Hãy nhập mật khẩu và tài khoản")

        if authentication_status:
            hide_login = True
            authenticator.logout("Logout", "sidebar")

            def streamlit_menu(example=1):
                if example == 1:
                    # 1. as sidebar menu
                    with st.sidebar:
                        selected = option_menu(
                            menu_title="Main Menu",  # required
                            options=["Tổng quan", "Đếm số người", "Nhận diện thí sinh trong phòng", "Quan sát phòng",
                                     "Phát hiện gian lận"],  # required
                            icons=["house", "pentagon", "distribute-horizontal", "display", "camera"],  # optional
                            menu_icon="cast",  # optional
                            default_index=0,  # optional
                        )
                    return selected

            selected = streamlit_menu(example=1)

            if selected == "Tổng quan":
                # Hiển thị tiêu đề "Tổng quan" ở giữa và đầu trang
                st.markdown(
                    "<h1 style='font-weight: bold; text-align: center; position: relative; top: -90px;'>Tổng quan</h1>",
                    unsafe_allow_html=True)

                selected = option_menu(
                    menu_title=None,  # required
                    options=["Thống kê sử dụng", "Hướng dẫn sử dụng","Đổi mật khẩu"],
                    # required
                    icons=["graph-up", "gear-fill", "book-half"],  # optional
                    menu_icon="cast",  # optional
                    default_index=0,  # optional
                    orientation="horizontal"
                )

                if selected == "Thống kê sử dụng":
                    thongkesudung()
                if selected=="Hướng dẫn sử dụng":
                    introduction()

                if selected=="Đổi mật khẩu":

                    passwords = st.text_input("Hãy nhập mật khẩu")
                    passwords_2 = st.text_input("Xác nhận mật khẩu")

                    button_pressed = st.button("Xác nhận")
                    if button_pressed:
                        if passwords == passwords_2:
                            try:
                                usernames = [f"{username}"]
                                names = [f"{name}"]
                                passwords = [f"{passwords}"]
                                roles = ["Teacher"]
                                hashed_passwords = stauth.Hasher(passwords).generate()

                                for (username, name, hashed_password, role) in zip(usernames, names, hashed_passwords,
                                                                                   roles):
                                    db.insert_user(username, name, hashed_password, role)
                                    st.success("Đăng kí thành công")
                            except:
                                pass
                        else:
                            st.error("Mật khẩu không khớp")

            elif selected == "Đếm số người":
                demsonguoi()
            elif selected == "Nhận diện thí sinh trong phòng":
                nhandienthisinh()
            elif selected == "Quan sát phòng":
                quansatphong()

            elif selected == "Phát hiện gian lận":
                phathiengianlan()

    ds_role = ['', 'Quản trị viên', 'Giáo viên']
    t = st.sidebar.selectbox("Đăng nhập với tư cách", ds_role)
    if t == "Giáo viên":
        try:
            role = "Teacher"
            users = db.fetch_all_users(role)
            usernames = [user["key"] for user in users]
            names = [user["name"] for user in users]
            hashed_passwords = [user["password"] for user in users]
            Authentication_Teacher(names, usernames, hashed_passwords)
        except:
            pass
    elif t == "Quản trị viên":
        try:
            role = "Admin"
            users = db.fetch_all_users(role)
            usernames = [user["key"] for user in users]
            names = [user["name"] for user in users]
            hashed_passwords = [user["password"] for user in users]
            Authentication_Admin(names, usernames, hashed_passwords)
        except:
            pass
    elif t == '':
        st.warning("Bạn phải chọn vai trò trước khi đăng nhập")

if '__name__'=='__main__':
    main()



