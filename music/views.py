from django.http import Http404
from django.views import generic
from .models import Video, Audio
from django.urls import reverse
from django.urls import resolve
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import  AudioForm, UserForm
from django.http import JsonResponse
from django.views.generic import View
from .forms import UserForm
from django.utils import timezone
from music.models import Audio

from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
AUDIO_FILE_TYPES = [ 'wav', 'mp3', 'ogg', 'mp4']
IMAGE = ['png', 'jpg', 'jpeg']
VIDEO_FILE_TYPE = ['mp4']


class IndexView(generic.ListView):
	template_name = 'music/index_bulma.html'
	context_object_name = 'all_videos'
	
	def get_queryset(self):
		return Video.objects.all()

			
class DetailView(generic.DetailView):
	model = Video
	template_name = 'music/detail_test.html'

	def get_context_data(self, **kwargs):
		context = super(DetailView, self).get_context_data(**kwargs)
		#Add 10 LandingPages to your context
		context['video_list'] = Video.objects.all()[:10]
		return context
	


class CreateAlbum(generic.CreateView):
	model = Video
	fields = ['artist', 'video_title', 'video_genre', 'video_logo']

	def from_valid(self, form):
		object = form.save(commit=False)
		object.user = self.request.user
		object.save()
		return super(CreateAlbum, self).form_valid(form)


def create_song(request, video_id):
	form = SongForm(request.POST or None, request.FILES or None)
	video = get_object_or_404(Video, pk=video_id)
	if form.is_valid():
		video_songs = video.audio_set.all()
		for s in video_songs:
			if s.song_title == form.cleaned_data.get("song_title"):
				context = {
					'video': video,
					'form': form,
					'error_message':'You already added that song',
				}
				return render(request, 'music/create_song.html', context)
		song = form.save(commit=False)
		song.video = video
		song.audio_file = request.FILES['audio_file']
		file_type = song.audio_file.url.split('.')[-1]
		file_type = file_type.lower()
		if file_type not in AUDIO_FILE_TYPES:
			context = {
				'video': video,
				'form': form,
				'error_message': ' Audio file must be WAV, MP3, or OGG',
			}
			return render(request, 'music/create_song.html', context)
			song.save()
			return render(request, 'music/detail.html', {'video': video})
		context = {
			'video': video,
			'form': form,
		}
		return render(request, 'music/create_song.html', context)

def delete_album(LoginRequiredMixin,request, album_id):
	video = Video.objects.get(pk=album_id)
	video.delete()
	videos = Video.objects.filter(user=request.user)
	return render(request, 'music/index.html', {'videos': videos})


def delete_song(request, album_id, song_id):
	album = get_object_or_404(Album, pk=album_id)
	song = Song.objects.get(pk=song_id)
	song.delete()
	return render(request, 'music/detail.html', {'album': album})


def favorite(request, song_id):
	song = get_object_or_404(Audio, pk=song_id)
	try:
		if song.is_favorite:
			song.is_favorite = False
		else:
			song.is_favorite = True
		song.save()
	except (KeyError, Song.DoesNotExist):
		return JsonResponse({'success': False})
	else:
		return JsonResponse({'success': True})


def favorite_album(request, video_id):
	video = get_object_or_404(Video, pk=video_id)
	try:
		if video.is_favorite:
			video.is_favorite = False
		else:
			video.is_favorite = True
		video.save()
	except (KeyError, Video.DoesNotExist):
		return JsonResponse({'success': False})
	else:
		return JsonResponse({'success': True})



def songs(request, filter_by):
	
		try:
			song_ids = []
			for album in Album.objects.filter(user=request.user):
				for song in album.song_set.all():
					song_ids.append(song.pk)
			users_songs = Song.objects.filter(pk__in=song_ids)
			if filter_by == 'favorites':
				users_songs = users_songs.filter(is_favorite=True)
		except Album.DoesNotExist:
			users_songs = []
		return render(request, 'music/songs.html', {
			'song_list': users_songs,
			'filter_by': filter_by,
		})

class UserFormView(View):
	form_class = UserForm
	template_name = 'music/registration_form.html'

	# display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			# creates form object without saving it to
			# database storing it locally
			user = form.save(commit=False)

			# cleaned normalized data (properly formatted)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			# returns User object if credentials are correct
			user = authenticate(username=username, password=password)

			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('music:index')
		render(request,self.template_name,{'form': form})

		