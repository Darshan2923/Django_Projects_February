from django import forms
from .models import *

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title','tag', 'content', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Blog'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content of the Blog'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('phone_no','bio','facebook','instagram','linkedin','image')
        widgets = {
            'phone_no': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Add Your Phone No. Here'}),
            'bio': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Add Your Bio Here'}),
            'facebook': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Add Your Facebook Profile Here'}),
            'instagram': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Add Your Instagram Profile Here'}),
            'linkedin': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Add Your Linkedin Profile Here'}),
        }