from . import Operasi

DB_NAME = "data.txt"
TEMPLATE = {
    "pk":"XXXXXX",
    "date_add":"dd-mm-yyyy",
    "penulis":255*" ",
    "judul":255*" ",
    "tahun":"yyyy"
}

def init_console():
    '''Check database'''
    try:
        with open(DB_NAME, mode="r", encoding="utf-8") as file:
            print("Database tersedia, init done!!")

    except FileNotFoundError :
        print("Database tidak ditemukan!!\nSilakan membuat database baru")
        Operasi.first_data()