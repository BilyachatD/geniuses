from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.SimpleLoginView.as_view(), name = "login_page"),
    path("register/", views.RegisterUserView.as_view(), name = "register_page"),
    path("logout/", views.UserLogOut.as_view(), name = "logout_page"),
    path("test/", views.testView, name = "test_page"),
]
