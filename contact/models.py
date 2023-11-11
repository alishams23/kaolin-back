from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(verbose_name='نام', max_length=30)
    last_name = models.CharField(verbose_name='نام خانواگی', max_length=30)
    email = models.EmailField(verbose_name='ایمیل', blank=True)

    def __str__(self):
        return self.first_name
    
