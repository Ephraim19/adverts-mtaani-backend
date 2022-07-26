from operator import mod
from django.db import models

class FileId(models.Model):
    file_id = models.CharField(max_length=100)
