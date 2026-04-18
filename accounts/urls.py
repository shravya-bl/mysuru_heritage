from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('home/', views.home_page, name='home'),
    path('logout/', views.user_logout, name='logout'),
    path('blog/', include('blog.urls')),
]
