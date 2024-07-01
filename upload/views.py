from io import BytesIO

from django.db.transaction import atomic
from django.http import FileResponse
from django.utils import timezone
from rest_framework import viewsets, views, status
from rest_framework.response import Response
from rest_framework.views import APIView

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

    def get(self, request):
        params = request.query_params
        if PARAM_KEY_NAME not in params:
            return Response(
                {"message": "Required <name> query parameter"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        name = params[PARAM_KEY_NAME]

        try:

            file = UploadFile.objects.get(name=name)
            return FileResponse(
                BytesIO(file.content),
                filename=file.name,
                status=status.HTTP_200_OK,
                as_attachment=True,
            )
        except UploadFile.DoesNotExist as e:
            return Response({"message": f"File <{name}> not found"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        uploaded_files = list(request.data.values())
        save_multiple_files(uploaded_files)

        return Response(
            {"message": f"{len(uploaded_files)} files parsed at the App Server"},
            status=status.HTTP_200_OK,
        )
