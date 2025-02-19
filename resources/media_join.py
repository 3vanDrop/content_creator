"""This library has been created using DeepSeek"""
import ffmpeg
import os
import logging

from resources.utils import time_it

logger = logging.getLogger(__name__)

@time_it
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

@time_it
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
    logger.info(f"Video joined to audio successfully! - {output_path}")

    return output_path

@time_it
def video_join_subs(video_input_path, srt_input_path, output_video):
    # Configuración de los subtítulos
    subtitle_style = (
        "force_style="
        "FontName=Arial,"
        "FontSize=24,"  # Tamaño de la fuente
        "PrimaryColour=&H00FFFFFF,"  # Color del texto (blanco)
        "OutlineColour=&H00000000,"  # Color del borde (negro)
        "BackColour=&H80000000,"  # Color de fondo (transparente)
        "BorderStyle=3,"  # Estilo del borde
        "Outline=1,"  # Grosor del borde
        "Shadow=0,"  # Sin sombra
        "Alignment=2"  # Alineación (centrado abajo)
    )

    # Filtro para los subtítulos
    subtitle_filter = f"subtitles={srt_input_path}:force_style='{subtitle_style}'"

    # Filtro para el subrayado dinámico
    underline_filter = (
        "drawtext="
        "fontcolor=yellow:"
        "fontsize=24:"
        "fontfile=/System/Library/Fonts/Supplemental/Arial.ttf:"  # Ruta a la fuente Arial
        "text='':"
        "x=(w-tw)/2:"  # Centrar horizontalmente
        "y=h-th-10:"  # Posicionar cerca de la parte inferior
        "box=1:"  # Habilitar fondo
        "boxcolor=black@0.5:"  # Color del fondo (negro semitransparente)
        "boxborderw=5:"  # Grosor del borde
        "enable='between(t,0,10)'"  # Ejemplo: subrayado dinámico entre 0 y 10 segundos
    )

    # Combinar los filtros
    filter_complex = f"{subtitle_filter},{underline_filter}"

    # Procesar el video con ffmpeg
    (
        ffmpeg
        .input(video_input_path)
        .output(output_video, vf=filter_complex)
        .run(overwrite_output=True)
    )

    # Retornar el path absoluto del video guardado
    return os.path.abspath(output_video)


if __name__ == "__main__":
    from resources.buscar_clips import VideoDownloader

    video_downloader = VideoDownloader(debug=True)  # Activar mensajes de depuración en la consola
    videos = video_downloader.query(name="food", count=2)
    video_join(*videos)