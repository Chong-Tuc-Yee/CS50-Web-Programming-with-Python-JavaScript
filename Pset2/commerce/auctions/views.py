from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from .models import User, Category, Listing, Comments, Bid


def index(request):
    # Display all active listings on index page
    active_listing = Listing.objects.filter(status_act = True)
    categories = Category.objects.all()
    all_option = Category.objects.get(category_name = "All")
    return render(request, "auctions/index.html", {
        "listings": active_listing,
        "categories": categories,
        "all_option": all_option
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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create_listing(request):
    if request.method == "GET":
        # Send name data from category in models to select options in HTML
        categories = Category.objects.all().exclude(category_name = "All")
        return render(request, "auctions/create.html", {
            "categories": categories
        })
    else:
        # If request method is POST, obtain data from form and create a new listing object and add it into database
        title = request.POST["title"]
        description = request.POST["description"]
        img_url = request.POST["url"]
        price = request.POST["price"]
        category = request.POST["category"]
        # Get all data from the particular category chosen. category_name in Category class equals to category form
        category_item = Category.objects.get(category_name=category)
        # Use request.user since only allow people logged in to access this function
        current_user = request.user
        # Create a new bid object using price input from user
        bid = Bid(
            bidprice = float(price),
            bidder = current_user
        )
        bid.save()
        new_entry = Listing(
            title = title,
            description = description,
            img_url = img_url,
            price = bid,
            name = current_user,
            category = category_item
        )
        new_entry.save()
        # Redirect to index page
        return HttpResponseRedirect(reverse(index))


def display_cat(request):
    # Display all active listings on the specified category user chooses
    if request.method == "POST":
        usr_category = request.POST['category']
        if usr_category == "All":
            return HttpResponseRedirect(reverse(index))
        else:
            category = Category.objects.get(category_name = usr_category)
            active_listing = Listing.objects.filter(status_act = True, category = category)
            categories = Category.objects.all()
            return render(request, "auctions/category.html", {
                "listings": active_listing,
                "category": category,
                "categories": categories
            })


def listing(request, id):
    # Display listings/details for each items
    item_listing = Listing.objects.get(pk = id)
    # Check if user is already in watchlist, returns Boolean values
    item_in_watchlist = request.user in item_listing.watchlist.all()
    # Filter to get only listing of particular item
    item_comments = Comments.objects.filter(commentlisting = item_listing)
    datetime = timezone.now()
    # Check if user is the one who created the listing (For closing auction)
    usr_create = request.user.username == item_listing.name.username
    return render(request, "auctions/listing.html", {
        "item_listing": item_listing,
        "item_in_watchlist": item_in_watchlist,
        "item_comments": item_comments,
        "datetime": datetime,
        "usr_create": usr_create
    })


def remove_watchlist(request, id):
    # Remove item from watchlist for current user
    newitem_listing = Listing.objects.get(pk = id)
    current_usr = request.user
    newitem_listing.watchlist.remove(current_usr)
    # Pass in argument to get the listing of particular object back
    return HttpResponseRedirect(reverse(listing, args=(id, )))


def add_watchlist(request, id):
    # Add new item to watchlist for current user
    newitem_listing = Listing.objects.get(pk = id)
    current_usr = request.user
    newitem_listing.watchlist.add(current_usr)
    # Pass in argument to get the listing of particular object back
    return HttpResponseRedirect(reverse(listing, args=(id, )))


def watchlist(request):
    # Add a display page for the watchlist
    current_usr = request.user
    list_watchlist = Listing.objects.filter(watchlist = current_usr) # Alternative: current_usr.watchlist.all()
    return render(request, "auctions/watchlist.html", {
        "listings": list_watchlist
    })


def add_comment(request, id):
    # Enable logged in users to add comment on listing page item
    current_usr = request.user
    item_listing = Listing.objects.get(pk = id)
    message = request.POST["comment"]
    # Add info to Comments model
    newcomment = Comments(
        commenter = current_usr,
        commentlisting = item_listing,
        message = message
    )
    newcomment.save()
    return HttpResponseRedirect(reverse(listing, args=(id, )))


def add_bid(request, id):
    # Add a new bid
    newbid = request.POST["bid"]
    item_listing = Listing.objects.get(pk = id)
    # Check if user is already in watchlist, returns Boolean values
    item_in_watchlist = request.user in item_listing.watchlist.all()
    # Filter to get only listing of particular item
    item_comments = Comments.objects.filter(commentlisting = item_listing)
    # Check if user is the one who created the listing (For closing auction)
    usr_create = request.user.username == item_listing.name.username
    # New bidding price must be larger than previous bidding price and initial set price
    if float(newbid) > item_listing.price.bidprice:
        # Update Bid model with new bid info
        updatebid = Bid(bidprice = float(newbid), bidder = request.user)
        updatebid.save()
        # Update listing price with new bid info
        item_listing.price = updatebid
        item_listing.save()
        return render(request, "auctions/listing.html", {
            "item_listing": item_listing,
            "message": "Bid updated sucessfully.",
            "update": True,
            "item_in_watchlist": item_in_watchlist,
            "item_comments": item_comments,
            "usr_create": usr_create
        })
    else:
        return render(request, "auctions/listing.html", {
            "item_listing": item_listing,
            "message": "Bid update failed.",
            "update": False,
            "item_in_watchlist": item_in_watchlist,
            "item_comments": item_comments,
            "usr_create": usr_create
        })


def close_auction(request, id):
    # Enable logged in user who created the auction listing to close the auction
    item_listing = Listing.objects.get(pk = id)
    # Change the status of the listing to false
    item_listing.status_act = False
    item_listing.save()
    # Check if user is the one who created the listing (For closing auction)
    usr_create = request.user.username == item_listing.name.username
    # Filter to get only listing of particular item
    item_comments = Comments.objects.filter(commentlisting = item_listing)
    # Check if user is the one who created the listing (For closing auction)
    usr_create = request.user.username == item_listing.name.username
    return render(request, "auctions/listing.html", {
        "item_listing": item_listing,
        "item_in_watchlist": item_in_watchlist,
        "item_comments": item_comments,
        "datetime": datetime,
        "usr_create": usr_create,
        "update": True,
        "message": "Your auction is closed.",
        "item_comments": item_comments,
        "usr_create": usr_create
    })
