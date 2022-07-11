from django.urls import path

from . import views

urlpatterns = [
    path('video/', views.GetYoutubeData.as_view(), name="search_youtube")
]