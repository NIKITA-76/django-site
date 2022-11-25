from django.db import models


class ModelPost(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=100, null=False)
    description = models.TextField(null=True, verbose_name='DESCRIPTION', )
    link = models.TextField(null=True, verbose_name='LINK', )
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='PHOTO', blank=True)
    time_create = models.DateTimeField(auto_now=True, verbose_name='TIME CREATE', )
    time_update = models.DateTimeField(auto_now=True, verbose_name='TIME UPDATE', )
    is_published = models.BooleanField(default=False, verbose_name='IS PUBL', )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['time_create']
