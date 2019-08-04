from src.models import Users, Token
import binascii,os
import hashlib

SALT_LENGTH = 16
HASH_METHOD = "SHA512"

class LoginLib():
    def __init__(self):
        print "Login Lib is working"

    def password_hashing(self, password, salt=None):
        if not salt:
            salt = binascii.hexlify(os.urandom(SALT_LENGTH / 2)).decode()

        hash_library = hashlib.new(HASH_METHOD)

        salted_client_hash = str(password + salt)
        hash_library.update(salted_client_hash)

        server_hash = hash_library.hexdigest()
        return server_hash, salt

    def validatelogin(self, login_detail):
        if "email_id" not in login_detail:
            return "key 'email_id' is not provided", False
        if "password" not in login_detail:
            return "key 'password' is not provided",False

        users = Users.objects.filter(email_id = login_detail["email_id"])
        if users.count()>0:
            selected_user=users[0]
            password_from_db = selected_user.password
            salt_from_db = selected_user.salt

            password_hash_req, salt = self.password_hashing(
                password = login_detail["password"], salt=salt_from_db
            )

            print password_from_db
            print password_hash_req


            if password_from_db == password_hash_req:
                return "Login validation successful", True
            else:
                return "Invalid password", False


        return "User not found", False

    def login(self,login_detail):
        message, status = self.validatelogin(login_detail)
        if (status):
            return "Continue with login process", True
        else:
            return message,False
