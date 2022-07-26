from rest_framework import permissions
from rest_framework.views import APIView
from .serializers import FileSerializer
from rest_framework.response import Response
from rest_framework import status

class UploadToYoutube(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


