from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, StrictButton



class RegisterForm(forms.Form):
    user_name = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    password = forms.CharField()
    confirm_password = forms.CharField()

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_method = 'post'
    helper.form_action = '/registered'
    # helper.add_input(Submit('save_changes', 'Save changes', css_class='btn btn-primary'))
    helper.layout = Layout(
                            Field('user_name', css_class='form-control'),
                            Field('email', css_class='form-control'),
                            Field('password', css_class='form-control'),
                            Field('confirm_password', css_class='form-control'),
                            FormActions(
                                        Submit('save_changes', 'Save changes', css_class='btn btn-primary'),
                                        Submit('cancel', 'Cancel'),
                                       )
                          )
    

    # if forms.is_valis
# class LoginForm(forms.Form):