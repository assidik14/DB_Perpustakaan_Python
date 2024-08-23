import os
from . import Operasi

def clear_console ():
    '''Fungsi untuk clear console'''
    sistem_operasi = os.name
    match sistem_operasi :
        case "posix" : os.system("clear")
        case "nt" : os.system("cls")

def header ():
    '''Fungsi menampilkan header aplikasi'''
    welcome_message = "=== SELAMAT DATANG ==="
    title_app = "Database Perpustakaan CRUD Menggunakan Python"
    print(f"{welcome_message:^45}")
    print(title_app)
    print(45*"=")

def divider():
    '''Fungsi garis pembatas'''
    print(45*"-")

def divider2():
    '''Fungsi garis pembatas'''
    print(45*"=")

def menu():
    '''Fungsi menampilkan menu'''
    opsi_menu = 0
    for opsi_menu in range(0,4):
        opsi_menu += 1
        match opsi_menu :
            case 1 : print(f"{opsi_menu}. CREATE DATA")
            case 2 : print(f"{opsi_menu}. READ DATA")
            case 3 : print(f"{opsi_menu}. UPDATE DATA")
            case 4 : print(f"{opsi_menu}. DELETE DATA")

def read_console():
    '''Fungsi read data di console'''
    data_file = Operasi.read()
    
    index = "NO"
    judul = "JUDUL"
    penulis = "PENULIS"
    tahun = "TAHUN"

    # Header
    print("\n"+100*"=")
    print(f"{index:^4} | {judul:^40} | {penulis:^40} | {tahun:^5}")
    print(100*"-")

    # Data
    for index, data in enumerate(data_file):
        data_break = data.split(',')
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}",end="")

    # Footer
    print(100*"="+"\n")

def create_console():
    '''Fungsi create data di console'''
    print(f"\n{'-----====== Silakan Masukan Data ======-----':^45}\n")
    while (True):
        penulis = input("Masukan Nama Penulis : ")
        if penulis == "":
            print("Nama penulis tidak boleh kosong")
        else:
            break

    while (True):
        judul = input("Masukan Judul : ")
        if judul == "":
            print("Judul buku harus di isi")
        else:
            break
    
    while (True):
        tahun = input("Masukan Tahun : ")
        if tahun == "":
            print("Tahun tidak boleh kosong!!!")
        elif tahun.isdigit() == False:
            print("Tahun harus angka!!")
        elif len(tahun) > 4 or len(tahun) < 4:
            print("Format tahun harus 'YYYY'")
        else:
            break
    try:
        Operasi.create(penulis, judul, tahun)
        print(f"\n{'-----===== Data Berhasil Ditambah =====-----':^45}")
        read_console()
    except Exception:
        print(f"\n{'##### Data tidak berhasil di tambahkan #####':^45}")

def update_console():
    '''Fungsi update data di console'''
    read_console()
    while (True):
        while(True):
            try :
                nomor = int(input("Pilih Nomor Buku : "))
                break
            except ValueError:
                print("Nomor harus diisi dan berupa angka!!")
        data_buku = Operasi.read(index=nomor)

        if data_buku:
            break
        else:
            print("Nomor Buku tidak valid!!")
    
    data_break = data_buku.split(',')
    pk = data_break[0]
    date_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]
    
    while (True):
        print("\nSilakan pilih data yang ingin diubah")
        divider()
        print(f"1. Penulis \t: {penulis:.40}")
        print(f"2. Buku \t: {judul:.40}")
        print(f"3. Tahun \t: {tahun:4}")
        divider()
        
        user_option = input("Pilih Data \t: ")
        
        match user_option :
            case "1" : penulis = input("Penulis \t: ")
            case "2" : judul = input("Judul \t: ")
            case "3" :
                while (True):
                    tahun = input("Tahun \t: ")
                    if tahun == "":
                        print("Tahun tidak boleh kosong!!!")
                    elif tahun.isdigit() == False:
                        print("Tahun harus angka!!")
                    elif len(tahun) > 4 or len(tahun) < 4:
                        print("Format tahun harus 'YYYY'")
                    else:
                        break
            case _: print("Data tidak valid!!")

        print("\nData baru")
        divider()
        print(f"1. Penulis \t: {penulis:.40}")
        print(f"2. Buku \t: {judul:.40}")
        print(f"3. Tahun \t: {tahun:4}")
        divider()

        is_done = input("Tekan sembarang untuk pilih data lagi atau Tekan 'y' untuk update data : ")
        if is_done == 'y' or is_done == "Y":
            break
    
    try :
        Operasi.update(nomor, pk, date_add, penulis, judul, tahun)
        print(f"\n{'-----===== Data disimpan =====-----':^45}")
    except Exception:
        print(f"\n{'##### Data tidak berhasil disimpan #####':^45}")