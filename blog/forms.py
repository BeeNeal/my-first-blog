from django import forms
from .models import Post

# tell django that PostForm is a ModelForm (django class)
class PostForm(forms.ModelForm):
    # with Meta, tell django which model should be used to create the form
    class Meta:
        model = Post
        fields = ('title', 'text',)