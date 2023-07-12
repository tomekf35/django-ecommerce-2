from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib.auth.views import PasswordChangeDoneView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import (
    CustomUserCreationForm,
    CustomUserEditForm,
    LoginForm,
    AddressEditForm,
    PhoneNumberEditForm,
)
from .models import CustomUser


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


@login_required
def user_profile_view(request, username):
    user = get_object_or_404(CustomUser, username=username)
    addres_list = user.addresses.all()
    phone_list = user.phone_numbers.all()
    return render(
        request,
        "user/profile.html",
        {"user": user, "addres_list": addres_list, "phone_list": phone_list},
    )


@login_required
def user_edit_personal_view(request, username):
    user = get_object_or_404(CustomUser, username=username)

    if request.method == "POST":
        form = CustomUserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("accounts:user_profile", username=username)
    else:
        form = CustomUserEditForm(instance=user)

    return render(request, "user/edit_personal.html", {"form": form})


@login_required
def user_edit_address_view(request, username):
    user = get_object_or_404(CustomUser, username=username)
    addres_list = user.addresses.all()
    return render(request, "user/edit_address.html", {"addres_list": addres_list})


@login_required
def user_edit_address_form_view(request, username, address_id):
    user = get_object_or_404(CustomUser, username=username)
    address = user.addresses.get(id=address_id)

    if request.method == "POST":
        form = AddressEditForm(request.POST, instance=address)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = user
            address.save()
            return redirect("accounts:user_edit_address", username=username)
    else:
        form = AddressEditForm(instance=address)

    return render(
        request, "user/edit_address_form.html", {"address": address, "form": form}
    )


@login_required
def user_edit_phone_view(request, username):
    user = get_object_or_404(CustomUser, username=username)
    phone_list = user.phone_numbers.all()
    return render(request, "user/edit_phone.html", {"phone_list": phone_list})


@login_required
def user_edit_phone_form_view(request, username, phone_id):
    user = get_object_or_404(CustomUser, username=username)
    phone = user.phone_numbers.get(id=phone_id)

    if request.method == "POST":
        form = PhoneNumberEditForm(request.POST, instance=phone)
        if form.is_valid():
            phone = form.save(commit=False)
            phone.user = user
            phone.save()
            return redirect("accounts:user_edit_phone", username=username)
    else:
        form = PhoneNumberEditForm(instance=phone)

    return render(request, "user/edit_phone_form.html", {"phone": phone, "form": form})
