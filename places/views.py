from django.shortcuts import render, redirect
from .models import Place, Review


# -------------------- PLACES LIST PAGE (WITH SEARCH + FILTER) --------------------
def places_list(request):

    places = [
        {
            "name": "Mysore Palace",
            "image": "place/palace.jpg"
        },
        {
            "name": "Chamundi Hills",
            "image": "place/temple.jpg"
        },
        {
            "name": "Brindavan Gardens",
            "image": "place/bg.jpg"
        },
        {
            "name": "Lalitha Mahal",
            "image": "place/lalitha.jpg"
        },
        {
            "name": "St. Philomena Church",
            "image": "place/church.jpg"
        },
        {
            "name": "Mysuru Zoo",
            "image": "place/zoo.jpg"
        },
    ]

    return render(request, 'places.html', {"places": places})


# -------------------- PLACE OPTIONS PAGE --------------------
def place_options(request):
    place_name = request.GET.get("place", "Selected Place")
    return render(request, 'place_options.html', {"place": place_name})


# -------------------- ROUTE PAGE --------------------
def route_page(request):
    place_name = request.GET.get("place", "Selected Place")

    if request.method == "POST":
        source = request.POST.get("source")
        destination = place_name

        maps_url = f"https://www.google.com/maps/dir/?api=1&origin={source}&destination={destination}"

        return render(request, "route_page.html", {
            "place": place_name,
            "maps_url": maps_url,
            "source": source
        })

    return render(request, "route_page.html", {"place": place_name})


# -------------------- PLACE INFO PAGE --------------------
def place_info(request):
    place_name = request.GET.get('place')

    place = Place.objects.get(name=place_name)   # ✅ FIXED

    info_data = {
        "Mysore Palace": {
            "history": "The Mysore Palace is the official residence of the Wadiyar dynasty.",
            "timings": "10:00 AM - 5:30 PM",
            "fee": "₹70 (Adults), ₹30 (Children)",
            "best_time": "Evening illumination",
            "facts": "Lights up with 97,000 bulbs!",
        },
        "Chamundi Hills": {
            "history": "Home to Chamundeshwari Temple.",
            "timings": "6:00 AM - 9:00 PM",
            "fee": "Free",
            "best_time": "Morning",
            "facts": "850 steps to top!",
        },
    }

    details = info_data.get(place_name, {})

    return render(request, "place_info.html", {
        "place": place,   # ✅ IMPORTANT FIX
        "details": details,
    })


# -------------------- ADD REVIEW --------------------
def add_review(request, place_id):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        place = Place.objects.get(id=place_id)

        Review.objects.create(
            user=request.user,
            place=place,
            rating=rating,
            comment=comment
        )

    return redirect(f'/places/info/?place={place.name}')


# -------------------- PLACES BETWEEN PAGE --------------------
def places_between(request):
    place_name = request.GET.get("place", "")

    data = {
        "Chamundi Hills": [
            {"name": "Nandi Statue", "image": "between/nandi.jpg", "desc": "Majestic statue"},
        ],
        "Mysore Palace": [
            {"name": "KR Circle", "image": "between/kr_circle.jpg", "desc": "Central landmark"},
        ],
    }

    places_list = data.get(place_name, [])

    return render(request, "between.html", {
        "place": place_name,
        "between_places": places_list
    })


# -------------------- LANDING PAGE --------------------
def landing_page(request):
    return render(request, "landing.html")