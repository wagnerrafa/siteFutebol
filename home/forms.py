from django import forms
from cloudinary_example.core.models import Post

class ImagensForm(forms.ModelForm):
    class Meta:
        model = Post