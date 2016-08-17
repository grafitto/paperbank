import uuid
import hashlib
import random

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