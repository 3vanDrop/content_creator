from resources.media_join import video_audio_join, video_join
from resources.generar_voz import generar_voz
from resources.buscar_clips import VideoDownloader


def test_audiolibro():
    video_downloader = VideoDownloader(debug=True)  # Activar mensajes de depuración en la consola

    keywords = ["habits", "growth", "success", "identity", "self improvement", "change"]

    all_videos = list()
    for kw in keywords:
        videos = video_downloader.query(name=kw, count=2)
        all_videos += videos

    output_video = video_join(*all_videos)

    script = [
        "¡Bienvenidos nuevamente a mi canal!",
        "El día de hoy hablaremos de un libro que puede cambiar tu vida: Hábitos Atómicos de James Clear.",
        "En el capítulo 1, el autor nos explica por qué los pequeños cambios pueden hacer una gran diferencia.",
        "Muchas personas piensan que para mejorar deben hacer transformaciones drásticas, pero la clave está en mejorar solo un 1% cada día.",
        "Este concepto se basa en el poder del crecimiento gradual. Pequeñas mejoras diarias se acumulan con el tiempo y generan resultados sorprendentes.",
        "James Clear nos cuenta que los hábitos son como el interés compuesto: pequeñas acciones repetidas llevan a grandes logros.",
        "El verdadero cambio no ocurre de la noche a la mañana, sino a través de la identidad que construimos con nuestros hábitos.",
        "En lugar de fijarte solo en los objetivos, enfócate en convertirte en la persona que los logra.",
        "Por ejemplo, en vez de decir 'quiero correr una maratón', dite a ti mismo 'soy un corredor'.",
        "Cuando adoptamos una identidad alineada con nuestros hábitos, el progreso se vuelve inevitable.",
        "Así que recuerda: cada pequeño cambio cuenta y te acerca a la persona que quieres ser.",
        "Si te gustó este video, no olvides dar Like y suscribirte para ver más contenido sobre crecimiento personal. ¡Nos vemos en el próximo video!"
    ]
    output_path = "salida.mp3"

    output_audio = generar_voz(" ".join(script), output_file=output_path)
    print(f"Archivo MP3 generado en: {output_audio}")
