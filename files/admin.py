from django.contrib import admin
from .models import *
# Register your models here.


class FileAdmin(admin.ModelAdmin):
    list_display = ( "id", )


admin.site.register(File, FileAdmin)