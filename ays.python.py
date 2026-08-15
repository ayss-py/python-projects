class istifadeci:
    def __init__(self, username, password):
        self.username = username
        self.password = password


istifadeciler = []


def register():
    username=input("Username: ")
    password=input("Password: ")

    for i in istifadeciler:
        if i.username==username:
            print("Bu username artiq movcuddur")
            break
    else:
        yeni_istifadeci=istifadeci(username,password)
        istifadeciler.append(yeni_istifadeci)
        print("Qeydiyyat ugurludur!")

def login():
    username1 = input("Username: ")
    password1 = input("Password: ")
    for j in istifadeciler:
            if j.username == username1 and j.password == password1:
                print("Login ugurludur!")
                return j 
            else:
                print("Username ve ya password yanlisdir!")


while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    secim=input("Seciminiz: ")

    if secim == "1":
        register()
        
    elif secim == "2":
        aktiv_user=login()
        
        if aktiv_user:
            print("Xos geldin, ")

            while True:
                print("\n1. Logout")
                print("2. Exit")

                secim2=input("Seciminiz: ")

                if secim2=="1":
                    print("Logout olundu")
                    break

                elif secim2=="2":
                    print("Programdan cixildi")
                    exit()

                else:
                    print("Yanlis secim!")
    elif secim=="3":
        print("Programdan cixildi")
        break
    else:
        print("Yanlis secim!")
        
                
