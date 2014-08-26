from django.contrib import admin
from .models import Poem


class PoemAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'author', 'book')

admin.site.register(Poem, PoemAdmin)
