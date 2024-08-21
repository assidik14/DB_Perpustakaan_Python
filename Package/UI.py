import os

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
    print("\n")