from ast import Delete
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
import json
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from .models import User, Movies, Actors, Directors, Watchlist,Comment,Trend



#----------------------------------------------------------------------------------
def index(request):
    movies = Movies.objects.all().order_by('-result_rate')[:5]
    trend = Trend.objects.first()
    trend1 = Trend.objects.last()
    return render(request, "imdb/index.html",{
        "Movies":movies, "Trend": trend, "Trend1":trend1
    })
#----------------------------------------------------------------------------------
@csrf_exempt
def rate(request):
    if request.method == "POST":
        data = json.loads(request.body)
        id = data.get("id", "")
        rate = data.get("rate", "")
        if Movies.objects.filter(id = id, rate_user = request.user).exists():
            return JsonResponse({"E": "You have already rate"}, status=400)
        else:
            movie = Movies.objects.get(pk = id)
            movie.rate += rate
            movie.rate_num += 1
            #movie1 = Movies.objects.get(pk = id)
            x = movie.rate
            y = movie.rate_num
            movie.result_rate = x/y
            movie.save()
            user = User.objects.get(id = request.user.id)
            movie.rate_user.add(user)
    return render(request, "imdb/index.html")
#----------------------------------------------------------------------------------

def info_page(request,name):
    if Actors.objects.filter(name = name).exists():
        person = Actors.objects.get(name = name )
    else:
        person = Directors.objects.get(name = name)

    return render(request, "imdb/info_page.html",{
        "Person": person
    })

#----------------------------------------------------------------------------------

def movie_page(request,name):
    movie = Movies.objects.get(name = name)
    id = movie.id
    comments = Comment.objects.filter( movie = id)
    comments =  comments.order_by("-timestamp").all()
    if Watchlist.objects.filter(user = request.user , movie = id).exists():
        x =  1
    else : x = 0
    return render(request, "imdb/movie_page.html",{
        "Movie":movie, "Comments": comments, "x":x
    })
#----------------------------------------------------------------------------------
@csrf_exempt
def comment(request):
    data = json.loads(request.body)
    id = data.get("id", "")
    comment = data.get("comment", "")
    m = Movies.objects.get(id = id)
    c = Comment()
    c.user = request.user
    c.comment = comment
    c.movie = m
    c.save()
    return render(request, "imdb/index.html")

#----------------------------------------------------------------------------------
@csrf_exempt
def update_watchlist(request):
    if request.method == "POST":
        data = json.loads(request.body)
        id = data.get("id", "")
        if  Watchlist.objects.filter(user = request.user, movie = id ).exists():
            act = Watchlist.objects.get(user = request.user)
            attendee = Movies.objects.get(pk = id)
            act.movie.remove(attendee)
            return render(request, "imdb/index.html")
        else:
            item1 = get_object_or_404(Movies, pk = id)
            user_list, created = Watchlist.objects.get_or_create(user=request.user)
            user_list.movie.add(item1)
            #wach = Watchlist.objects.get(user = request.user)
            #wach1 = wach.item.all()
            return render(request, "imdb/index.html",{
            })
    return render(request, "imdb/index.html")
#----------------------------------------------------------------------------------

def watchlist(request):
    wach1 = Watchlist.objects.get(user = request.user)
    #wach1 = wach.movie.all().values()

    return render(request, 'imdb/watchlist.html',{
        "watchlist":wach1
    })  
#----------------------------------------------------------------------------------

def category(request,cate):
    if cate == "All":
        category = Movies.objects.all()
    else :
        category = Movies.objects.filter(gener = cate)
    return render(request, 'imdb/category.html',{
        "Movies":category, "Cate":cate
    }) 

#----------------------------------------------------------------------------------

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
            return render(request, "imdb/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "imdb/login.html")
#----------------------------------------------------------------------------------

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
#----------------------------------------------------------------------------------

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "imdb/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "imdb/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "imdb/register.html")
#----------------------------------------------------------------------------------