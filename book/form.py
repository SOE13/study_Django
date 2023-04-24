from django import forms

class UserFrom(forms.Form):
    user_name=forms.CharField(label='User Name',max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label='Password',max_length=16,widget=forms.PasswordInput(attrs={'class':'form-control'}))