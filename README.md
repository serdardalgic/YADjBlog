YADjBlog
========

Yet Another Django Blog

* Uses Postgresql for the db. DatabaseName is django_blog_db
* You should run these commands before firing up the blog:<br />
 `python manage.py collectstatic` <br />
 `python manage.py syncdb`<br />
* Then you can start the server by giving runserver command:<br/>
 `python manage.py runserver`<br/>

The static files (main.css, images) and templates are taken from [PyLadiesBYOBlog](https://github.com/econchick/PyLadiesBYOBlog)

## General Guidelines
1. Coding should obey PEP8 rules restrictly.
2. All html forms must be validated using django form. See [Django form and field validation](https://docs.djangoproject.com/en/1.3/ref/forms/validation/) for details.
3. ~~GenericForeignKey's must be used. See [Content Types Framework](https://docs.djangoproject.com/en/1.3/ref/contrib/contenttypes/) for details.~~ 
4. Caching should be encouraged. [Redis](http://redis.io/) must be used for cache backend. See [redis-py](https://github.com/andymccurdy/redis-py/) for details.
5. Users can use up-to-a-certain-size images in their blog posts. These images must be resized using PIL, by using celery tasks in the backend part. For image upload, see [File Uploads](https://docs.djangoproject.com/en/1.3/topics/http/file-uploads/) ; HINT: a)celery decorator @task, check [celery docs](http://docs.celeryproject.org/en/latest/index.html) b)[StackOverflow Q1](http://stackoverflow.com/questions/4330719/django-celery-how-to-send-request-filesphoto-to-task)
6. ~~Every user must have a profile. Use UserProfile of Django1.3, See [User authentication in Django](https://docs.djangoproject.com/en/1.3/topics/auth/) for details.~~
7. Users:
  * ~~can register by their e-mail address. That e-mail address should be verified via sending an authentication mail.~~
  * ~~can login via e-mail~~
  * ~~can create/edit a Blog Post (Needs login)~~
  * ~~can see Blog Posts~~
  * ~~can comment on Blog Posts (Needs login)~~
  * ~~can comment on Comments (Needs login)~~
  * ~~can change their Profile infos (Needs login)~~
  * ~~can update their passwords (Needs login)~~
  * ~~can update their e-mails (Needs login)~~
  * ~~can disable their accounts (Needs login)~~

Skip the anonymous users for now.

### TODO:
  * Use redirect shortcuts
  * Use reverse
  * Combine confirm and confirm_verification views. After confirmation, log in the user.
  * Make all strings translatable
  * Drop messages in login_page view, use field validation.
