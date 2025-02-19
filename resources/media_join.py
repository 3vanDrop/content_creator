"""This library has been created using DeepSeek"""
import ffmpeg

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
