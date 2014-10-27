from django.forms import ModelForm, Textarea
from .models import *


class PoemForm(ModelForm):
    class Meta:
        model = Poem
        fields = ['title', 'body', 'author', 'book']
        widgets = {
            'body': Textarea(attrs={'wrap': 'hard'}),
        }
