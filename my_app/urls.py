from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('upload/', views.upload_photo, name='upload_photo'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),  
    path('gallery/', views.gallery, name='gallery'),
]
