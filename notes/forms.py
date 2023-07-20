from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from notes.models import*


class PostForm(forms.ModelForm):
    pdf = forms.FileField(
        label=_('PDF'),
        help_text=_('PDF file type only.'),
        widget=forms.FileInput(attrs={'accept': 'application/pdf'})
    )

    class Meta:
        model = Post
        fields = ('img','title', 'desc')

