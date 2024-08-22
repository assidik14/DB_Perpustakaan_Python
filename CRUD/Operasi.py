from . import Database
from . import Util
import time

def first_data():
    '''Init data pertama kali'''
    while (True):
        penulis = input("Penulis : ")
        if penulis == "":
            print("Nama penulis tidak boleh kosong")
        else:
            break

    while (True):
        judul = input("Judul : ")
        if judul == "":
            print("Judul buku harus di isi")
        else:
            break
    
    while (True):
        tahun = input("Tahun : ")
        if tahun == "":
            print("Tahun tidak boleh kosong!!!")
        elif tahun.isdigit() == False:
            print("Tahun harus angka!!")
        else:
            break

    time_format = time.strftime("%d-%m-%Y-%H:%M:%S%z", time.localtime())

    data = Database.TEMPLATE.copy()
    data["pk"] = Util.random_string(6)
    data["date_add"] = time_format
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = tahun

    try:
        with open(Database.DB_NAME, mode="w", encoding="utf-8") as file:
            str_data = f"{data['pk']}, {data['date_add']}, {data['penulis']}, {data['judul']}, {data['tahun']}\n"
            file.write(str_data)
    except Exception:
        print("Gagal menulis data!!")

def create(penulis:str, judul:str, tahun:int):
    '''Fungsi Create Data'''

    time_format = time.strftime("%d-%m-%Y-%H:%M:%S%z", time.localtime())

    data = Database.TEMPLATE.copy()
    data["pk"] = Util.random_string(6)
    data["date_add"] = time_format
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = tahun

    try:
        with open(Database.DB_NAME, mode="a", encoding="utf-8") as file:
            str_data = f"{data['pk']}, {data['date_add']}, {data['penulis']}, {data['judul']}, {data['tahun']}\n"
            file.write(str_data)
    except Exception:
        print("Gagal menulis data!!")

def read():
    '''FUNGSI READ DATA'''
    try:
        with open(Database.DB_NAME, mode="r", encoding="UTF-8") as file:
            content = file.readlines()
            return content
    except Exception:
        print("Gagal membaca database!!")
        return False

def update():
    '''Fungsi Update Data'''
    print("FUNGSI UPDATE DATA")

def delete():
    '''Fungsi Delete Data'''
    print("FUNGSI DELETE DATA")