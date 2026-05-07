# texnomart/
# ├── main.py                        ← Dastur kirish nuqtasi
# ├── models/
# │   └── db.py                      ← JSON fayl orqali ma'lumot saqlash
# ├── services/
# │   ├── mahsulot_service.py        ← Mahsulot CRUD funksiyalari
# │   ├── savat_service.py           ← Savatcha funksiyalari
# │   ├── buyurtma_service.py        ← Buyurtma funksiyalari
# │   └── foydalanuvchi_service.py   ← Ro'yxat/kirish funksiyalari
# └── utils/
#     ├── chiqish.py                 ← Rangli terminal chiqishi, jadval
#     └── menu.py                    ← Menyu va kiritish yordamchilari

#  shu fayllar buyicha ishlaymiz bollar


def asosiy_menyu():
    """Dasturning asosiy menyusini ko'rsatadi"""
    while True:
        separator()
        buyumlar("🛒  TEXNOMART - Elektronika Do'koni")
        separator()
        menyu_chiqar([
            "Mahsulotlar",
            "Savatcha",
            "Buyurtmalar",
            "Foydalanuvchi",
            "Chiqish",
        ])

        tanlov = tanlov_ol(1, 5)

        if tanlov == 1:
            mahsulotlar_menyusi()
        elif tanlov == 2:
            savat_menyusi()
        elif tanlov == 3:
            buyurtma_menyusi()
        elif tanlov == 4:
            foydalanuvchi_menyusi()
        elif tanlov == 5:
            rang("\n✅  Xayr! Yana keling!", "yashil")
            break
