from rest_framework import generics, filters


from .models import Video
from .serializers import VideoSerializer


class GetYoutubeData(generics.ListAPIView):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["published_at"]


class FilterYoutubeData(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']