from django import forms

from .models import Merchandise

INPUT_CLASSES = 'col-sm-6 col-md-6 col-lg-4 col-xl-3 text-uppercase justify-content-center'
class NewMerchandiseForm(forms.ModelForm):
    class Meta:
        model = Merchandise
        fields = ('category', 'name', 'description', 'price', 'image',)
        widget = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
     