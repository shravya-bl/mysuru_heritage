from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Photo

@login_required
def gallery_view(request):
    photos = Photo.objects.all().order_by('-uploaded_at')
    return render(request, "gallery/gallery.html", {"photos": photos})

@login_required
def upload_photo(request):
    if request.method == "POST":
        image = request.FILES.get('image')
        caption = request.POST.get('caption')
        place = request.POST.get('place')

        Photo.objects.create(
            image=image,
            caption=caption,
            place=place
        )

        return render(request, "gallery/upload_photo.html", {
            "message": "Photo uploaded successfully!"
        })

    return render(request, "gallery/upload_photo.html")