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
    # Convertir rutas a formato absoluto
    video_input_path = video_input_path.replace("\\", "/")
    srt_input_path = srt_input_path.replace("\\", "/")
    
    logger.debug(f"video_input_path={video_input_path}")
    logger.debug(f"srt_input_path={srt_input_path}")

    # 🔹 Verificar si el archivo SRT existe
    if not os.path.exists(srt_input_path.strip('"')):  # Quitar comillas antes de verificar
        print(f"Error: No se encontró el archivo SRT en {srt_input_path}")
        return None

    try:
        # 🔹 Pasar la ruta corregida en comillas dobles
        ffmpeg_cmd = (
            ffmpeg
            .input(video_input_path)
            .output(
                output_video,
                vf=f"subtitles={srt_input_path}",  # Comillas dobles en ruta SRT
                vcodec="libx264",
                acodec="aac",
                strict="experimental"
            )
        )

        # Ejecutar FFmpeg y capturar salida
        ffmpeg_cmd.run(overwrite_output=True, capture_stdout=True, capture_stderr=True)

        return output_video  # Retorna la ruta del video generado

    except ffmpeg.Error as e:
        print("Error al procesar el video:", e.stderr.decode())
        return None  # Retorna None si ocurre un error

if __name__ == "__main__":
    from resources.buscar_clips import VideoDownloader

    video_downloader = VideoDownloader(debug=True)  # Activar mensajes de depuración en la consola
    videos = video_downloader.query(name="food", count=2)
    video_join(*videos)