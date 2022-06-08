from django import forms
from blog.models import Post, Comment
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ( 'title', 'text')
        # adding widgets
        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }
        

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        #fields = ('author', 'text')
        fields =('text',)
        widgets = {
            #'author': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }

class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    email = forms.CharField(widget=forms.EmailInput)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
  
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if password1 != password2:
            raise forms.ValidationError("Your passwords do not match")
        return password2

