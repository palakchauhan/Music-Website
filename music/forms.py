from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
        'username', 
        'email', 
        'password',
        ]

    def clean_email(self,*args,**kwargs):
    	email=self.cleaned_data.get("email")
    	if not email.endswith("com"):
    		raise forms.ValidationError("Not a valid email")
    	return email