from django.db import models


class Checklist(models.Model):
    name = models.CharField(max_length=50)
    is_mandatory = models.BooleanField(default=True)
