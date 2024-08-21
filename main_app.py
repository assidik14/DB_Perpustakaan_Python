from CRUD import Operasi, View
from CRUD import Database

if __name__ == "__main__":

    View.clear_console()
    View.header()

    # Check database
    Database.init_console()
    
    while (True):

        View.clear_console()
        View.header()
        View.menu()
        View.divider()
        
        # User input menu
        while (True):
            pilih_Menu = int(input("Pilih Menu : "))
            if pilih_Menu != 1 and pilih_Menu != 2 and pilih_Menu != 3 and pilih_Menu != 4:
                print("Menu yang kamu pilih salah, silakan pilih lagi !!")
            else:
                break

        match pilih_Menu :
            case 1 : Operasi.create()
            case 2 : View.read_console()
            case 3 : Operasi.update()
            case 4 : Operasi.delete()

        is_done = input("\nApakah lanjut (y/n) : ")
        if is_done == "n" or is_done == "N":
            break
    
    View.divider()
    print(f"{'===== Program Selesai =====':^45}")
    View.divider()