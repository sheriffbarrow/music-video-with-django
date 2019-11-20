from django.urls import path
from . import views
from django.conf.urls import include, url
from .views import IndexView, DetailView, CreateAlbum
from music.models import Video

app_name = 'music'
urlpatterns = [

	path('', views.IndexView.as_view(), name='index_bulma'),
	path('watch/artist/<int:pk>/', views.DetailView.as_view(), name='detail_test'),
	#url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail_test'),
	#path(r'^(?P<pk>[0-9]+)/create_song/$',views.create_song, name='create_song'),
	#path('songs/<int:filter_by>/',views.songs, name='songs'),

	#path('<song_id>/favorite/', views.favorite, name='favorite'),
	#path('<album_id>/favorite_album/', views.favorite_album, name='favorite_album'),

	#path('create_album/', views.CreateAlbum.as_view(), name='create_album'),
	
	
	
]

