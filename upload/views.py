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
    if request.method == 'GET':
        return Response({"message": "Unsupported"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    if request.method == 'POST':
        data = request.data
        return Response({"message": f"{len(data)} files parsed at the App Server"}, status=status.HTTP_200_OK)

    return Response({"message": "Unsupported"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
