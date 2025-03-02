from resources.subtitles import generar_subtitulos
from tests.base_test import BaseTest

class TestGenerateSubs(BaseTest):

    def test_generate_subtitules_audiolibro(self):
        """Generate subtitles from video with audio"""
        script = [
            "Capítulo 4, Los filtros de la información",
            "¿Por qué ciertas noticias llegan a nosotros y otras no? En este capítulo, Chomsky y Herman explican los cinco filtros que moldean la información en los medios de comunicación.",
            
            "Los cinco filtros",
            "1. Propiedad de los medios: Grandes corporaciones poseen los medios y priorizan sus intereses.",
            "2. Publicidad: Los ingresos publicitarios influyen en qué contenido se publica.",
            "3. Fuentes oficiales: Los medios dependen de información de gobiernos y corporaciones.",
            "4. Flak o represalias: Críticas y presiones limitan lo que se puede publicar.",
            "5. Enemigos ideológicos: Narrativas que favorecen la agenda del poder.",
            
            "En Conclusión",
            "El cuarto capítulo revela cómo estos filtros limitan el acceso a la verdad. Si queremos estar informados, debemos diversificar nuestras fuentes de información."
        ]

        self.logger.info("Creating video with audio...")
        video_with_audio = self.create_video_with_audio(
            keywords=["advertisement", "censorship", "power", "media", "propaganda"],
            video_count=4,
            tts_text=" ".join(script))
        assert self.file_exists(video_with_audio), "Video with Audio shall Exist!"

        self.logger.info("Generating subtitles...")
        srt_output = generar_subtitulos(video_with_audio)
        assert self.file_exists(srt_output), "SRT Subtitles shall Exist!"
