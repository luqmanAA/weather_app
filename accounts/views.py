from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import View
from django.shortcuts import get_object_or_404, redirect, render

from .models import User

# Create your views here.


class LoginView(View):
    page = 'login'

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')

        if request.user.is_authenticated:
            redirect('index')

        try:
            user = User.objects.get_object_or_404(email=email)
        except User.DoesNotExist:
            messages.error(f'A user with this email, {email} does not exist.')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            redirect('index')
        else:
            messages.error('Email or password is incorrect, please try again.')

        return render(request, 'accounts/login.html')

