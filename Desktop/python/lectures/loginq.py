
username = "tirup"
passwd = "12345678"

def login():
    password = input("password sholud be 8 cha long...")
    a = len(password)
    if a >= 8:
        uname = input("enter ur username...")
        if (uname == username and passwd == password):
            print("login success")
        else:
            print("inalid")
    else:
        print("invalid password length..")


login()