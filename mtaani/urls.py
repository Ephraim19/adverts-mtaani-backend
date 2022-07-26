from django.urls import path
from . views import UploadToYoutube

urlpatterns = [
    path("upload/",UploadToYoutube.as_view()),
]