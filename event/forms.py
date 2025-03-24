
from django import forms
from django.contrib.auth.models import User


class Signupform(forms.ModelForm):


    class Meta:
        model = User
        fields = ['email', 'username' ,'first_name', 'last_name', 'password'] 
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Custom placeholders for each field
        placeholders = {
            'email': 'Email',
            'username': 'username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'password': 'Password',

        }
        
        # Customize each field
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                "class": "flex size-full text-white min-h-11 border border-border-primary bg-background-primary py-2 align-start file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-neutral focus-visible:outline-none disabled:cursor-not-allowed disabled:opacity-50 px-3",
                "placeholder": placeholders.get(field_name, ''),  # Set placeholder
            })
            field.label = ''

       
        self.fields['username'].help_text = ''
       


class SigninForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "flex size-full text-white min-h-11 border border-border-primary bg-background-primary py-2 align-start file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-neutral focus-visible:outline-none disabled:cursor-not-allowed disabled:opacity-50 px-3",
            'placeholder': 'Username',
            'id': 'username'
        }),
        label=''  # Explicitly set label to empty string
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "flex size-full text-white min-h-11 border border-border-primary bg-background-primary py-2 align-start file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-neutral focus-visible:outline-none disabled:cursor-not-allowed disabled:opacity-50 px-3",
            'placeholder': 'Password',
            'id': 'password'
        }),
        label=''  # Explicitly set label to empty string
    )




