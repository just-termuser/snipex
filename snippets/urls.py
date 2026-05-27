from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("category/<str:category_name>/", views.categories, name="category_filter"),
]
