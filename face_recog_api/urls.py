from django.urls import path
from .views import *

urlpatterns = [
    path("enrollment_img/", enrollment_img),
    path("analy_img/", analy_img)
]