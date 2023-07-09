from django import forms

# Importing Models
from .models import Message

#-----------------#
#  Messages FORM  #
#-----------------#
class MessageForm(forms.ModelForm):
    required_css_class = 'required'
    error_css_class = 'err'
    class Meta:
        model = Message
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control','placeholder':'First Name','id':'name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control','placeholder':'Last Name','id':'name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control','placeholder':'Email Address','id':'email'})
        self.fields['subject'].widget.attrs.update({'class': 'form-control','placeholder':'Subject','id':'subject'})
        self.fields['message'].widget.attrs.update({'class': 'form-control','placeholder':'Your message','cols':'30','rows':'6','id':'message'})

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if len(first_name) <= 1:
            raise forms.ValidationError("Your first name is too short")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if len(last_name) <= 1:
            raise forms.ValidationError("Your last name is too short")
        return last_name

    def clean_subject(self):
        subject = self.cleaned_data.get("subject")
        if len(subject) <= 1:
            raise forms.ValidationError("Your subject is too short")
        return subject

    def clean_message(self):
        message = self.cleaned_data.get("message")
        if len(message) <= 3:
            raise forms.ValidationError("Your message is too short")
        return message