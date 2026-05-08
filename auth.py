users = {}

def register():
    print("\n=== Ro'yxatdan o'tish ===")
    username = input("Yangi login kiriting: ")
    password = input("Parol kiriting: ")

    if username in users:
        print("Bu login allaqachon mavjud!")
    else:
        users[username] = password
        print("Muvaffaqiyatli ro'yxatdan o'tdingiz!")

def login():
    print("\n=== Tizimga kirish ===")
    username = input("Login: ")
    password = input("Parol: ")

    if username in users and users[username] == password:
        print("Xush kelibsiz,", username)
        return True
    else:
        print("Login yoki parol noto'g'ri!")
        return False