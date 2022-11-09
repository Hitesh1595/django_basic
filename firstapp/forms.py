from django import forms
# use inbuilt django validators for fields
from django.core import validators

# custom validator using validators called
# def check_for_z_in_name(value):
#     # test case
#     # name must start with z other wise raise error
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("name start with z")

class FormName(forms.Form):
    # name = forms.CharField(max_length = 160,validators = [check_for_z_in_name])
    name = forms.CharField(max_length = 160)
    # name1 = forms.CharField(max_length = 160,required = False)
    email = forms.EmailField()
    verify_email = forms.EmailField(label = 'enter you email again')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required = False,widget = forms.HiddenInput,validators = [validators.MaxLengthValidator(0)])

    # this method use to clean data at once
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']

        if vemail != email:
            raise forms.ValidationError("email not match")










    # botcatcher is used to make out site safe from bots to detect whether human submit form or bots
    # define function  name with    clean_fieldname      to define a function

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']

    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("gotcha bot")

    #     return botcatcher