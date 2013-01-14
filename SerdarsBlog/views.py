import datetime
import hashlib

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext as _

from SerdarsBlog.models import Post, UserProfile
from SerdarsBlog.forms import (UserForm, ChangeEmailForm,
                               BlogPostForm, CommentForm)
from SerdarsBlog.utils import uri_b64decode
from SerdarsBlog.decorators import anonymous_required


def home(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)

    try:
        page = int(request.GET.get("page", 1))
    except ValueError:
        page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return render(request, "list.html", dict(posts=posts, user=request.user))


def post(request, pk_id):
    post = get_object_or_404(Post, pk=int(pk_id))
    return render(request, "post.html", dict(post=post, user=request.user))


@login_required
def addpost(request):
    if request.POST:
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            return HttpResponseRedirect('/')
    else:
        form = BlogPostForm(request.POST)

    return render(request,
                  'addpost.html',
                  {'form': form})


def addcomment(request, pk_id):
    post = get_object_or_404(Post, pk=int(pk_id))
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save(post)
            return HttpResponseRedirect('/')
    else:
        form = CommentForm(request.POST)

    return render(request, 'addcomment.html',
                  {'post': post, 'form': form})


@login_required
def edit(request, pk_id):
    post = get_object_or_404(Post, pk=int(pk_id))
    if request.user.is_staff or request.user.id == post.author.id:
        if request.POST:
            postform = BlogPostForm(request.POST)
            if postform.is_valid():
                postform.save(request.user, post)
                return HttpResponseRedirect('/')
        else:
            postform = BlogPostForm({'title': post.title,
                                     'body': post.body})
        return render(request, 'edit.html', {'pk_id': pk_id, 'form': postform})
    else:
        messages.error(request, _('You can not edit this post, '
                                  'because you are not the author '
                                  'of it.'))


@login_required
def changepass(request):
    return HttpResponseRedirect('/')


def noconfirm_when_others_authenticated(request):
    return render(request, 'error/noconfirmothersauth.html')


@login_required
def change_email(request):
    if request.POST:
        form = ChangeEmailForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            #TODO: redirect to somewhere with a meaning
            return HttpResponseRedirect('/profile')
    else:
        form = ChangeEmailForm()

    return render(request,
                  'changeemail.html',
                  {'form': form})


#@login_required
def disable_account(request):
    userProfile = get_object_or_404(UserProfile, user=request.user)
    userProfile.user.is_active = False
    userProfile.user.save()
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def profile_info(request):
    return render(request, 'profile.html')


def add_user(request):
    if request.POST:
        data = request.POST.copy()
        #FIXME: Maybe, below code can be a separate function,
        #       like clean_username()
        username = data['email']
        username = hashlib.sha1(username.lower()).hexdigest()[:30]
        data['username'] = username
        form = UserForm(data)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserForm()

    return render(request, 'adduser.html', {'form': form})


# new user confirmation:
# TODO: must not be logged in decorator should be put here.
@anonymous_required
def confirm(request, activation_key):
    user_profile = get_object_or_404(UserProfile,
                                     activation_key=activation_key)

    if user_profile.key_expires < datetime.datetime.today():
        #TODO: some kind of notification should be raised!
        return HttpResponseRedirect('/')

    # activate the user
    user_profile.is_verified = True
    user_profile.save()

    # FIXME: Check below, maybe we don't need this user_account
    user_account = user_profile.user
    user_account.save()
    # TODO: this user should be logged-in

    return HttpResponseRedirect('/')


@anonymous_required
def confirm_verification(request, activation_key):
    user_profile = get_object_or_404(UserProfile,
                                     activation_key=activation_key)

    if user_profile.key_expires < datetime.datetime.today():
        #TODO: some kind of notification should be raised!
        return HttpResponseRedirect('/')

    user_account = user_profile.user
    user_account.email = uri_b64decode(str(activation_key[20:]))
    user_account.save()
    user_profile.save()

    return HttpResponseRedirect('/')


@anonymous_required
def login_page(request):
    messages.info(request, _('Please log in below...'))
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.info(request, _('You\'re successfully logged in!'))
                return HttpResponseRedirect('/')
            else:
                #TODO: More options:
                # "is active" and "is verified" should be clarified.
                # MARK AS LATER!
                messages.warning(request, _('Your account is not active,'
                                 'please contact the site admin.'))
        else:
            messages.error(request, _('Your username and/or'
                                      'password were incorrect.'))

    return render(request, 'login.html',
                  {'username': username})


@login_required
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
