from django import forms
from .models import Author, Friend, UserProfile


class AuthorForm(forms.ModelForm):

    full_name = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Author
        fields = '__all__'


class FriendForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Friend
        fields = '__all__'


class ProfileCreationForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = [
            'age',
            'phone'
        ]
