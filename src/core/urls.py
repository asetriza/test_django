from django.urls import path

from . import views

urlpatterns = [
    path("", views.flights, name="flights"),
    path("flight/", views.flight, name="flight"),
]