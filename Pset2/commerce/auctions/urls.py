from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create_listing, name="create"),
    path("category", views.display_cat, name="category"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("removewatchlist/<int:id>", views.remove_watchlist, name="removewatchlist"),
    path("addwatchlist/<int:id>", views.add_watchlist, name="addwatchlist"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("addcomment/<int:id>", views.add_comment, name="addcomment"),
    path("addbid/<int:id>", views.add_bid, name="addbid"),
    path("closeauction/<int:id>", views.close_auction, name="closeauction")
]
