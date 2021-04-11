from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes='bcrypt', deprecated='auto')

class Hash:
    def hash_password(self, password:str):
        return pwd_cxt.hash(password)

    def verify(self, hashed_password,plain_password):
        return pwd_cxt.verify(plain_password,hashed_password)