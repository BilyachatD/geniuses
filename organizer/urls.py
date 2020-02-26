from django.urls import path

from . import views

urlpatterns = [
    path("", views.MainChoiseView.as_view(), name = "main_page"),
]