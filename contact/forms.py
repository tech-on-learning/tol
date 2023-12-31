from django import forms

# Importing Models
from .models import Message, Student, Teacher

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


#-----------------#
#  Student FORM  #
#-----------------#
class StudentForm(forms.ModelForm):
    required_css_class = 'required'
    error_css_class = 'err'
    class Meta:
        model = Student
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'cf_form_group_field_input',})
        self.fields['last_name'].widget.attrs.update({'class': 'cf_form_group_field_input',})
        self.fields['email'].widget.attrs.update({'class': 'cf_form_group_field_input',})
        self.fields['course'].widget.attrs.update({'class': 'cf_form_group_field_input select',})
        self.fields['set_schedule'].widget.attrs.update({'class': 'cf_form_group_field_input select',})
        self.fields['q_laptop'].widget.attrs.update({'class': 'cf_form_group_field_input select',})
        self.fields['q_wish'].widget.attrs.update({'class': 'cf_form_group_field_input select',})
        self.fields['q_hearing_us'].widget.attrs.update({'class': 'cf_form_group_field_input select',})
        self.fields['q_certificate'].widget.attrs.update({'class': 'cf_form_group_field_input select',})
        self.fields['q_price'].widget.attrs.update({'class': 'cf_form_group_field_input select',})
        self.fields['message'].widget.attrs.update({'class': 'cf_form_group_field_input msg','cols':'30','rows':'6',})

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

    def clean_message(self):
        message = self.cleaned_data.get("message")
        if len(message) <= 3:
            raise forms.ValidationError("Your message is too short")
        return message


#-----------------#
#  Teacher FORM  #
#-----------------#
class TeacherForm(forms.ModelForm):
    required_css_class = 'required'
    error_css_class = 'err'
    class Meta:
        model = Teacher
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'cf_form_group_field_input',})
        self.fields['last_name'].widget.attrs.update({'class': 'cf_form_group_field_input',})
        self.fields['email'].widget.attrs.update({'class': 'cf_form_group_field_input',})
        self.fields['set_education_level'].widget.attrs.update({'class': 'cf_form_group_field_input select',})
        self.fields['course'].widget.attrs.update({'class': 'cf_form_group_field_input','placeholder':'e.g. Graphic design, Coding, Data analysis, Marketing...',})
        self.fields['message'].widget.attrs.update({'class': 'cf_form_group_field_input msg','cols':'30','rows':'6',})

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

    def clean_message(self):
        message = self.cleaned_data.get("message")
        if len(message) <= 3:
            raise forms.ValidationError("Your message is too short")
        return message