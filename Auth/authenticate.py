import streamlit_authenticator as stauth
import database as db
import streamlit as st
from deta import Deta
from dotenv import load_dotenv
import os

def authentication():
    list_role=["Giáo viên","Quản trị viên"]
    select_bt=st.selectbox("Chọn vai trò cần thêm tài khoản",list_role)
    if select_bt=="Giáo viên":
        name = st.text_input("Họ và tên")
        username=st.text_input("Hãy nhập tài khoản")
        passwords=st.text_input("Hãy nhập mật khẩu")
        passwords_2=st.text_input("Xác nhận mật khẩu")

        button_pressed=st.button("Xác nhận")
        if button_pressed:
            if passwords==passwords_2:
                try:
                    usernames=[f"{username}"]
                    names=[f"{name}"]
                    passwords=[f"{passwords}"]
                    roles=["Teacher"]
                    hashed_passwords=stauth.Hasher(passwords).generate()

                    for(username,name,hashed_password,role) in zip(usernames,names,hashed_passwords,roles):
                        db.insert_user(username,name,hashed_password,role)
                        st.success("Đăng kí thành công")
                except :
                    pass
            else:
                st.error("Mật khẩu không khớp")
    if select_bt=="Quản trị viên":
        name = st.text_input("Họ và tên")
        username = st.text_input("Hãy nhập tài khoản")
        passwords = st.text_input("Hãy nhập mật khẩu")
        passwords_2 = st.text_input("Xác nhận mật khẩu")


        button_pressed = st.button("Xác nhận")
        if button_pressed:
            if passwords == passwords_2:
                try:
                    usernames = [f"{username}"]
                    names = [f"{name}"]
                    passwords = [f"{passwords}"]
                    roles = ["Admin"]
                    hashed_passwords = stauth.Hasher(passwords).generate()

                    for (username, name, hashed_password, role) in zip(usernames, names, hashed_passwords, roles):
                        db.insert_user(username, name, hashed_password, role)
                        st.success("Đăng kí thành công")
                except:
                    pass
            else:
                st.error("Mật khẩu không khớp")
#authentication()