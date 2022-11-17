from django.db import models


class ModelPost(models.Model):
    author = models.CharField('Автор записи', max_length=100, null="dsf")
    title = models.CharField('Заголовок записи', max_length=500, null="dsf")

    def __str__(self):
        return self.title

