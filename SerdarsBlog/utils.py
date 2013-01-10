import datetime
import hashlib
import random

from base64 import urlsafe_b64encode, urlsafe_b64decode

def create_salt():
    return hashlib.sha1(str(random.random())).hexdigest()[:5]

def create_activation_key(user, email):
    username = user.username
    usersha = hashlib.sha1(create_salt() + username).hexdigest()
    encoded_email = encode_mail(email)
    return {usersha : usersha, encoded_email : encoded_email}

def create_expire_date():
    return datetime.datetime.today() + datetime.timedelta(2)

def encode_mail(email):
    return base64.uri_b64encode(email)

def uri_b64encode(s):
    return urlsafe_b64encode(s).strip('=')

def uri_b64decode(s):
    return urlsafe_b64decode(s + '=' * (4 - len(s) % 4))
