from drf_yasg.utils import swagger_auto_schema
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class GetYoutubeData(APIView):

    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)