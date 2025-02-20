from resources.media_join import video_audio_join, video_join
from resources.generar_voz_gtts import generar_voz
from resources.buscar_clips import VideoDownloader


def test_video_audio_realistic_join():
    video_downloader = VideoDownloader(debug=True)  # Activar mensajes de depuración en la consola

    keywords = ["relativity", "time", "gravity", "space", "speed"]

    all_videos = list()
    for kw in keywords:
        videos = video_downloader.query(name=kw, count=1)
        all_videos.append(*videos)

    output_video = video_join(*all_videos)

    script = [
        "¿Sabías que el tiempo no pasa igual para todos?",
        "Esto no es solo una idea de ciencia ficción, sino una realidad comprobada por la física.",
        "Gracias a la teoría de la relatividad de Albert Einstein, sabemos que la gravedad y la velocidad afectan el tiempo.",
        "Por ejemplo, los astronautas que pasan meses en la Estación Espacial Internacional envejecen un poco más lento que nosotros en la Tierra.",
        "Esto sucede porque están moviéndose a gran velocidad en órbita y experimentan menos gravedad que en la superficie terrestre.",
        "De hecho, los relojes atómicos en satélites GPS deben ser ajustados constantemente para compensar este efecto.",
        "Si no se hiciera, nuestros sistemas de navegación tendrían errores de varios metros en cuestión de minutos.",
        "Pero, ¿qué pasaría si viajaras cerca de la velocidad de la luz?",
        "Según la relatividad, cuanto más rápido te mueves, más lento pasa el tiempo para ti en comparación con alguien en reposo.",
        "Si pudieras viajar a una velocidad cercana a la luz y regresar a la Tierra después de unos años, podrías encontrar que aquí han pasado siglos.",
        "Este fenómeno se conoce como dilatación del tiempo y ha sido probado en experimentos con partículas subatómicas.",
        "Así que la próxima vez que pienses en el tiempo, recuerda que no es absoluto, sino relativo a tu movimiento y la gravedad a tu alrededor.",
        "El universo es un lugar increíble lleno de maravillas científicas... ¡y aún nos queda mucho por descubrir!"
    ]
    idioma = "es"  # Código de idioma para español
    output_path = "salida.mp3"

    output_audio = generar_voz(" ".join(script), idioma, output_path)
    print(f"Archivo MP3 generado en: {output_audio}")

    video_audio_join(*[output_video, output_audio])
