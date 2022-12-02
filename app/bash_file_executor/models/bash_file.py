from django.db import models
from django.utils import timezone


class BashFile(models.Model):
    file = models.FileField(upload_to='bash_file')
    uploaded_datetime = models.DateTimeField(blank=True, default=timezone.now)

    def __str__(self):
        return '{}'.format(self.file.name)
