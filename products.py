products = ["Telefon", "Noutbuk", "Televizor"]

def show_products():
    print("\n--- Mahsulotlar ro'yxati ---")
    for i, p in enumerate(products, 1):
        print(f"{i}. {p}")


def add_product():
    print("\n--- Mahsulot qo'shish ---")
    name = input("Mahsulot nomi: ")
    products.append(name)
    print(f"'{name}' mahsuloti qo‘shildi.")