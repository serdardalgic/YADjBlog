from django.conf.urls.defaults import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'DjangoBlogProject.views.home', name='home'),
    # url(r'^DjangoBlogProject/', include('DjangoBlogProject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Password change
    url(r'^changepass/$',
        'django.contrib.auth.views.password_change',
        name='change_password'),
    url(r'^password_change_done/$',
        'django.contrib.auth.views.password_change_done',
        {'template_name': 'profile.html'}),

    url(r'^', include('SerdarsBlog.urls')),
)
