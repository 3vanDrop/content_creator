from resources.subtitles import generar_subtitulos
from tests.base_test import BaseTest

class TestGenerateSubs(BaseTest):

    def test_generate_subtitules_audiolibro(self):
        """Generate subtitles from video with audio"""
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
        self.logger.info("Creating video with audio...")
        video_with_audio = self.create_video_with_audio(
            keywords=["habits", "growth", "success", "identity", "self improvement", "change"],
            tts_text=" ".join(script))
        assert self.file_exists(video_with_audio), "Video with Audio shall Exist!"

        self.logger.info("Generating subtitles...")
        srt_output = generar_subtitulos(video_with_audio)
        assert self.file_exists(srt_output), "SRT Subtitles shall Exist!"
