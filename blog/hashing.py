from passlib.context import CryptContext


class Hash:
    pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @staticmethod
    def bcrypt(password: str):
        hashPassword = Hash.pwd_cxt.hash(password)
        return hashPassword

    @staticmethod
    def verify_password(hashed_passwd, plain_passwd):
        return Hash.pwd_cxt.verify(plain_passwd, hashed_passwd)
