
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path("movie_page/<str:name>", views.movie_page, name="movie_page"),
    path("update/watchlist", views.update_watchlist, name="watchlist"),
    path("watchlist", views.watchlist, name="user-watchlist"),
    path("rate", views.rate, name="rate"),
    path("info/<str:name>", views.info_page, name="info_page"),
    path("comment", views.comment, name="comment"),
    path("category/<str:cate>", views.category, name="category"),
]
