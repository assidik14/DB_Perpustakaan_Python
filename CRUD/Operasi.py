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
        elif len(tahun) > 4 or len(tahun) < 4:
            print("Format tahun harus 'YYYY'")
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
            str_data = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"
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
            str_data = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"
            file.write(str_data)
            print(f"\n{'-----===== Data Berhasil Ditambah =====-----':^45}")
    except Exception:
        print(f"\n{'##### Data tidak berhasil di tambahkan #####':^45}")

def read(**kwargs):
    '''FUNGSI READ DATA'''
    try:
        with open(Database.DB_NAME, mode="r", encoding="UTF-8") as file:
            content = file.readlines()
            jumlah_buku = len(content)
            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:
                    return content[index_buku]
            else:
                return content
    except Exception:
        # print("Gagal membaca database!!")
        return False

def update(nomor, pk, date_add, penulis, judul, tahun):
    '''Fungsi Update Data'''

    data = Database.TEMPLATE.copy()
    data["pk"] = pk
    data["date_add"] = date_add
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = tahun

    str_data = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"
    panjang_data = len(str_data)

    try:
        with open(Database.DB_NAME, mode="r+", encoding="utf-8") as file:
            file.seek(panjang_data*(nomor-1))
            file.write(str_data)
            print(f"\n{'-----===== Data disimpan =====-----':^45}")
    except Exception:
        print(f"\n{'##### Data tidak berhasil disimpan #####':^45}")