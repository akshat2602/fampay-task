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


class VideoFilterSet(django_filters.FilterSet):
    class Meta:
        model = Video
        fields = {
            'title': ['contains'],
            'description': ['contains'],
        }

class FilterYoutubeData(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = VideoFilterSet