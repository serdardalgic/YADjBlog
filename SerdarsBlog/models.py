#import datetime
from django.db import models
from django.template.defaultfilters import slugify

from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    # created_on = models.DateTimeField(editable=False)
    # modified = models.DateTimeField()

    def __unicode__(self):
        return self.title

    #def get_absolute_url(self):
        #return ('blog_post_detail', (),
                #{
                    #'slug' :self.slug,
                #})

    #def save(self, *args, **kwargs):
        #if not self.slug:
            #self.slug = slugify(self.title)

        ##''' On save, update timestamps '''

        ##if not self.id:
            ##self.created_on = datetime.datetime.today()
        ##self.modified = datetime.datetime.today()
        #super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=80)
    website = models.URLField(max_length=200, null=True, blank=True)
    text = models.TextField()
    post = models.ForeignKey(Post)
    created_on = models.DateTimeField(auto_now_add=True)

