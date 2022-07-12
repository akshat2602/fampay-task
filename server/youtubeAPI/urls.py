from rest_framework import routers
from django.urls import path, include

from . import views

router = routers.DefaultRouter()


router.register(r"", views.VideoViewSet, basename="video")

urlpatterns = [
    # path('list/video/', views.VideoViewSet.as_view(), name="list_youtube"),
    # path('search/video/', views.FilterYoutubeData.as_view() , name="search_youtube"),
    path("", include(router.urls)),
]
