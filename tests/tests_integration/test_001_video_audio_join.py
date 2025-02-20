from resources.media_join import video_audio_join, video_join
from resources.generar_voz_gtts import generar_voz
from resources.buscar_clips import VideoDownloader


def test_video_audio_join():
    video_downloader = VideoDownloader(debug=True)  # Activar mensajes de depuración en la consola
    videos = video_downloader.query(name="food", count=5)
    output_video = video_join(*videos)

    # Ejemplo de uso
    texto = "Hola, este es un ejemplo de texto a voz."
    idioma = "es"  # Código de idioma para español
    output_path = "salida.mp3"

    ruta_absoluta = generar_voz(texto, idioma, output_path)
    print(f"Archivo MP3 generado en: {ruta_absoluta}")

    video_audio_join(*[output_video, ruta_absoluta])
