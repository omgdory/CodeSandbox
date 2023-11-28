from django.urls import path
from . import views # import views file

urlpatterns = [
    # empty first arg -- go to base url
    path("", views.home, name="home")
]
