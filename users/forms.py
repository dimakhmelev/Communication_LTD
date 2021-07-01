from django import forms
from django.contrib.auth.models import User
from .models import Profile, Customer
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

DATA_PLAN_CHOICES = (
    ("1", "Ultimate  100$/m"),
    ("2", "Regular 50$/m"),
    ("3", "Free 0$/m"),
)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    phone = forms.IntegerField()
    data_plan = forms.ChoiceField(choices=DATA_PLAN_CHOICES)

    class Meta:
        model = Profile
        fields = ['phone', 'data_plan']


class CustomerCreateForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['Name', 'Email', 'Phone']
