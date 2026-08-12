#password manager 
import os
from cryptography.fernet import Fernet
import hashlib
import base64

def setup_master_password():
    master_pass = input("Please select your master password")
    hashed_password = hashlib.sha256(master_pass.encode()).hexdigest()
    with open("master.txt", 'w') as f:
        f.write(hashed_password)
        print("Master password created")


def verify_master_password():
    entered_password = input("Enter master password: ")
    entered_hashed = hashlib.sha256(entered_password.encode()).hexdigest()
    with open("master.txt", "r") as f:
        saved_pass = f.read()

        if entered_hashed == saved_pass:
            print("Acess Granted")
        else:
            print("Wrong master password")
            quit()

if os.path.exists("master.txt"):
    verify_master_password()
else:
    setup_master_password()

def load_key():
   file = open("key.key","rb")
   key = file.read()
   file.close()
   return key


key = load_key()
fer = Fernet(key)
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key" ,"wb") as key_file:
        key_file.write(key)

write_key()
'''
#just used this directry to create the key.key foler from fernet

def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data =line.rstrip()
            user , passw = data.split("|")
            print("user: ",user, "Password: ",fer.decrypt(((passw.encode()))).decode())

def add():
    name = input("Account name")
    password = input("Password: ")

    with open("password.txt", "a") as f:
        f.write(name + "|" +fer.encrypt(password.encode()).decode() + "\n")



while True:
    mode = input("Woulld you like to add a password or view your password?\n 1.View \n 2.Add \n \n If you want to exit press q ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()
        

    elif mode == "add":
        add()
        

    else:
        print("Invalid option")
        continue

