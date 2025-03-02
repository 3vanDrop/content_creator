from resources.subtitles import generar_subtitulos
from tests.base_test import BaseTest

class TestGenerateSubs(BaseTest):

    def test_generate_subtitules_audiolibro(self):
        """Generate subtitles from video with audio"""
        script = [
            "¿Sabías que los perros pueden leer nuestras emociones mejor de lo que pensamos?",
            "Hoy te traigo 5 datos psicológicos sobre los perros que te harán verlos de una manera",
            "completamente nueva. Quédate hasta el final porque el último dato te sorprenderá.",
            "Pueden reconocer nuestras emociones. Los perros no solo entienden nuestro tono de voz,",
            "sino que también pueden interpretar nuestras expresiones faciales. Un estudio demostró",
            "que identifican cuando estamos felices, tristes o enojados, y adaptan su comportamiento",
            "en consecuencia.",
            "Sufren de ansiedad por separación.",
            "Cuando los dejas solos, no solo te extrañan, sino que pueden experimentar un fuerte",
            "estrés. Algunos perros llegan a desarrollar comportamientos destructivos debido a la ",
            "angustia de estar lejos de su humano favorito.",
            "Son empáticos con los humanos",
            "Si alguna vez te has sentido triste y tu perro se ha acercado a consolarte, no es coincidencia. Los estudios han demostrado que los perros pueden detectar nuestro estado emocional y responder con gestos de apoyo."
            "Tienen sueños como nosotros"
            "Sí, los perros sueñan, y lo más interesante es que en sus sueños recrean actividades de su día, como correr, jugar o incluso interactuar con sus dueños. Así que cuando ves que mueven las patas dormidos, probablemente estén soñando contigo.",
            "Nos manipulan con su mirada",
            "Ese “mirada de perrito triste” no es casualidad. Los perros han desarrollado expresiones faciales que los hacen parecer más adorables ante los humanos, lo que les ayuda a obtener lo que quieren, como comida o atención.",
            "Los perros son mucho más inteligentes y emocionales de lo que imaginamos. ¿Cuál de estos datos te sorprendió más? Déjamelo en los comentarios y comparte este video con otros amantes de los perros."
        ]
        self.logger.info("Creating video with audio...")
        video_with_audio = self.create_video_with_audio(
            keywords=["dog", "pet", "animals"],
            video_count=3,
            tts_text=" ".join(script))
        assert self.file_exists(video_with_audio), "Video with Audio shall Exist!"

        self.logger.info("Generating subtitles...")
        srt_output = generar_subtitulos(video_with_audio)
        assert self.file_exists(srt_output), "SRT Subtitles shall Exist!"
