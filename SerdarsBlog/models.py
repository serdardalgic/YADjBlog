from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import (GenericForeignKey,
                                                 GenericRelation)
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    comments = GenericRelation('SerdarsBlog.Comment')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-created_on']


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=80)
    website = models.URLField(max_length=200, null=True, blank=True)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # Content_object model
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    parent_object = GenericForeignKey('content_type', 'object_id')
    # Child Comments
    comments = GenericRelation('SerdarsBlog.Comment')

    def __unicode__(self):
        return 'Comment %s - to %s %s:::: %s' % (self.id,
                                                 self.content_type,
                                                 self.object_id,
                                                 self.created_on)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    is_verified = models.BooleanField(default=False)
    activation_key = models.CharField(max_length=60)
    key_expires = models.DateTimeField()

    def __unicode__(self):
        return self.user.username
