from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse
import json

from .models import User, Post, Follow, Like


def index(request):
    # Get all posts from user in descending order to display latest post on topmost
    allpost = Post.objects.all().order_by("id").reverse()
    # Create paginator of 10 objects for a single page
    paginator = Paginator(allpost, 10)
    page_number = request.GET.get("page")
    page_item = paginator.get_page(page_number)
    # Get all liked posts
    allpost_like = Like.objects.all()
    # Check if user is logged in and update list of liked posts by respective user. Returns an empty list if user not logged in.
    userpost_like = []
    try:
        for like in allpost_like:
            if like.user.id == request.user.id:
                userpost_like.append(like.post.id)
    except:
        userpost_like = []

    return render(request, "network/index.html", {
        "allpost": allpost,
        "pageitem": page_item,
        "userpost_like": userpost_like
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


def new_post(request):
    if request.method == "POST":
        content = request.POST["content"]
        user = User.objects.get(pk=request.user.id)
        # Add info to Post model
        post = Post(
            content = content,
            name = user
        )
        post.save()
        return HttpResponseRedirect(reverse(index))


def profile(request, id):
    user = User.objects.get(pk=id)
    # Get all posts from particular user in descending order to display latest post on topmost
    allpost = Post.objects.filter(name=user).order_by("id").reverse()
    # Create paginator of 10 objects for a single page
    paginator = Paginator(allpost, 10)
    page_number = request.GET.get("page")
    page_item = paginator.get_page(page_number)
    # Create following and followed count for user
    following = Follow.objects.filter(user=user)
    followed = Follow.objects.filter(user_followed=user)
    # Check if user currently making request is already a follower
    try:
        check_follow = followed.filter(user=User.objects.get(pk=request.user.id))
        # If filter result returns empty list means previously user was not a follower
        if len(check_follow) != 0:
            isfollowing = True
        else:
            isfollowing = False
    except:
        isfollowing = False
    # Get all liked posts
    allpost_like = Like.objects.all()
    # Check if user is logged in and update list of liked posts by respective user. Returns an empty list if user not logged in.
    userpost_like = []
    try:
        for like in allpost_like:
            if like.user.id == request.user.id:
                userpost_like.append(like.post.id)
    except:
        userpost_like = []
    return render(request, "network/profile.html", {
        "allpost": allpost,
        "pageitem": page_item,
        "username": user.username,
        "following": following,
        "followed": followed,
        "isfollowing": isfollowing,
        "currentuser": user,
        "userpost_like": userpost_like
    })


def follow(request):
    userfollow = request.POST["userfollow"]
    # Obtain info of login user and followed user
    login_user = User.objects.get(pk=request.user.id)
    userfollow_info = User.objects.get(username=userfollow)
    # Add both info to model
    newfollow = Follow(
        user = login_user,
        user_followed = userfollow_info,
    )
    newfollow.save()
    # Pass id info when redirect to profile page
    id = userfollow_info.id
    return HttpResponseRedirect(reverse(profile, args=(id, )))


def unfollow(request):
    userfollow = request.POST["userfollow"]
    # Obtain info of login user and followed user
    login_user = User.objects.get(pk=request.user.id)
    userfollow_info = User.objects.get(username=userfollow)
    # Get both info from model and delete
    newfollow = Follow.objects.get(
        user = login_user,
        user_followed = userfollow_info,
    )
    newfollow.delete()
    # Pass id info when redirect to profile page
    id = userfollow_info.id
    return HttpResponseRedirect(reverse(profile, args=(id, )))


def following(request):
    user = User.objects.get(pk=request.user.id)
    followlist = Follow.objects.filter(user=user)
    allpost = Post.objects.all().order_by("id").reverse()
    followpost = []
    for post in allpost:
        for follow in followlist:
            if post.name == follow.user_followed:
                followpost.append(post)
    # Create paginator of 10 objects for a single page
    paginator = Paginator(followpost, 10)
    page_number = request.GET.get("page")
    page_item = paginator.get_page(page_number)
    # Get all liked posts
    allpost_like = Like.objects.all()
    # Check if user is logged in and update list of liked posts by respective user. Returns an empty list if user not logged in.
    userpost_like = []
    try:
        for like in allpost_like:
            if like.user.id == request.user.id:
                userpost_like.append(like.post.id)
    except:
        userpost_like = []
    return render(request, "network/following.html", {
        "pageitem": page_item,
        "userpost_like": userpost_like
    })


def edit(request, post_id):
    if request.method == "POST":
        # Update the post-edit content into data
        post_data = json.loads(request.body)
        edit_post = Post.objects.get(pk=post_id)
        # Json content in JS is in dict form. Save content
        edit_post.content = post_data["content"]
        edit_post.save()
        return JsonResponse({"message": "Post updated successfully", "data": post_data["content"]})


def remove_like(request, post_id):
    post = Post.objects.get(pk=post_id)
    user = User.objects.get(pk=request.user.id)
    likedpost = Like.objects.filter(
        user = user,
        post = post,
    )
    likedpost.delete()
    return JsonResponse({"message": "Like removed"})


def add_like(request, post_id):
    post = Post.objects.get(pk=post_id)
    user = User.objects.get(pk=request.user.id)
    newlike = Like(
        user = user,
        post = post,
    )
    newlike.save()
    return JsonResponse({"message": "Like added"})
