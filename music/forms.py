from django import forms
from django.contrib.auth.models import User

from .models import Video, Audio


class VideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ['artist', 'video_title', 'video_file']


class AudioForm(forms.ModelForm):

    class Meta:
        model = Audio
        fields = ['song_title', 'audio_file']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']