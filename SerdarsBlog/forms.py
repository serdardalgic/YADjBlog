from django.forms import (EmailField, CharField,
                        DateTimeField)

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

import hashlib
import random
import datetime

class UserForm(UserCreationForm):
    email = EmailField(required=True)
    activation_key = CharField(max_length=40, required=False)
    key_expires = DateTimeField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self):
        user = User.objects.create_user(
                username = self.cleaned_data['username'],
                email = self.cleaned_data['email'],
                password = self.cleaned_data['password1']
                )
        user.is_active = False
        user.save()
        # activation
        salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
        username = user.username
        if isinstance(username, unicode):
            username = username.encode('utf-8')
        activation_key = hashlib.sha1(salt+username).hexdigest()
        key_expires = datetime.datetime.today()+datetime.timedelta(2)

        # send_activation email


