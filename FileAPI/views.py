from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import File
from .serializers import FileSerializer
from .tasks import process


# Create your views here.
class FileAPIView(ViewSet):
    serializer_class = FileSerializer

    def upload(self, request, *args, **kwargs):
        data = {
            'file': request.FILES.get('file')
        }
        serializer = FileSerializer(data=data)
        if serializer.is_valid():
            file = serializer.save()
            process.delay(file.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
