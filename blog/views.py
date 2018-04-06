from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.views.generic import RedirectView
from .models import Post, Profile
from django.utils import timezone
from .forms import PostForm, LoginForm, ProfileForm, RegistrationForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'myblog2/post_detail.html', {'post': post})


def users_list(request):
    users = User.objects.all().order_by('username')
    return render(request, 'myblog2/users.html', {'users': users})


def list_of_posts(request, username):
    myuser = get_object_or_404(User, username=username)
    profile, is_created = Profile.objects.get_or_create(user=myuser)
    user_posts = Post.objects.filter(author__username__exact=username)
    paginator = Paginator(user_posts, 4)
    page = request.GET.get('page')
    try:
        user_posts= paginator.page(page)
    except PageNotAnInteger:
        user_posts = paginator.page(1)
    except EmptyPage:
        user_posts = paginator.page(paginator.num_pages)
    return render(request, 'myblog2/list_of_posts.html',
                  {'user_posts': user_posts, 'name': username, 'profile': profile})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'myblog2/post_new.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'myblog2/post_edit.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            if form.get_user():
                login(request, form.get_user())
                return HttpResponseRedirect('/author/username/', username=form.username)
    else:
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})


def log_out(request):
    logout(request)
    return HttpResponseRedirect('login')


def who_is_it(request):
    return redirect('list_of_posts', username=request.user.username)


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('list_of_posts', username=post.author)


def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    is_liked = post.user_likes.filter(username=request.user.username)
    if is_liked.__bool__():
        post.unlike()
        post.user_likes.remove(request.user)
    else:
        post.like()
        post.user_likes.add(request.user)
    return redirect('post_detail', pk=pk)


def post_like2(request, pk):
    post = get_object_or_404(Post, pk=pk)
    is_liked = post.user_likes.filter(username=request.user.username)
    if is_liked.__bool__():
        post.unlike()
        post.user_likes.remove(request.user)
    else:
        post.like()
        post.user_likes.add(request.user)
    return redirect('list_of_posts', username=post.author)


def profile_edit(request):
    profile, is_created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('who_is_it')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'myblog2/profile_edit.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            newuser = form.myuser()
            login(request, newuser)
            return redirect(who_is_it)
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
