import whisper  
import sys

def generar_subtitulos(video_path, output_srt_path="subtitles.srt", model_size="base"):
    """
    Genera un archivo de subtítulos en formato SRT a partir de un video.

    Parámetros:
        video_path (str): Ruta del archivo de video.
        output_srt_path (str): Ruta donde se guardará el archivo SRT (opcional, por defecto "subtitles.srt").
        model_size (str): Tamaño del modelo Whisper ("tiny", "base", "small", "medium", "large").

    Retorna:
        str: Ruta del archivo SRT generado.
    """

    # Cargar modelo de Whisper
    model = whisper.load_model(model_size)

    # Transcribir el audio del video
    result = model.transcribe(video_path)

    # Guardar la transcripción en formato SRT
    with open(output_srt_path, "w", encoding="utf-8") as f:
        for segment in result["segments"]:
            start = segment["start"]
            end = segment["end"]
            text = segment["text"]

            # Formato SRT (HH:MM:SS,mmm --> HH:MM:SS,mmm)
            f.write(f"{segment['id'] + 1}\n")
            f.write(f"{format_time(start)} --> {format_time(end)}\n")
            f.write(f"{text}\n\n")

    print(f"Subtítulos guardados en: {output_srt_path}")
    return output_srt_path


def format_time(seconds):
    """
    Convierte segundos en formato SRT (HH:MM:SS,mmm).

    Parámetro:
        seconds (float): Tiempo en segundos.

    Retorna:
        str: Tiempo formateado en HH:MM:SS,mmm
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    milliseconds = int((seconds % 1) * 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"


# Ejemplo de uso
if __name__ == "__main__":
    generar_subtitulos("video.mp4", "subtitulos.srt")
