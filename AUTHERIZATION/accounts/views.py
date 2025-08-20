from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render, redirect
from .forms import RoleUserCreationForm


# class RegisterView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('dashboard')
#         form = UserCreationForm()
#         return render(request, 'accounts/register.html', {'form': form})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('dashboard')
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('dashboard')
#         return render(request, 'accounts/register.html', {'form': form})
class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        form = RoleUserCreationForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        form = RoleUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            role = form.cleaned_data.get('role')

            # Set role flags
            if role == 'manager':
                user.is_staff = True
                user.is_superuser = True
            else:  # customer
                user.is_staff = False
                user.is_superuser = False

            user.save()
            login(request, user)
            return redirect('dashboard')
        return render(request, 'accounts/register.html', {'form': form})


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        return render(request, 'accounts/login.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
    

class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        if user.is_superuser:
            role = "Manager"
        elif user.is_staff:
            role = "Owner"
        else:
            role = "Customer"
        return render(request, 'accounts/dashboard.html', {'role': role})


# class DashboardView(LoginRequiredMixin, View):
#     def get(self, request):
#         user = request.user
#         if user.is_staff:
#             role = "Owner"
#         else:
#             role = "Customer"
#         return render(request, 'accounts/dashboard.html', {'role': role})

