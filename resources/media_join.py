"""This library has been created using DeepSeek"""
import ffmpeg
import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.VideoClip import TextClip
import pysrt

def video_join(*videos, output_resolution="1280x720"):
    # Crear una lista de inputs para ffmpeg
    inputs = [ffmpeg.input(video) for video in videos]
    
    # Escalar todos los videos a la misma resolución
    scaled_videos = []
    for input_video in inputs:
        scaled_video = input_video.filter('scale', output_resolution)
        scaled_videos.append(scaled_video)
    
    # Concatenar los videos escalados
    concatenated = ffmpeg.concat(*scaled_videos, v=1, a=0)
    
    # Guardar el video resultante
    output_path = "output_joined.mp4"
    concatenated.output(output_path).run()
    
    return output_path

def video_audio_join(*media, output_resolution="1280x720"):
    # Separar videos y audios
    videos = [m for m in media if m.endswith(('.mp4', '.avi', '.mov'))]
    audios = [m for m in media if m.endswith(('.mp3', '.wav', '.aac'))]
    
    # Crear una lista de inputs para ffmpeg
    video_inputs = [ffmpeg.input(video) for video in videos]
    audio_inputs = [ffmpeg.input(audio) for audio in audios]
    
    # Escalar todos los videos a la misma resolución
    scaled_videos = []
    for input_video in video_inputs:
        scaled_video = input_video.filter('scale', output_resolution)
        scaled_videos.append(scaled_video)
    
    # Concatenar los videos escalados
    concatenated_video = ffmpeg.concat(*scaled_videos, v=1, a=0)
    
    # Concatenar los audios
    concatenated_audio = ffmpeg.concat(*audio_inputs, v=0, a=1)
    
    # Combinar video y audio
    output_path = "output_with_audio.mp4"
    ffmpeg.output(concatenated_video, concatenated_audio, output_path).run()
    
    return output_path

def video_join_subs(video_input_path, srt_input_path, output_video):
    # Cargar el video
    video = VideoFileClip(video_input_path)
    
    # Cargar los subtítulos desde el archivo SRT
    subs = pysrt.open(srt_input_path)
    
    # Convertir los subtítulos a un formato que moviepy pueda entender
    def generator(txt):
        return TextClip(
            txt, 
            font='Courier',  # Especifica la fuente aquí
            fontsize=24, 
            color='white', 
            bg_color='black', 
            size=video.size
        )
    
    # Crear el clip de subtítulos
    subtitles = SubtitlesClip(srt_input_path, generator)
    
    # Ajustar los subtítulos al video
    subtitles = subtitles.set_position(('center', 'bottom'))
    
    # Combinar el video con los subtítulos
    final_video = CompositeVideoClip([video, subtitles])
    
    # Guardar el video final
    final_video.write_videofile(output_video, codec='libx264')
    
    # Retornar el path absoluto del video guardado
    return os.path.abspath(output_video)


if __name__ == "__main__":
    from resources.buscar_clips import VideoDownloader

    video_downloader = VideoDownloader(debug=True)  # Activar mensajes de depuración en la consola
    videos = video_downloader.query(name="food", count=2)
    video_join(*videos)