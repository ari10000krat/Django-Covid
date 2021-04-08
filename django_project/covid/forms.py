from .models import Article
from django.forms import ModelForm, TextInput,DateTimeInput,Textarea


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['first_name', 'last_name', 'username', 'city', 'state', 'zip','date', 'comment']

        widgets = {
            'first_name':TextInput(attrs={
                'class':'form-control',
                'placeholder':'First Name',
                'width':'60%',

            }),
            'last_name':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Last Name'
            }),
            'username':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Username'
            }),
            'city':TextInput(attrs={
                'class':'form-control',
                'placeholder':'City'
            }),
            'state':TextInput(attrs={
                'class':'form-control',
                'placeholder':'State'
            }),
            'zip':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Zip'
            }),
            'date':DateTimeInput(attrs={
                'class':'form-control',
                'placeholder':'Date'

            }),
            'comment':Textarea(attrs={
                'class':'form-control',
                'placeholder':'Comment'
            }),            
        }