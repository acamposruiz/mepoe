from django.forms import ModelForm, Textarea
from .models import *


class PoemForm(ModelForm):
    class Meta:
        model = Poem
        fields = ['title', 'body']
        widgets = {
            'body': Textarea(attrs={'wrap': 'hard'}),
        }
