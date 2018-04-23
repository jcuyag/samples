from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions



class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField()
    confirm_password = forms.CharField()


    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
                            Field('username', css_class='input-xlarge'),
                            Field('email', css_class='input-xlarge'),
                            Field('password', css_class='input-xlarge'),
                            Field('confirm_password', css_class='input-xlarge'),
                            FormActions(
                                        Submit('save_changes', 'Save changes', css_class='btn-primary'),
                                        Submit('cancel', 'Cancel'),
                                       )
                          )
# class LoginForm(forms.Form):