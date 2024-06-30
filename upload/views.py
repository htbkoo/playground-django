from rest_framework import viewsets, views, status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
class UploadViewSet(viewsets.GenericViewSet):
    def post(self, request, format=None):
        return Response("upload 200")


class UploadView(views.APIView):
    def get(self, request, format=None):
        return Response("upload 200")

    def post(self, request, format=None):
        return Response("upload 200")


@api_view(['GET', 'POST'])
def upload_file(request):
    return Response("Not implemented yet", status=status.HTTP_501_NOT_IMPLEMENTED)
