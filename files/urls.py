from .views import FilesList
from django.urls import path

urlpatterns = [
    
    path('FilesList/',FilesList.as_view() ),
]
