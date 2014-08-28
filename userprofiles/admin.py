from django.contrib import admin
from django.contrib.auth.models import User
from django.conf import settings
from avatar.util import get_primary_avatar


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email',
                    'first_name', 'last_name', 'is_staff', 'avatar_display')
    list_filter = ('is_staff', 'is_superuser')

    def avatar_display(self, user):
        avatar = get_primary_avatar(user)
        try:
            if avatar and avatar.avatar:
                return '<img width="100" src="%s" />' % \
                    (settings.MEDIA_URL + str(avatar.avatar))
            else:
                return 'No Avatar'
        except Exception, e:
            raise
        else:
            pass
        finally:
            pass

    avatar_display.allow_tags = True


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# from avatar.models import Avatar
# from avatar.util import get_user_model
# from django.utils.translation import ugettext_lazy as _
# from avatar.signals import avatar_updated
# from avatar.templatetags.avatar_tags import avatar


# class AvatarAdmin(admin.ModelAdmin):
#     list_display = ('get_avatar', 'user', 'primary', "date_uploaded")
#     list_filter = ('primary',)
#     search_fields = ('user__%s' %
#                      getattr(get_user_model(), 'USERNAME_FIELD', 'username'),)
#     list_per_page = 50

#     def get_avatar(self, avatar_in):
#         return avatar(avatar_in.user, 80)

#     get_avatar.short_description = _('Avatar')
#     get_avatar.allow_tags = True

#     def save_model(self, request, obj, form, change):
#         super(AvatarAdmin, self).save_model(request, obj, form, change)
#         avatar_updated.send(sender=Avatar, user=request.user, avatar=obj)

# admin.site.unregister(Avatar)
# admin.site.register(Avatar, AvatarAdmin)
