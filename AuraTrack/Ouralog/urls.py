from django.urls import path
from . import views

urlpatterns =[
    path("receive/", views.receive_vitals, name="receive_vitals"),
]