from django.db import models
from django.conf import settings
from datetime import datetime

# Create your models here.
class MyImage(models.Model):
    title = models.CharField(max_length=30)
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title
