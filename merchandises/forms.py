from django import forms

from .models import Merchandise

INPUT_CLASSES = 'col-sm-12 col-md-8 col-lg-6 col-xl-4'
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

class EditMerchandiseForm(forms.ModelForm):
    class Meta:
        model = Merchandise
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        widget = {

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
     