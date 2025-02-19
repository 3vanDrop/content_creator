from resources.media_join import video_audio_join, video_join
from resources.buscar_clips import VideoDownloader

#Esta es una prueba de video join
def test_video_join():
    video_downloader = VideoDownloader(debug=True)  # Activar mensajes de depuración en la consola
    videos = video_downloader.query(name="food", count=5)
    video_join(*videos)
