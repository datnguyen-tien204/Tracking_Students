import  streamlit_authenticator as stauth

from src.Auth import database as db

usernames=["abc"]
names=["abc"]
passwords=["abc"]
hashed_passwords=stauth.Hasher(passwords).generate()

for(username,name,hashed_password) in zip(usernames,names,hashed_passwords):
    db.insert_user(username,name,hashed_password)