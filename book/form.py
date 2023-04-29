from django import forms
from . import models

class UserFrom(forms.Form):
    user_name=forms.CharField(label='User Name',max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label='Password',max_length=16,widget=forms.PasswordInput(attrs={'class':'form-control'}))


class WriterForm(forms.ModelForm):
    class Meta:
        model =models.Writer
        exclude = ["age"]
        labels = {
            "first_name": ("Writer frist Name"),
        }
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'birthday':forms.DateInput(attrs={'class': 'form-control','type':'date'})
        }
        help_texts = {
            "first_name": ("First name can't be dulicated."),
        }
        error_messages = {
            "first_name": {
                "max_length": ("This writer's name is too long."),
                "unique": ("This writer's Already exited."),
            },
        }
        
        
class BookForm(forms.ModelForm):
    class Meta:
        model= models.Book
        fields=['name','writer']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'writer':forms.Select(attrs={'class':'form-select'}),
        }

class FavForm(forms.ModelForm):
    class Meta:
        model=models.FavBookCollection
        fields='__all__'
        widgets={
            'collect_name':forms.TextInput(attrs={'class':'form-control col-6'}),
            'books':forms.SelectMultiple(attrs={'class':'form-select col-6'}),
        }