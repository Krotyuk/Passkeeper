from django import forms

from .models import accessPost

class accessForm(forms.ModelForm):

    class Meta:
        model = accessPost
        fields = ('title', 'comment')