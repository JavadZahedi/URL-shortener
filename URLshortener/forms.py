from django import forms
from .models import URL

class URLForm(forms.ModelForm):
    shortened_url = forms.URLField(label='نشانی کوتاه شده', required=False)

    class Meta:
        model = URL
        fields = ['label', 'address']
