from deta import Deta
from dotenv import load_dotenv
import os


#DETA_KEY=os.getenv("DETA_KEY")
DETA_KEY="c0zs8h1xkrh_7BrDAB5AG1KTwbPn4he92NHed1UvDRLa"
deta=Deta(DETA_KEY)



def insert_user(username,name,password,role):
    if role=="Teacher":
        db = deta.Base("PWwithUsername")
        return db.put({"key":username,"name":name,"password":password,"role":role})
    if role=="Admin":
        db = deta.Base("DatabaseAdmin")
        return db.put({"key":username,"name":name,"password":password,"role":role})

def fetch_all_users(role):
    if role=="Teacher":
        db = deta.Base("PWwithUsername")
        res=db.fetch()
        return res.items
    if role=="Admin":
        db = deta.Base("DatabaseAdmin")
        res = db.fetch()
        return res.items

def get_user(username,role):
    if role=="Teacher":
        db = deta.Base("PWwithUsername")
        return db.get(username)
    if role=="Admin":
        db = deta.Base("DatabaseAdmin")
        return db.get(username)

def update_user(username,updates,role):
    if role=="Teacher":
        db = deta.Base("PWwithUsername")
        return db.update(updates,username)
    if role=="Admin":
        db = deta.Base("DatabaseAdmin")
        return db.update(updates,username)

def delete_user(username,role):
    if role=="Teacher":
        db = deta.Base("PWwithUsername")
        return db.delete(username)
    if role=="Admin":
        db = deta.Base("DatabaseAdmin")
        return db.delete(username)

#insert_user("abc","abc","abc","abc")
