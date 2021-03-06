import uuid
import hashlib
import random
import boto3 

class Utilities:

    @staticmethod
    def hash_password(password):
        """Hashes the password provided"""
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ":" + salt

    @staticmethod
    def check_password(user_password, hashed_password):
        salt = hashed_password.split(":")[1]
        return hashed_password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest() + ":" + salt

    @staticmethod
    def magic_word_random_flash():
        flashes = ["Are you sure that's the magic word?", "Now, relax and try again", "Try again, Am still here. Waiting.."]
        return flashes[random.randint(0, len(flashes) - 1)]

    @staticmethod
    def allowed_file(filename):
        ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'docx'])
        return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

    @staticmethod
    def download():
        s3Client = boto3.client('s3')
        s3Client.generate_presigned_url('get_object', Params = {'Bucket': 'www.mybucket.com', 'Key': 'hello.txt'}, ExpiresIn = 100)