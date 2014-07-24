from django.contrib import admin
from .models import Poem


class PoemAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Poem, PoemAdmin)
