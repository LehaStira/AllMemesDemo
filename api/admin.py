from django.contrib import admin
from .models import Meme, Tag
# Register your models here.


@admin.register(Meme)
class MemeAdmin(admin.ModelAdmin):
    list_display = ['picture', 'published']
    list_filter = ['published']
    search_fields = ['picture']


admin.site.register(Tag)
