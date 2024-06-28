from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import RegistrationForm, LoginForm, UserProfileForm
from django.contrib.auth import authenticate, login as auth_login, logout 
from django.contrib.auth.decorators import login_required
from .models import UserProfile



# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('profile')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('Home')
            else:
                form.add_error(None, 'Invalid email or password.')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def Home(request):
    return render(request, 'home.html')

@login_required
def myprofile(request):
    return render(request, 'profile.html')

@login_required
def profile_create_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile_detail')
    else:
        form = UserProfileForm()
    return render(request, 'profile/profile_form.html', {'form': form})

@login_required
def profile_update_view(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_detail')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'profile/profile_form.html', {'form': form})

@login_required
def profile_detail_view(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    print(profile)
    return render(request, 'profile/profile_detail.html', {'profile': profile})
