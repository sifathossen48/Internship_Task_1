from django import forms
from django.forms import ModelForm

from website.models import NewsLetter, ContactUs, Subscribe


class NewsLetterForm(ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'

class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'

class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'