from django.core.management.base import BaseCommand, CommandError
from allauth.account.models import EmailAddress
from django.contrib.auth.models import User
from avatar.models import Avatar
import urllib2
import json


class Command(BaseCommand):
    args = '<user_num ...>'
    help = 'Create new users based in http://randomuser.me/ API'

    def handle(self, *args, **options):
        user_num = args[0] if len(args) > 0 else 1
        response = urllib2.urlopen(
            "http://api.randomuser.me/?results=%s" % user_num)
        data = json.load(response)
        for u in data['results']:
            # Create user
            newUser = User()
            newUser.first_name = u['user']['name']['first']
            newUser.last_name = u['user']['name']['last']
            newUser.username = u['user']['username']
            newUser.email = '%s@mailinator.com ' % u['user']['username']
            newUser.set_password(u['user']['username'])
            newUser.save()

            # Validate email address
            EmailAddress.objects.create(user=newUser,
                                        email=newUser.email,
                                        primary=True,
                                        verified=True)

            # Add avatar to user
            image_url = u['user']['picture']
            import requests
            import tempfile
            from django.core import files

            # Steam the image from the url
            request = requests.get(image_url, stream=True)

            # Create a temporary file
            lf = tempfile.NamedTemporaryFile(
                suffix='.' + request.url.split('/')[-1].split('.')[-1],
                prefix=newUser.username)

            # import ipdb
            # ipdb.set_trace()

            # Read the streamed image in sections
            for block in request.iter_content(1024 * 8):

                # If no more file then stop
                if not block:
                    break

                # Write image block to temporary file
                lf.write(block)

            newAvatar = Avatar()
            newAvatar.avatar = files.File(lf)
            newAvatar.primary = True
            newAvatar.user = newUser
            newAvatar.save()

            self.stdout.write('New user created: %s.' % newUser)

        self.stdout.write('Successfully created %s new users.' % user_num)
