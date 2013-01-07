from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('SerdarsBlog.views',
    # Examples:
    # url(r'^$', 'DjangoBlogProject.views.home', name='home'),
    # url(r'^DjangoBlogProject/', include('DjangoBlogProject.foo.urls')),

    url(r'^$', 'home', name='home'),
    url(r'^(\d+)/$', 'post', name='post'),
    url(r'^logout/$', 'logout_page', name='logout'),
    url(r'^login/$', 'login_page', name='login'),
    url(r'^adduser/$', 'add_user'),
    url(r'^confirm/(?P<activation_key>\w+)/$', 'confirm', name='confirm'),
    url(r'^profile/$', 'profile_info', name='profile'),

    #url(r'^changeemail/$', changeemail, name="change_email"),

)
