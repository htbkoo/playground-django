from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("file/", views.UploadFileView.as_view(), name="upload_file"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
