from django import forms

from .models import Merchandise

# INPUT_CLASSES = 'bootstrap class'
class NewMerchandiseForm(forms.ModelForm):
    class Meta:
        model = Merchandise
        fields = ('category', 'name', 'description', 'price', 'image',)
        # widget = {
            #'category': forms.Select(attrs{
                #'class': 'kolla bootstrap' INPUT_CLASSES 
            #}),
            #'name': forms.TextInput(attrs{
                #'class': 'kolla bootstrap' INPUT_CLASSES 
            #}),
            #'description': forms.Textarea(attrs{
                #'class': 'kolla bootstrap' INPUT_CLASSES 
            #}),
            #'price': forms.TextInput(attrs{
                #'class': 'kolla bootstrap' INPUT_CLASSES 
            #}),
            #'image': forms.FileInput(attrs{
                #'class': 'kolla bootstrap' INPUT_CLASSES 
            #}),
        #}
     