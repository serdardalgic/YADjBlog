# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import ugettext as _

from SerdarsBlog.models import Post

def home(request):
    posts = Post.objects.all().order_by("-created_on")
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


def post(request, pk):
    post = Post.objects.get(pk=int(pk))
    return render(request, "post.html", dict(post=post, user=request.user))

def login_page(request):
    state = _("Please log in below...")
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = _("You're successfully logged in!")
                return HttpResponseRedirect('/')
            else:
                state = _("Your account is not active, please contact the site admin.")
        else:
            state = _("Your username and/or password were incorrect.")

    return render(request, 'login.html', {'state':state, 'username': username})


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

