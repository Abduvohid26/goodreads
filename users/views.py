from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin


from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .forms import UserCreateForm, UserLoginForm, ProfileUpdateForm
from django.contrib import messages


class RegisterView(View):
    template_name = 'users/register.html'

    def get(self, request):
        create_form = UserCreateForm()
        context = {
            "form": create_form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        create_form = UserCreateForm(data=request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect(reverse_lazy('users:login'))  # Use reverse_lazy for better URL handling
        else:
            context = {
                "form": create_form
            }
            return render(request, self.template_name, context)


class LoginView(View):
    def get(self, request):
        login_form = UserLoginForm()
        return render(request, 'users/login.html', {'login_form': login_form})

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('books:list')
        else:
            return render(request, 'users/login.html', {'login_form': login_form})


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.info(request, 'You have successfully logged out')
        return redirect('landing_page')


class Profile(LoginRequiredMixin, View):

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        return render(request, 'users/profile.html', {'user': request.user})


class ProfileEdit(LoginRequiredMixin, View):
    def get(self, request):
        user_update = ProfileUpdateForm(instance=request.user)
        return render(request, 'users/profile-edit.html', {'form': user_update})

    def post(self, request):
        user_update = ProfileUpdateForm(instance=request.user, data=request.POST, files=request.FILES)
        if user_update.is_valid():
            user_update.save()
            messages.success(request, 'You have successfully updated your profile ')

            return redirect('users:profile')

        return render(request, 'profile.html', {"form": user_update})

































