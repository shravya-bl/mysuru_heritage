from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(blank=True, null=True)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


# Create your models here.
