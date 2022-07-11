from django.urls import path

from . import views

urlpatterns = [
    path('list/video/', views.GetYoutubeData.as_view(), name="list_youtube"),
    path('search/video/', views.FilterYoutubeData.as_view() , name="search_youtube"),
]