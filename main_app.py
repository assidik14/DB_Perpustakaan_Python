from Package import UI, CRUD, Database

if __name__ == "__main__":

    # Check database
    Database.init_console()
    
    while (True):

        UI.clear_console()
        UI.header()
        UI.menu()

        # User input menu
        pilih_Menu = int(input("Pilih menu : "))
        # Validasi pilih menu
        while pilih_Menu != 1 and pilih_Menu != 2 and pilih_Menu != 3 and pilih_Menu != 4:
            print("Menu yang kamu pilih salah, silakan pilih lagi !!")
            pilih_Menu = int(input("Pilih Menu : "))

        UI.divider2()
        print("\n")
        match pilih_Menu :
            case 1 : CRUD.create()
            case 2 : CRUD.read()
            case 3 : CRUD.update()
            case 4 : CRUD.delete()
        print("\n")
        UI.divider2()
        print("\n")

        is_done = input("\nApakah lanjut (y/n) : ")
        if is_done == "n" or is_done == "N":
            break
    
    UI.divider()
    print(f"{'===== Program Selesai =====':^45}")
    UI.divider()