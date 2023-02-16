from django import forms
from nursery.models import ContactUs, UserDetails, Blogs
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from ckeditor.fields import RichTextField


class WriteBlogForm(forms.ModelForm):
    Plant_Essentials = RichTextField()
    Common_Problems = RichTextField()
    Style_and_Decor = RichTextField()

    class Meta:
        model = Blogs
        fields = ('Plant_Essentials', 'Common_Problems', 'Style_and_Decor')


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('Full_Name', 'Email', 'Mobile', 'Message')
        labels = {'Full_Name': 'Full Name', 'Email': 'Email', 'Mobile': 'Mobile', 'Message': 'Message'}


class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = "__all__"
        exclude = ['user']


class RegistrationForm(UserCreationForm):
    password2 = forms.CharField(required=True, label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {'email': 'Email', 'username': 'Username'}


class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = "__all__"
        exclude = ['user']


class AdminProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = '__all__'
        labels = {'email': 'Email'}
