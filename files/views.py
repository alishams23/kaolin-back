
from rest_framework import generics

from .models import File
from .serializers import FileSerializer
# Create your views here.




class FilesList(generics.ListAPIView):
  
    queryset = File.objects.all()
    serializer_class = FileSerializer
    

