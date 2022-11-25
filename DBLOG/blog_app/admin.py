from django.contrib import admin
from .models import ModelPost


class ModelPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published',)
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'content',)
    list_editable = ('is_published',)
    list_filter = ('is_published',)


admin.site.register(ModelPost, ModelPostAdmin)
