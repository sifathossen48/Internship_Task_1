from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from website.models import NewsLetter, ContactUs, Subscribe, ErrorEmail, Comment


class NewsLetterForm(ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'
class ErrorEmailForm(ModelForm):
    class Meta:
        model = ErrorEmail
        fields = '__all__'
class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'

class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=32)

class LatestNewsSearchForm(forms.Form):
    name = forms.CharField(required=False)
    category = forms.CharField(required=False)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'comment')