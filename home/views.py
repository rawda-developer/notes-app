from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# from django.contrib.au <link rel="stylesheet" type="text/css" href="{% static './css/style.css' %}">th.decorators import login_required
# this is for class based views
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = 'smart/notes'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}

# delete if use class-based view
# def home(request):
#     return render(request, 'home/welcome.html', {'today': datetime.today()})


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'
# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})

# def home(request):
#     return HttpResponse('<h1>Hello, World!</h1>')
