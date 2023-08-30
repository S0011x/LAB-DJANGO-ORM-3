from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('cafe', 'cafe'),
        ('lounge', 'lounge'),
        ('Food', 'Food'),
        ('New Experince', 'New Experince'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    publish_date = models.DateField()
    photo = models.ImageField(upload_to='post_photos/', null=True, blank=True)
    
    def __str__(self):
        return self.title
    


class Comment(models.Model):

    rating_choices = ((1, "1 Star"), (2, "2 Star"), (3, "3 Star"), (4, "4 Star"), (5, "5 Star"), )

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE ,default=1)
    content = models.TextField()
    rating = models.IntegerField(choices=rating_choices)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} on {self.post.title}"
    


class Favorate(models.Model):
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
