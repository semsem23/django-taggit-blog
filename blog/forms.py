from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title  = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'input[type=text]'}))
    content  = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':4,'cols':50}))
    tags  = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'input[type=text]', 'placeholder':'ex : "USA","Elon Musk"'}))
    
    class Meta:
        model = Post
        fields =['title', 'content', 'tags',]
