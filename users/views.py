from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .forms import *


# Create your views here.
def logout_view(request):
    logout(request)
    redirect('users:user_login_view')


class UserLoginView(View):
    template_name = 'login.html'

    def get(self, request):
        form = UserLoginForm()
        context = {
            'form': form,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = UserLoginForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active():
                    login(self.request, user)

                    context = {'form': form}
                    return render(request, self.template_name, context)
                else:
                    messages.error(request, 'Username or Password is incorrect')
        else:
            form = UserLoginForm()

        context = {
            'form': form,
            }

        return render(request, self.template_name, context)


