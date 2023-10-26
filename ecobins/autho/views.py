from django.shortcuts import render, redirect

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django. contrib import messages
from django.urls import reverse
from .models import *

from django.contrib.auth.forms import PasswordChangeForm

@csrf_exempt
def loginPage(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            try:
                profile = Userauth.objects.get(user=user)
                return redirect(reverse('user-home'))
            except Userauth.DoesNotExist:
                return redirect(reverse('health-profile'))
        else:
            messages.info(request, 'Password or Username is incorrect')
            return render(request, 'login.html')

    return render(request, 'login.html')

def reset_password(request):
    return render(request,'reset_password.html')

def update_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            # Clean the form data, including the old_password field
            form.clean()
            user = form.save()
            # Important: update the user's session to avoid logging them out
            update_session_auth_hash(request, user)
            # Show a success message
            messages.success(request, 'Password updated successfully.')
            # Redirect to the home page or any other URL you prefer
            return redirect('home')
        else:
            print(form.errors)
            messages.error(request, 'Password update failed. Please correct the errors.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'update_password.html', {'form': form})