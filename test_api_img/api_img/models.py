from django.contrib.auth.models import User
from django.db import models


class Img(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    img = models.ImageField(upload_to='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
