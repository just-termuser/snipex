from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("clicked", views.htmx_test),
    path("category/<int:category_id>/", views.categories, name="category_filter"),
]
