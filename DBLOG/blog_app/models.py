from django.db import models


class ModelPost(models.Model):
    title = models.CharField('Заголовок записи', max_length=100, null=False)
    description = models.TextField(null=True)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    time_create = models.DateTimeField(auto_now=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

