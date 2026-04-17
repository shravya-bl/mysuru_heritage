from django.db import models

class Photo(models.Model):
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=255)
    place = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption