from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import View, CreateView, FormView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

from .models import User
from .forms import UserRegisterForm

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
            messages.error(request, f'A user with this email, {email} does not exist.')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            redirect('index')
        else:
            messages.error(request, 'Email or password is incorrect, please try again.')

        return render(request, 'accounts/login.html')


class UserRegisterView(FormView):
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data['email']
        password = form.cleaned_data['password2']
        user = authenticate(email=email, password=password)
        login(self.request, user)
        return super(UserRegisterView, self).form_valid(form)




