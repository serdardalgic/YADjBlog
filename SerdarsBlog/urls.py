from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('SerdarsBlog.views',
    # Examples:
    # url(r'^$', 'DjangoBlogProject.views.home', name='home'),
    # url(r'^DjangoBlogProject/', include('DjangoBlogProject.foo.urls')),

    url(r'^$', 'home', name='home'),
    url(r'^(\d+)/$', 'post', name='post'),
    url(r'^logout/$', 'logout_page'),
    url(r'^login/$', 'login_page'),
)
