from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Address, PhoneNumber


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )


class CustomUserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "birth_date",
            "email",
            "profile_picture",
        ]


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False)


class AddressEditForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            "address_title",
            "address_line_1",
            "address_line_2",
            "city",
            "state",
            "postal_code",
            "country",
        ]


class PhoneNumberEditForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = [
            "phone_title",
            "number",
        ]
