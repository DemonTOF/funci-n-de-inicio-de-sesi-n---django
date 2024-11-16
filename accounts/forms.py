# forms.py en accounts
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Asegúrate de que use el modelo CustomUser
        fields = ('username', 'email', 'age', 'password1', 'password2')  # Añade explícitamente los campos que necesitas

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'age',
        )

"""
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        #fields = UserCreationForm.Meta.fields + ('email', 'age')
        fields = ('username', 'email', 'age', 'password1', 'password2')  # Añade explícitamente los campos
"""