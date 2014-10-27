from django.contrib import admin
from .models import *
# from django.conf import settings


class PoemAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'author', 'book')

    # def image_display(self, poem):
    #     return '<img width="100" src="%s" />' % \
    #         (settings.MEDIA_URL + str(poem.image))

    # image_display.allow_tags = True

admin.site.register(Poem, PoemAdmin)
admin.site.register(Author)
admin.site.register(Book)
