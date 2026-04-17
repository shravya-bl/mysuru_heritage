from django.db import models
from django.contrib.auth.models import User


class Place(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='places/')
    description = models.TextField()

    CATEGORY_CHOICES = [
        ('palace', 'Palace'),
        ('temple', 'Temple'),
        ('museum', 'Museum'),
        ('nature', 'Nature'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='palace')

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.place.name}"