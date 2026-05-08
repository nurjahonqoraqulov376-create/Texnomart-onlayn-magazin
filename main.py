#  shu fayllar buyicha ishlaymiz bollar


from auth import login, register
from products import show_products, add_product


def main_menu():
    while True:
        print("\n==== TEXNOMART DASTURI ====")
        print("1. Login")
        print("2. Ro'yxatdan o'tish")
        print("3. Mahsulotlar ro'yxati")
        print("4. Mahsulot qo'shish")
        print("0. Chiqish")

        choice = input("Tanlang: ")

        if choice == "1":
            login()
        elif choice == "2":
            register()
        elif choice == "3":
            show_products()
        elif choice == "4":
            add_product()
        elif choice == "0":
            print("Dasturdan chiqildi!")
            break
        else:
            print("Noto‘g‘ri tanlov. Qayta urinib ko‘ring.")


if __name__ == "__main__":
    main_menu()