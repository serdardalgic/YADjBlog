import datetime
import hashlib
import random

def create_salt():
    salt = hashlib.sha1(str(random.random())).hexdigest()[:5]

def create_activation_key(salt, username):
    return hashlib.sha1(salt + username).hexdigest()

def create_expire_date():
    return datetime.datetime.today() + datetime.timedelta(2)

