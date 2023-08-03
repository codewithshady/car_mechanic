from django import forms
from .models import Career,Enquiry

class TestimonialForm(forms.Form):
    name = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':"form-control text-dark"}))
    designation = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':"form-control text-dark"}))
    message = forms.CharField(label='please share your thoughts',widget=forms.Textarea(attrs={'class':"form-control"}))

class CareerForm(forms.ModelForm):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control text-dark"}))
    email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'class': "form-control text-dark"}))
    phone_number = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': "form-control text-dark"}))
    message = forms.CharField(label='say something',
                              widget=forms.Textarea(attrs={'class': "form-control"}))
    class Meta:
        model = Career
        fields = ('name', 'email', 'phone_number', 'resume', 'message')


class contactForm(forms.ModelForm):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control text-dark"}))
    email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'class': "form-control text-dark"}))
    phone_no = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': "form-control text-dark"}))
    message = forms.CharField(label='please share your thoughts',
                              widget=forms.Textarea(attrs={'class': "form-control"}))

    class Meta:
        model = Enquiry
        fields = ('name', 'email', 'phone_no','message')



