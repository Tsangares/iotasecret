from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import time,json,base64,random
class Crypt:
    LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ9"
    def __init__(self,secret):
        random.seed(secret+"426838")
        self.address = ''.join(random.choice(self.LETTERS) for i in range(81))
        self.f = Fernet(self.genKey(secret))
        
    def encrypt(self,string):
        return self.f.encrypt(bytes(string,'utf-8'))
    
    def decrypt(self,byteString):
        try:
            return str(self.f.decrypt(byteString),'utf-8')
        except TypeError:
            raise Exception("ERROR: Trying to decrypt something that is not encrypted.")

    
    def genKey(self,secret):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=bytes(83),
            iterations=100000,
        )
        return base64.urlsafe_b64encode(kdf.derive(bytes(secret,'utf-8')))
