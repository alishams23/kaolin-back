
from django.urls import  include, path,re_path
from .views import ContactApi
urlpatterns = [
     path('create/', ContactApi.as_view(),name="ContactApi"),
  
]
