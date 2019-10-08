from django.urls import path

from .views import homepageview, devview

urlpatterns = [path("", homepageview, name="home"), path("dev/", devview, name="dev")]
