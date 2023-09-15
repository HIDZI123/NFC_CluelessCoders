from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("disease/<int:disease_id>", views.disease, name="disease"),
    path("bodypart/<int:part_id>", views.bodypart, name="body_part"),
    path("disease/search/", views.disease_search, name="disease_search"),
    path('quiz/', views.quiz_view, name='quiz'),
]
