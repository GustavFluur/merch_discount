from django import forms 

from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        field = ('content', )
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'add a class here from bootstrap'
        
            })
        }
