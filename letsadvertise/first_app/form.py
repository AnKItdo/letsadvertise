from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class registerForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']






class SMSForm(forms.Form):
    from_ = forms.CharField()
    message = forms.CharField(widget = forms.Textarea)
    to = forms.CharField()

# class EMAILForm(forms.Form):
#     From_= forms.CharField()
#     Mail = forms.CharField(widget = forms.Textarea)
#     To = forms.CharField()





class EMAILForm(forms.Form):
    from_ = forms.CharField()
    message = forms.CharField(widget = forms.Textarea)
    to = forms.CharField()
    #









class GMAILForm(forms.Form):
    from_ = forms.CharField()
    message = forms.CharField(widget = forms.Textarea)
    to = forms.CharField()




# class EMAILForm(forms.ModelForm):
#
#     class Meta:
#         model = Email
#         fields = ('FROM', 'MAIL','TO')
