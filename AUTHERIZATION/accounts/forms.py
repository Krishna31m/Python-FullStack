from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RoleUserCreationForm(UserCreationForm):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('manager', 'Manager'),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True, widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'role']
