from django.db import models

# Create your models here.

class ImageDataFiles(models.Model):
    sku = models.CharField(max_length=30)
    image_status = models.CharField(max_length=5)
    image_file = models.ImageField(upload_to="Images")

class FindAndReplaceFiles(models.Model):
    filename = models.CharField(max_length=50)
    excel_file = models.FileField(upload_to="ExcelSheets")