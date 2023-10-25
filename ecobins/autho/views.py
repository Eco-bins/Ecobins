from django.shortcuts import render, redirect

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django. contrib import messages
from django.urls import reverse
from .models import *

# Create your views here.
@csrf_exempt
def loginPage(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            try:
                profile = User.objects.get(user=user)
                return redirect(reverse('user-home'))
            except User.DoesNotExist:
                return redirect(reverse('health-profile'))
        else:
            messages.info(request, 'Password or Username is incorrect')
            return render(request, 'login.html')

    return render(request, 'login.html')
