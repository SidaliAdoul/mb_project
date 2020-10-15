from django.urls import path

from .views import HomePageView
from .models import Post

urlpatterns = [
    path("", HomePageView.as_view(model=Post), name="home"),
]