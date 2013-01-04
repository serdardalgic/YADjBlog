from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoBlogProject.views.home', name='home'),
    # url(r'^DjangoBlogProject/', include('DjangoBlogProject.foo.urls')),

    url(r'^$', 'SerdarsBlog.views.home', name='home'),
    url(r'^(\d+)/$', 'SerdarsBlog.views.post', name='post'),
    url(r'^logout/$', 'SerdarsBlog.views.logout_page'),
)
