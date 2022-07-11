import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters


from .models import Video
from .serializers import VideoSerializer


class GetYoutubeData(generics.ListAPIView):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["published_at"]
