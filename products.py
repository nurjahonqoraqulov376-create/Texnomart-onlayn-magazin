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

# 10. git init ---- bu yangi bo'sh git papkasini qushib beradi
# 11.git status ----- bu nimalar bajarilayotganini va bajarilganini kurishimiz mumkin
# 12.git add . ----- bu proyektingizdagi xamma fayllarini saqlab beradi
# 13.git commit -m 'your message' ---- bu saqlangan faylarningizga izoh yozish
# 14. git push origin main ---- bu proyektingizdagi fayllarni githupga uzatadi
# 15.git pull origin main ---- bu yuborgan fayllarizni yuklab oladi
# 16. git branch ---- bu branchlar ruyxatini kursatadi
# 17. git chekout branch_name ---- bu ko'rsatilgan branchingizga o'tishni taminlaydi
# 18. git checkout -b new_branch ---- bu yangi branch ochadi va unga bog'lab quyadi
# 19. git merge branch_name ---- bu ko'rsatilgan branchdagi uzgarishlarni uziga maqul kelsa yuklab oladi
# 20. git clone URL --- bu githupda masofaviy proyektingni url orqali  bog'lash
# 21. git log ---- bu barcha commitlardagi uzgarishlar tarixini kursatadi