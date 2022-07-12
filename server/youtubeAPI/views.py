from rest_framework import viewsets, status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Video
from .serializers import VideoSerializer


class VideoViewSet(viewsets.ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()

    @swagger_auto_schema(responses={200: VideoSerializer(many=True)})
    @action(detail=False, methods=["get"], url_path="list/video", url_name="list_videos")
    def list_videos(self, request):
        """Request to list all the videos"""
        if request.query_params.get("ordering") == "published_at":
            videos = Video.objects.order_by("published_at")
        else:
            videos = Video.objects.all().order_by("-published_at")

        if videos.exists():
            page = self.paginate_queryset(videos)
            if page is not None:
                serialized = VideoSerializer(page, many=True)
                return self.get_paginated_response(serialized.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={200: VideoSerializer(many=True)})
    @action(detail=False, methods=["get"], url_path="search/video", url_name="search_videos")
    def search_videos(self, request):
        """Request to search for videos"""
        search_query = request.query_params.get("search")
        if search_query:
            search_terms = search_query.split(" ")
            videos = Video.objects.none()
            for term in search_terms:
                temp_search_title = Video.objects.filter(title__icontains=term)
                temp_search_description = Video.objects.filter(
                    description__icontains=term)
                videos = videos | temp_search_title | temp_search_description
                videos = videos.union(temp_search_title).union(
                    temp_search_description)

            videos = videos.order_by("-published_at")
            page = self.paginate_queryset(videos)
            if page is not None:
                serialized = VideoSerializer(page, many=True)
                return self.get_paginated_response(serialized.data)
            return Response(status=status.HTTP_404_NOT_FOUND)

        videos = Video.objects.all().order_by("-published_at")
        page = self.paginate_queryset(videos)
        if page is not None:
            serialized = VideoSerializer(page, many=True)
            return self.get_paginated_response(serialized.data)
        return Response(status=status.HTTP_404_NOT_FOUND)


# class GetYoutubeData(generics.ListAPIView):
#     serializer_class = VideoSerializer
#     queryset = Video.objects.all()
#     filter_backends = [filters.OrderingFilter]
#     ordering_fields = ["published_at"]


# class FilterYoutubeData(generics.ListAPIView):
#     queryset = Video.objects.all()
#     serializer_class = VideoSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['title', 'description']
