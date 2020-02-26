from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from .forms import AuthUserForm, RegisterUserForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def testView(request):
    return HttpResponse('Работает')

# Авторизация пользователя
class SimpleLoginView(LoginView):
    template_name = "authorization/login.html"
    form_class = AuthUserForm 
    succes_url = reverse_lazy("main_page") 
    #Переопределение метода для переадресации после выполнения
    def get_success_url(self):
        return self.succes_url

# Регистрация
class RegisterUserView(CreateView):
    model = User
    template_name = "authorization/register.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy('main_page') 
    success_msg = "Пользователь успешно создан"
    #Автоматический вход в систему, если регистрация прошла успешно
    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        auth_user = authenticate(username=username, password=password)
        login(self.request, auth_user)
        return form_valid

# Выход из учетной записи
class UserLogOut(LogoutView):
    next_page = "login_page"