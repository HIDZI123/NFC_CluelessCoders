from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("disease/<int:disease_id>", views.disease, name="disease"),
    path("disease/search/", views.disease_search, name="disease_search"),
]
