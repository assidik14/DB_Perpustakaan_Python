from . import CRUD

DB_NAME = "data.txt"
TEMPLATE = {
    "pk":"XXXXXX",
    "date_add":"yyyy-mm-dd",
    "judul":255*" ",
    "penulis":255*" ",
    "tahun":"yyyy"
}

def init_console():
    '''Check database'''
    try:
        with open(DB_NAME, mode="r", encoding="utf-8") as file:
            print("Database tersedia, init done!!")

    except Exception as ErrorMessage :
        print(ErrorMessage)
        print("Database tidak ditemukan, silakan membuat database baru")
        CRUD.first_data()