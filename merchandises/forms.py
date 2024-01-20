from django import forms

from .models import Merchandise


class NewMerchandiseForm(forms.ModelForm):
    class Meta:
        model = Merchandise
        fields = ('category', 'name', 'description', 'price', 'image',)
        # widget = {
            #'category': forms.Select(attrs{
                #'class': 'kolla bootstrap'
            #})
        #}
     