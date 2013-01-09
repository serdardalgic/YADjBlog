import hashlib
import random
import datetime

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django import forms

from SerdarsBlog.models import UserProfile

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email address', max_length=75)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            user = User.objects.get(email=email)
            raise forms.ValidationError("This email address is already taken.")
        except User.DoesNotExist:
            return email

    def save(self):
        # check Form validation.
        user = User.objects.create_user(
                username = self.cleaned_data['username'],
                email = self.cleaned_data['email'],
                password = self.cleaned_data['password1']
                )
        user.save()
        # activation
        salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
        username = user.username
        if isinstance(username, unicode):
            username = username.encode('utf-8')
        activation_key = hashlib.sha1(salt+username).hexdigest()
        key_expires = datetime.datetime.today()+datetime.timedelta(2)

        new_user = UserProfile(user = user, activation_key = activation_key,
                key_expires = key_expires, is_verified = False)
        new_user.save()

        # send_activation email

        email_subject = 'SerdarsBlog - Confirmation for Your New Account'
        email_body = ('Hello! Thanks for registering for the blog \n' +
        'In order to active your account, click following link in ' +
        'the next 48 hours: \n http://localhost:8000/confirm/%s') % activation_key

        send_mail(email_subject, email_body, 'sd@serdardalgic.org', [user.email])


