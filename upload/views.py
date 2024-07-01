from django.db.transaction import atomic
from rest_framework import viewsets, views, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from django.http import FileResponse
from django.db import models
from io import BytesIO

from .models import UploadFile

PARAM_KEY_NAME = 'name'


# Create your views here.
class UploadViewSet(viewsets.GenericViewSet):
    def post(self, request, format=None):
        return Response("upload 200")


class UploadView(views.APIView):
    def get(self, request, format=None):
        return Response("upload 200")

    def post(self, request, format=None):
        return Response("upload 200")


@atomic
def save_multiple_files(files):
    print(f"count before: {UploadFile.objects.count()}")
    for file in files:
        uf = UploadFile(name=file.name, content=file.read(), upload_date=timezone.now())
        uf.save()


class UploadFileView(APIView):
    """

    """

    def post(self, request):
        uploaded_files = list(request.data.values())
        save_multiple_files(uploaded_files)

        return Response(
            {"message": f"{len(uploaded_files)} files parsed at the App Server"},
            status=status.HTTP_200_OK,
        )
