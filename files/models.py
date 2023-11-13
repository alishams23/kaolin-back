from django.db import models

# Create your models here.
from django.db import models
import os


def file_upload_path(instance, filename):
    # Generate folder name based on the date
    
    
    # Combine folder name with the filename
    return os.path.join('media/files', filename)

class File(models.Model):
    title = models.CharField(max_length=800,verbose_name="عنوان")
    tds = models.FileField(verbose_name="فایل",upload_to=file_upload_path)
    usage = models.TextField()
    
    
    class Meta:
        verbose_name = "فایل"
        verbose_name_plural = "فایل ها"
