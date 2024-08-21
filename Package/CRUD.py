from . import Database

def first_data():
    '''Init data pertama kali'''
    penulis = input("Penulis : ")
    judul = input("Judul : ")
    tahun = input("Tahun : ")

    data = Database.TEMPLATE.copy()
    

def create():
    '''Fungsi Create Data'''
    print("FUNGSI CREATE DATA")

def read():
    '''Fungsi Read Data'''
    print("FUNGSI READ DATA")

def update():
    '''Fungsi Update Data'''
    print("FUNGSI UPDATE DATA")

def delete():
    '''Fungsi Delete Data'''
    print("FUNGSI DELETE DATA")