from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import render
from user.models import CustomUser
from django.http import HttpResponseRedirect


class UserRegistrationView(View):
    def get(self, request):
        return render(request, 'signup.html')
    
    def post(self, request):
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        # number = request.POST.get('number')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        confirmation = request.POST.get('confirmation')
        
        if confirmation != 'on':
            return render(request, 'signup.html', {'error_message': 'Please agree to the terms and conditions'})
        
        if password != confirm_password:
            return render(request, 'signup.html', {'error_message': 'Passwords do not match'})
        
        # Check if username or email already exists
        if CustomUser.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error_message': 'Email already exists'})
        
        # Create new user
        user = CustomUser.objects.create_user( 
            email=email,
            first_name=first_name,
            last_name=last_name
            )
        user.set_password(password)
        user.save()
        
        return redirect('login')  # Redirect to login page after successful registration


class UserLoginView(View):
    def get(self, request):
        return render(request, 'signin.html')
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            if request.session.get("booking_in_progress"):
                del request.session["booking_in_progress"]
                return redirect('seat_selection')
            
            return redirect('home')  # Redirect to dashboard after successful login
        else:
            return render(request, 'signin.html', {'error_message': 'Invalid username or password'})


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')