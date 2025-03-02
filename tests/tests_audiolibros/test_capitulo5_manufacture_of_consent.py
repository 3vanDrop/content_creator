from resources.subtitles import generar_subtitulos
from tests.base_test import BaseTest

class TestGenerateSubs(BaseTest):

    def test_generate_subtitules_audiolibro(self):
        """Generate subtitles from video with audio"""
        script = [
            "Capítulo 5, La construcción de enemigos",
            "¿Cómo los medios crean villanos? En este capítulo, se analiza cómo los medios refuerzan narrativas de enemigos externos e internos para justificar ciertas políticas.",
            
            "Ejemplo clásico",
            "Durante la Guerra Fría, los medios occidentales demonizaban constantemente a la Unión Soviética, mientras que la prensa soviética hacía lo mismo con Estados Unidos. Estas narrativas justificaban guerras, inversiones militares y políticas represivas.",
            
            "Ejemplo moderno",
            "Hoy en día, los medios refuerzan narrativas sobre migrantes, activistas o naciones rivales para mantener el statu quo.",
            
            "En Conclusión",
            "El quinto capítulo de 'Manufacture of Consent' nos muestra que los medios son herramientas clave en la construcción de enemigos. Cuestionemos a quiénes nos presentan como amenaza y por qué."
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
