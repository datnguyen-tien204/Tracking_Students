import streamlit as st
import tempfile
import time
import requests
def load_image(url,chatID,temp_file2):


    try:
        my_file = open(temp_file2.name, "rb")

        caption_time = time.strftime("%Y-%m-%d %H:%M:%S",
                                     time.localtime())  # Lấy thời gian hiện tại
        parameters = {
            "chat_id": f"{chatID}",
            "caption": f"Test -  Thời gian: {caption_time}"
        }

        files = {
            "photo": my_file
        }

        resp = requests.get(url, data=parameters, files=files)


        return resp.status_code
    except:
        pass


