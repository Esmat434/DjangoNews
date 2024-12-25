from django import forms
from django_countries.fields import CountryField
from .models import CustomUser
from datetime import date

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100,required=True,help_text='Please Enter Your Username',
                               widget=forms.TextInput(attrs={
                               'type':'text',
                               'class':'form-control'
                           }),label='Username',error_messages={'required':'Enter Your User Name'})
    email = forms.EmailField(required=True,help_text='Please Enter Your Email',
                             widget=forms.EmailInput(attrs={
                               'type':'email',
                               'class':'form-control'
                           }),label='Email',error_messages={'required':'Enter Your Email Address'})
    first_name = forms.CharField(max_length=100,required=False,help_text='Enter Your First Name',
                                 widget=forms.TextInput(attrs={
                               'type':'text',
                               'class':'form-control'
                           }),label='First Name')
    last_name = forms.CharField(max_length=100,required=False,help_text='Enter Your Last Name',
                                widget=forms.TextInput(attrs={
                               'type':'text',
                               'class':'form-control'
                           }),label='Last Name')

    password = forms.CharField(max_length=18,min_length=8,required=True,
                            help_text='Your Password Must be 8 degits.',
                        error_messages={'required':'Your Password Must be contain on Uppercase letter One Number and One digits'},
                        widget=forms.PasswordInput(attrs={
                               'type':'password',
                               'class':'form-control'
                           }),label='Password')
    phone_number = forms.CharField(max_length=15,required=True,help_text='Enter Your Number With country Code.',
                                   error_messages={'required':'Your Phone Number Must be contain Contry Code.'},
                                   widget=forms.TextInput(attrs={
                                        'type':'text',
                                        'class':'form-control'
                                    }),label='Phone Number')
    country = CountryField().formfield(
        widget = forms.Select(attrs={
            'class':'form-control'
        }),label='Country',required=True,error_messages = {'required':'Your Must Choose Your Country.'}
    )
    city = forms.CharField(max_length=100,required=True,help_text='Enter Your City',
                           error_messages={"required":'Your City is Required.'},widget=forms.TextInput(attrs={
                               'type':'text',
                               'class':'form-control'
                           }),label='Country')
    birth_date = forms.DateField(required=True,widget=forms.DateInput(attrs={
                                'type':'date',
                                'class':'form-control'
                            }),label='Birth Date',help_text='Your Age Must be 18',
                            error_messages={'required':'Your Age Must be between 18 and 100'})
    def clean_birth_date(self):
        birth_date = self.cleaned_data.get('birth_date')  # از get استفاده کنید تا None برگرداند اگر مقدار موجود نباشد
        if not birth_date:
            raise forms.ValidationError("Please provide a valid birth date.")

        today = date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        if age < 18 or age > 100:
            raise forms.ValidationError("Your age must be between 18 and 100.")
        return birth_date

    def clean_username(self):
        username = self.cleaned_data['username']
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("This Username is Already Taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This Email Already Taken.")
        return email
