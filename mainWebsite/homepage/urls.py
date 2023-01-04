from django.contrib import admin
from django.urls import path, include
from .views import HomepageView

app_name = "homepage"

urlpatterns = [
    path("", HomepageView.as_view(), name="homepage"),
]