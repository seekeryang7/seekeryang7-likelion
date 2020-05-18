from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_in_view, name="index_html"),
    path('new', views.new_in_view, name="new_html"),
    path('detail/<int:primary_articles>', views.detail_in_view, name="detail_html"),
    path('drama', views.drama_in_view, name="drama_html"),
    path('movie', views.movie_in_view, name="movie_html"),
    path('entertain', views.entertain_in_view, name="entertain_html"),
]
