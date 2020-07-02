from django.db import models


class Developer(models.Model):
    user_id = models.IntegerField()
    project_id = models.IntegerField()
