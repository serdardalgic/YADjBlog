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
3. GenericForeignKey's must be used. See [Content Types Framework](https://docs.djangoproject.com/en/1.3/ref/contrib/contenttypes/) for details. 
4. Caching should be encouraged. [Redis](http://redis.io/) must be used for cache backend. See [redis-py](https://github.com/andymccurdy/redis-py/) for details.
5. Every user must have a profile. 
