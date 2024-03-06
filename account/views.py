from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth import get_user_model, authenticate, login

from .forms import SignUpForm, LogInForm

User = get_user_model()


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'account/signup.html'
    success_url = '/'


def login_view(request):
    form = LogInForm
    if request.method == "POST":
        phone = request.POST['phone']
        password = request.POST['password']
        user = authenticate(request, phone=phone, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('app:home'))

    return render(request, 'account/login.html', {'form': form})
