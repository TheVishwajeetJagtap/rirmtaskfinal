from django.db import models
from phone_field import PhoneField
# Create your models here.
class UserInfo(models.Model):
    name=models.CharField(max_length=15)
    url=models.URLField(max_length=400)
    phone=PhoneField(null=False,blank=False,unique=True)

    def __str__(self):
        return self.name
