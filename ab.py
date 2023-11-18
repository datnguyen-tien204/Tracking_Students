import requests

# Gửi yêu cầu GET đến một URL nào đó
response = requests.get('https://api.telegram.org/bot6374709841:AAEFa1PDP9q6Vo52C8WvXvRiZ66Xou7rqec/')

# Lấy mã trạng thái HTTP từ Response
status_code = response.status_code

# In mã trạng thái HTTP
print(status_code)
