from django import forms

class Forum_Form(forms.Form):
    error_messages = {
        'required': 'please fill this out...',
    }

    title_attrs = {
        'type': 'text',
        'class': 'form-control',
        'placeholder':'Title here...'
    }

    post_attrs = {
        'type': 'text',
        'cols': 50,
        'rows': 4,
        'class': 'form-control',
        'placeholder':'What jobs do you have? ...'
    }

    title = forms.CharField(label='', required=True, max_length=27, widget=forms.TextInput(attrs=title_attrs))
    post = forms.CharField(label='', required=True, widget=forms.Textarea(attrs=post_attrs))