from django.urls import path

from . import views

urlpatterns = [
    path('video/', views.GetYoutubeData.as_view(), name="list_youtube"),
    path('video/filter/', views.FilterYoutubeData.as_view() , name="filter_youtube"),
]