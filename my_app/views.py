from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import ProfileForm, PhotoForm
from .models import Photo, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('gallery')  

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            Profile.objects.get_or_create(user=user)
            
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})

@login_required
def gallery(request):
    photos = Photo.objects.all()
    return render(request, 'gallery.html', {'photos': photos})

@login_required
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None  
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')  
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'profile.html', {'form': form, 'profile': profile})

@login_required
def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user  
            photo.save()
            return redirect('gallery')  
    else:
        form = PhotoForm()
    
    return render(request, 'upload_photo.html', {'form': form})
