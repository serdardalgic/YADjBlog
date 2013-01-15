from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'SerdarsBlog.views',
    # Examples:
    # url(r'^$', 'DjangoBlogProject.views.home', name='home'),
    # url(r'^DjangoBlogProject/', include('DjangoBlogProject.foo.urls')),

    url(r'^$', 'home', name='home'),
    url(r'^(\d+)/$', 'post', name='post'),
    url(r'^logout/$', 'logout_page', name='logout'),
    url(r'^login/$', 'login_page', name='login'),
    url(r'^adduser/$', 'add_user', name='add_user'),
    url(r'^addpost/$', 'addpost', name='addpost'),
    url(r'^addcomment/(?P<comment_to>\w+)/(?P<pk_id>\d+)/$', 'addcomment', name='add_comment'),
    url(r'^edit/(?P<pk_id>\d+)/$', 'edit', name='edit'),
    url(r'^confirm/(?P<activation_key>\w+)/$', 'confirm', name='confirm'),
    url(r'^confirm_verify/(?P<activation_key>\w+)/$', 'confirm_verification',
        name='confirm_verification'),
    url(r'^profile/$', 'profile_info', name='profile'),

    url(r'^error/noconfirmothersauth/$', 'noconfirm_when_others_authenticated',
        name='noconfirmothersauth'),

    url(r'^changeemail/$', 'change_email', name="change_email"),
    url(r'^disable/$', 'disable_account', name="disable")

)
