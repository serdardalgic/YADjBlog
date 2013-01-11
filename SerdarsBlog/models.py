from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-created_on']


class Comment(models.Model):
    # TODO: Comments can be linked with parent relationship
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=80)
    website = models.URLField(max_length=200, null=True, blank=True)
    text = models.TextField()
    post = models.ForeignKey(Post)
    created_on = models.DateTimeField(auto_now_add=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    is_verified = models.BooleanField(default=False)
    activation_key = models.CharField(max_length=60)
    key_expires = models.DateTimeField()

    def __unicode__(self):
        return self.user.username
