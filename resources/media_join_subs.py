import os
import pysrt
import ffmpeg

from resources.utils import time_it

@time_it
def parse_srt(srt_path):
    subtitles = pysrt.open(srt_path)
    words = []
    for sub in subtitles:
        start_time = sub.start.ordinal  # Tiempo de inicio en milisegundos
        end_time = sub.end.ordinal  # Tiempo de fin en milisegundos
        text = sub.text
        words.extend([(word, start_time, end_time) for word in text.split()])
    return words

@time_it
def render_word(video_input_path, word, start_time, end_time, output_path):
    # Duración de la palabra en segundos
    duration = (end_time - start_time) / 1000.0

    # Filtro para el subrayado dinámico
    filter_complex = (
        f"drawtext="
        f"fontcolor=yellow:"
        f"fontsize=24:"
        f"fontfile=/System/Library/Fonts/Supplemental/Arial.ttf:"  # Ruta a la fuente Arial
        f"text='{word}':"
        f"x=(w-tw)/2:"  # Centrar horizontalmente
        f"y=h-th-10:"  # Posicionar cerca de la parte inferior
        f"box=1:"  # Habilitar fondo
        f"boxcolor=black@0.5:"  # Color del fondo (negro semitransparente)
        f"boxborderw=5:"  # Grosor del borde
        f"enable='between(t,{start_time / 1000.0},{end_time / 1000.0})'"  # Habilitar entre start_time y end_time
    )

    # Procesar el video con ffmpeg
    (
        ffmpeg
        .input(video_input_path)
        .output(output_path, vf=filter_complex, t=duration)
        .run(overwrite_output=True)
    )

@time_it
def combine_videos(video_paths, output_path):
    # Crear una lista de inputs para ffmpeg
    inputs = [ffmpeg.input(path) for path in video_paths]

    # Combinar los videos
    (
        ffmpeg
        .concat(*inputs, v=1, a=0)
        .output(output_path)
        .run(overwrite_output=True)
    )

@time_it
def video_join_subs(video_input_path, srt_input_path, output_video):
    # Procesar el archivo SRT
    words = parse_srt(srt_input_path)

    # Renderizar cada palabra
    video_paths = []
    for i, (word, start_time, end_time) in enumerate(words):
        output_path = f"temp_word_{i}.mp4"
        render_word(video_input_path, word, start_time, end_time, output_path)
        video_paths.append(output_path)

    # Combinar todos los videos renderizados
    combine_videos(video_paths, output_video)

    # Eliminar archivos temporales
    for path in video_paths:
        os.remove(path)
