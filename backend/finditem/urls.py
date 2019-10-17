from django.urls import path

from .views import homepageview, keywordSearchView

urlpatterns = [
    path("", homepageview, name="home"),
    path("api/v1/", keywordSearchView, name="keywordSearchView"),
    ]
