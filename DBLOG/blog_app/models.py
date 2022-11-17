from django.db import models


class ModelPost(models.Model):
    title = models.CharField

    def __str__(self):
        return self.title
