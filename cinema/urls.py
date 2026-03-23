from django.urls import path

from cinema.views import movie_list, movie_detail


app_name = "cinema"

urlpatterns = [
    path("movies/", movie_list, name="movie_list"),
    path("movies/<int:pk>/", movie_detail, name="movie_detail"),
    path("movies/create", movie_list, name="movie_create"),
    path("movies/update/<int:pk>/", movie_detail, name="movie_update"),
    path("movies/delete/<int:pk>/", movie_detail, name="movie_delete"),

]