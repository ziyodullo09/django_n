from django.urls import path
from .views import home, andijon, namangan, buxoro, toshkent



urlpatterns = [
    path("", home),
    path("and/", andijon),
    path("nam/", namangan),
    path("bux/", buxoro),
    path("tosh/", toshkent)
]