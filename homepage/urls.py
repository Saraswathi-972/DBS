from django.urls import path
from .views import home, HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]

