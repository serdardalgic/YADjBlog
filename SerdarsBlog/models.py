#import datetime

from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    # created = models.DateTimeField(editable=False)
    # modified = models.DateTimeField()

    def __unicode__(self):
        return self.title

    #def save(self, *args, **kwargs):
        #''' On save, update timestamps '''

        #if not self.id:
            #self.created = datetime.datetime.today()
        #self.modified = datetime.datetime.today()
        #super(Post, self).save(*args, **kwargs)
