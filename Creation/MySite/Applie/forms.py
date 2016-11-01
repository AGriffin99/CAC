from django.contrib.auth.models import User
from django import forms
from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.layout import *
# from crispy_forms.bootstrap import PrependedText, PrependedAppendedText, FormActions
from crispy_forms.bootstrap import *

class UserSignupForm(forms.ModelForm):
    password= forms.CharField(max_length=32, widget=forms.PasswordInput)
    class Meta:
        model= User
        fields =['first_name','last_name','username','password']
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        super(UserSignupForm, self).__init__(*args, **kwargs)
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-inline'
        self.helper.add_input(Submit('submit', 'Submit'))
        super(UserLoginForm, self).__init__(*args, **kwargs)
