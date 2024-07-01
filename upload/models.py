from django.db import models

MB = 1_000_000


# Create your models here.
class UploadFile(models.Model):
    name = models.CharField(max_length=1024)
    content = models.BinaryField(max_length=1 * MB)
    upload_date = models.DateTimeField("date uploaded")

    def __str__(self):
        return self.name
