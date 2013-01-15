from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.utils.translation import ugettext as _
from django import forms

from SerdarsBlog import utils
from SerdarsBlog.models import Post, UserProfile, Comment


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True,
                             label='Email address',
                             max_length=75)

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
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1'])
        user.save()

        # activation
        activation_key = utils.create_activation_key(user, user.email)
        key_expires = utils.create_expire_date()

        new_user = UserProfile(user=user,
                               activation_key=activation_key,
                               key_expires=key_expires,
                               is_verified=False)
        new_user.save()

        # send_activation email

        email_subject = 'SerdarsBlog - Confirmation for Your New Account'
        email_body = ('Hello! Thanks for registering for the blog \n'
                      'In order to active your account,'
                      'click following link in the next 48 hours: \n'
                      'http://localhost:8000/confirm/%s') % activation_key

        send_mail(email_subject, email_body,
                  'sd@serdardalgic.org', [user.email])


class ChangeEmailForm(forms.Form):
    new_email_address = forms.EmailField(
        _(u'new e-mail address'),
        help_text=_(u'Your old email address will be used'
                    'until you verify your new one.'),
        required=True,
        label='New Email Address')

    def save(self, user):
        userProfile = UserProfile.objects.get(user=user)
        userProfile.activation_key = utils.create_activation_key(
            user,
            self.cleaned_data["new_email_address"])

        userProfile.key_expires = utils.create_expire_date()
        userProfile.save()
        self.send_verification(userProfile)

    def clean_email(self):
        new_email_address = self.cleaned_data["email"]
        try:
            user = User.objects.get(email=new_email_address)
            raise forms.ValidationError("This email address is already taken.")
        except User.DoesNotExist:
            return new_email_address

    def send_verification(self, userProfile):

        email_subject = ('SerdarsBlog - Verify your new email' +
                         'address for SerdarsBlog')
        email_body = ('Hi! You or another person wanted to change your ' +
                      'SerdarsBlog account\'s email with this e-mail.' +
                      'If you agree to change your e-mail, click on' +
                      'the link below in the next 48 hours: \n' +
                      'http://localhost:8000/confirm_verify/%s'
                      ) % userProfile.activation_key

        send_mail(email_subject, email_body,
                  'sd@serdardalgic.org',
                  [self.cleaned_data["new_email_address"]])


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ["author", "created_on"]
        widgets = {'body': forms.Textarea(attrs={'cols': 100, 'rows': 20}), }

    def save(self, user, post=None):
        if post:
            post.title = self.cleaned_data["title"]
            post.body = self.cleaned_data["body"]
        else:
            post = Post(author=user,
                        title=self.cleaned_data["title"],
                        body=self.cleaned_data["body"])
        post.save()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["created_on", "content_type", "object_id"]
        widgets = {'text': forms.Textarea(attrs={'cols': 60, 'rows': 10}), }

    def save(self, parent):
        comment = Comment(name=self.cleaned_data["name"],
                          email=self.cleaned_data["email"],
                          website=self.cleaned_data["website"],
                          text=self.cleaned_data["text"],
                          parent_object=parent
                          )
        comment.save()
