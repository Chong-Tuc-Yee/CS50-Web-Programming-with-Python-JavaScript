from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    category_name = models.CharField(max_length = 64)

    # Define a function to rename each categories created instead of display categories as cat. obj 1, 2 etc.
    def __str__(self):
        return f"{self.category_name}"


class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="bidder")
    # Default 0 if user did not enter any bidding price
    bidprice = models.FloatField(default = 0)

    def __str__(self):
        return f"{self.bidprice}"


# Create model for auction listings
# Watchlist model is many-to-many field as one listing items can be on multiple user's watchlist and each user can have multiple listing items on their watchlist
class Listing(models.Model):
    title = models.CharField(max_length = 64)
    description = models.CharField(max_length = 300)
    img_url = models.URLField(max_length = 1000)
    price = models.ForeignKey(Bid, on_delete=models.CASCADE, blank=True, null=True, related_name = "price")
    status_act = models.BooleanField(default = True)
    name = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name = "owner")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name = "category")
    watchlist = models.ManyToManyField(User, blank=True, null=True, related_name = "watchlist")

    # Define a function to rename each listings created.
    def __str__(self):
        return f"{self.title}"


class Comments(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name= "commenter")
    commentlisting = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True, related_name= "commentlisting")
    message = models.CharField(max_length = 300)

    def __str__(self):
        return f"{self.commenter} comment on {self.commentlisting}"
