from resources.media_join import video_audio_join, video_join
from resources.generar_voz import generar_voz
from resources.buscar_clips import VideoDownloader


def test_audiolibro():
    video_downloader = VideoDownloader(debug=True)  # Activar mensajes de depuración en la consola

    keywords = ["videogame", "games", "space", "spaceships", "multiplayer", "space soldier"]

    all_videos = list()
    for kw in keywords:
        videos = video_downloader.query(name=kw, count=3)
        all_videos += videos

    output_video = video_join(*all_videos)

    script = [
        "¡Hola, gamers! Bienvenidos a un nuevo video.",
        "Hoy hablaremos de un videojuego legendario: Halo Reach.",
        "Lanzado en 2010 por Bungie, este juego nos transporta a los eventos previos a Halo: Combat Evolved.",
        "La historia sigue a Noble Team, un grupo de supersoldados Spartan que lucha para defender el planeta Reach de la invasión Covenant.",
        "Desde el inicio, el juego nos sumerge en una narrativa intensa y emocionante.",
        "Cada miembro de Noble Team tiene una personalidad única y un papel crucial en la historia.",
        "Uno de los aspectos más impactantes del juego es su tono trágico. Sabemos desde el principio que Reach está condenado.",
        "Las misiones nos llevan a escenarios épicos, desde ciudades devastadas hasta bases militares en el espacio.",
        "El gameplay es sólido, con mecánicas clásicas de Halo y algunas innovaciones, como la personalización de armaduras y las habilidades de combate.",
        "Además, el multijugador de Halo Reach fue revolucionario, con modos como Invasión, Forge y Firefight.",
        "Los gráficos y la banda sonora elevan la experiencia, haciendo que cada momento sea memorable.",
        "Halo Reach no solo es un gran juego de disparos, sino una historia de sacrificio y heroísmo.",
        "Si nunca lo has jugado, te recomiendo darle una oportunidad. Es una joya dentro del universo de Halo.",
        "¿Cuál es tu momento favorito de Halo Reach? Déjalo en los comentarios.",
        "Si te gustó este video, no olvides dar Like y suscribirte para más contenido sobre videojuegos. ¡Nos vemos en la próxima misión, Spartan!"
    ]
    output_path = "salida.mp3"

    output_audio = generar_voz(" ".join(script), output_file=output_path)
    print(f"Archivo MP3 generado en: {output_audio}")

    video_audio_join(*[output_video, output_audio])
