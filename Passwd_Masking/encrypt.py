from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()

    with open("secret.key","wb") as f:
        f.write(key)
        print("Key Successfully saved to 'secret.key'")

def encrypt_passwd(passwd):
    key = open('secret.key','rb').read()
    f=Fernet(key)
    encrypted = f.encrypt(passwd.encode())
    return encrypted

    