from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


class SignupPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("accounts:login")
    template_name = "registration/signup.html"


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            remember_me = form.cleaned_data["remember_me"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(10000)
                return redirect("core:index")
    else:
        form = LoginForm()

    return render(request, "registration/login.html", {"form": form})
