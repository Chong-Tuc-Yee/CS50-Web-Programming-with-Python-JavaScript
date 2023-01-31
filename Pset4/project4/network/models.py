from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="owner")
    content = models.CharField(max_length = 200)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post {self.id} made by {self.name} on {self.datetime.strftime('%d %b %Y %H:%M:%S')}"

class Follow(models.Model):
    # User that follows other people
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user_follower")
    # Same user that is being followed by others
    user_followed = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user_followed")

    def __str__(self):
        return f"{self.user} is following {self.user_followed}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user_like")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True, related_name="post_like")

    def __str__(self):
        return f"{self.user} liked {self.post}"
