from django.urls import path

from . import views

urlpatterns = [
    path("", views.Excels.as_view()),
]
