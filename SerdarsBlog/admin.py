from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from SerdarsBlog.models import Post, UserProfile, Comment


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']


class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ['user']
    list_display = ['user', 'is_verified']


class CommentsAdmin(admin.ModelAdmin):
    search_fields = ['email']

UserAdmin.list_display = ('email', 'first_name', 'last_name',
                          'is_active', 'is_staff')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Comment, CommentsAdmin)
