from django.contrib import admin

from SerdarsBlog.models import Post, UserProfile

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']

class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ['user']

admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

