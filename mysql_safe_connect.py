import mysql.connector
from passwd_utils import get_decrypted_passwd
from encrypt import *


    
def connect_mysql():
    try:
       conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = get_decrypted_passwd(),
            database = 'py_db'
        )
               
    except Exception :
        print('Authentication Failed')
    
    else:
        print('.....Your Connected to MySQL SuccessFully.....')
        conn.close()           
        
    

if __name__=='__main__':
    generate_key()
    connect_mysql()

