from cryptography.fernet import Fernet

"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)"""

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("What is the master password ?\n")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open("Password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split(" : ")
            print(f"Username : {user} / Password : {fer.decrypt(passw.encode()).decode()}")

def add():
    name = input("Account Name : ")
    pwd = input("Password : ")

    with open("Password.txt", "a") as f:
        f.write(name + " : " + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("\nAdd a new password or view a password\n"
                 "(Press 'X' to quit) View or Add or Quit:\n"
                 )

    if mode.lower() == "x":
        break

    elif mode == "view":
        view()
        continue

    elif mode == "add":
        add()
        continue

    else:
        print("Invalid Mode...")
        break