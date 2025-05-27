
from cryptography.fernet import Fernet
from encrypt import *

class FakeStr(str):
    def __str__(self):
        return "********"
    def __repr__(self):
        return "********"
    

def load_key():
    return open('secret.key','rb').read()

def decrypt_passwd(encrypted_passwd):
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_passwd).decode()
    return FakeStr(decrypted)


def get_decrypted_passwd():
    encrypted_passwd = encrypt_passwd(input('Enter The MySQL Password : '))
    return decrypt_passwd(encrypted_passwd)