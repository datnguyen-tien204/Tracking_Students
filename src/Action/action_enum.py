from enum import Enum


class Actions(Enum):
    """
    Actions enum
    """
    # framewise_recognition.h5
    # squat = 0
    # stand = 1
    # walk = 2
    # wave = 3

    # framewise_recognition_under_scene.h5
    BinhThuong = 0 #Mauxanh la cay
    DangTayTrai = 1 #Mau cam
    DangTayPhai = 2 #Mau hong dam
    DungDay = 4 #Mau xanh duong
    NemPhao = 5 #Maudo
    QuayDau=3 #Mau nau nhat
