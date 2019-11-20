from django.db import models
from django.conf import settings
from django.urls import reverse



# Create your models here.


class Video(models.Model): 
    artist = models.CharField(max_length=250)  
    video_file = models.FileField(upload_to='videos', max_length=500)
    video_title = models.CharField(max_length=500)
    video_genre = models.CharField(max_length=100)
 

    def get_absolute_url(self):
        return reverse('music:detail_test', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.video_title 


class Audio(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=500)
    audio_file = models.FileField(default='audios')
    file_type = models.CharField(max_length=10)
    
    
    def __str__(self):
        return reverse('music:detail_test', kwargs={'pk': self.pk})


    def __str__(self):
        return self.file_type

	
