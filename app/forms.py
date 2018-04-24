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
    helper.form_class = 'form-group'
    helper.layout = Layout(
                            Field('username', css_class='form-control'),
                            Field('email', css_class='form-control'),
                            Field('password', css_class='form-control'),
                            Field('confirm_password', css_class='form-control'),
                            FormActions(
                                        Submit('save_changes', 'Save changes', css_class='btn btn-primary'),
                                        Submit('cancel', 'Cancel'),
                                       )
                          )
# class LoginForm(forms.Form):