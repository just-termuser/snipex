from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("clicked", views.htmx_test),
    path("category/<int:category_id>/", views.categories, name="category_filter"),
    path("add/", views.add_snippet, name="add_snippet"),
    path("favorites/<int:snippet_id>/", views.toggle_favorite, name="toggle_favorite"),
    path("favorites/", views.favorites, name="favorites"),
    path("search-users/", views.search_users, name="search_users"),
    path("user/<str:username>/", views.user_profile, name="user_profile"),
    path("<int:snippet_id>/", views.snippet_detail, name="snippet_detail"),
]
