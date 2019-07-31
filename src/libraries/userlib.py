from src.models.users import Users
import binascii,os
import hashlib

SALT_LENGTH = 16
HASH_METHOD = "SHA512"

class UserLib():

    def __init__(self):
        print "Initialized User Lib"

    def password_hashing(self,password,salt=None):
        if not salt:
            salt = binascii.hexlify(os.urandom(SALT_LENGTH/2)).decode()

        hash_library = hashlib.new(HASH_METHOD)

        salted_client_hash = str(password + salt)
        hash_library.update(salted_client_hash)

        server_hash = hash_library.hexdigest()
        return server_hash, salt

    @property
    def validate_input(self):
        if "name" not in self.user_info:
            return "Missing key 'name'", False

        if "email_id" not in self.user_info:
            return "Missing key 'email_id'", False

        if "password" not in self.user_info:
            return "Missing key 'password'", False

        users = Users.objects.filter(email_id=self.user_info["email_id"])
        if users.count() > 0:
            return "User already exists", False

        return "Success", True


    def CreateUser(self, user_info):

        self.user_info = user_info
        message, status = self.validate_input

        if status:
            print "Validation is successfull", self.user_info
            password_hash, salt = self.password_hashing(self.user_info["password"])
            print password_hash, salt

            self.user_info["password"] = password_hash
            self.user_info["salt"] = salt


            Users.objects.create(**self.user_info)

        else:
            return message,False
        print "User created successfully", True