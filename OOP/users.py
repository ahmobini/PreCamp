import re
from cryptography.fernet import Fernet


class UserManager:

    __secret_key = Fernet.generate_key()

    @classmethod
    def check_password(cls, password):
        if not all([re.search("[a-z]", password), re.search("[A-Z]", password), len(password) > 7]):
            raise Exception('invalid password')
        fernet = Fernet(cls.__secret_key)
        return fernet.encrypt(bytes(password, 'utf-8'))

    @classmethod
    def compare_password(cls, encoded_password, password):
        fernet = Fernet(cls.__secret_key)
        return fernet.decrypt(encoded_password) == password

    @classmethod
    def check_phone_number(cls, phone_number):
        if not any([re.search("^\+989[0-3,9]\d{8}$", phone_number), re.search("^09[0-3,9]\d{8}$", phone_number)]):
            raise Exception('invalid phone number')
        return phone_number

    @staticmethod
    def check_email(email):
        pass

    @classmethod
    def check_user_name(cls, username):
        if not re.search("^\w+_\w+$", username):
            raise Exception('invalid username')
        return username


class User:
    def __init__(self, username, phone_number, email, password):
        self.username = UserManager.check_user_name(username)
        self.password = UserManager.check_password(password)
        self.phone_number = UserManager.check_phone_number(
            phone_number)
        self.email = email

    def __str__(self):
        return self.username


if __name__ == '__main__':
    user = User('alireza_helali', '09163311945',
                'a.helali1995@gmail.com', "A.helali1995")
    print(user.password)
