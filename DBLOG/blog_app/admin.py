from django.contrib import admin
from .models import ModelPost


@admin.register(ModelPost)
class MPAdmin(admin.ModelAdmin):
    list_display = ('title', )
