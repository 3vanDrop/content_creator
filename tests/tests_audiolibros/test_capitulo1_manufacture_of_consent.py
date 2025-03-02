from resources.subtitles import generar_subtitulos
from tests.base_test import BaseTest

class TestGenerateSubs(BaseTest):

    def test_generate_subtitules_audiolibro(self):
        """Generate subtitles from video with audio"""
        script = [
            "¡Bienvenidos nuevamente al canal!",
            "¿Alguna vez te has preguntado quién controla la información que consumes? Hoy hablaremos del primer capítulo de 'Manufacture of Consent', un libro de Noam Chomsky y Edward Herman que explica cómo los medios de comunicación moldean nuestra forma de pensar sin que nos demos cuenta.",
            "El modelo de propaganda",
            "Chomsky y Herman presentan el 'modelo de propaganda', que explica cómo los medios no son completamente libres, sino que están influenciados por cinco filtros que determinan qué información llega a nosotros y cómo se presenta.",    
            "Primer filtro: Propiedad de los medios",
            "La mayoría de los medios pertenecen a grandes corporaciones que tienen intereses económicos y políticos. ¿Crees que criticarán a quienes les pagan? Difícilmente.",
            "Segundo filtro: Publicidad",
            "Los medios dependen de la publicidad para sobrevivir. Si una noticia afecta a los anunciantes, lo más probable es que nunca la veas en televisión o redes sociales.",
            "Tercer filtro: Fuentes de información",
            "Los medios necesitan acceso a fuentes confiables como gobiernos y grandes empresas. Si desafían a estas fuentes, pueden perder acceso a la información privilegiada, así que muchas veces prefieren no cuestionarlas.",
            "Cuarto filtro: Flak (Críticas y represalias)",
            "Si un medio publica algo incómodo para los poderosos, se enfrentará a críticas, demandas o incluso amenazas. Esto crea un ambiente de autocensura.",
            "Quinto filtro: Anticomunismo y control ideológico",
            "Históricamente, el miedo al comunismo se usó para silenciar opiniones alternativas. Hoy en día, otros temas cumplen esta función, como la 'guerra contra el terrorismo' o la 'protección de la democracia'.",
            "En conclusión",
            "Los medios no solo informan, también moldean nuestra percepción del mundo. Noam Chomsky nos advierte que debemos ser críticos con lo que consumimos y buscar diferentes perspectivas. ¿Crees que hoy en día sigue funcionando este modelo? Déjamelo en los comentarios y comparte este video si te gustó."
        ]
        self.logger.info("Creating video with audio...")
        video_with_audio = self.create_video_with_audio(
            keywords=["propaganda", "censorship", "power", "media", "influence"],
            video_count=4,
            tts_text=" ".join(script))
        assert self.file_exists(video_with_audio), "Video with Audio shall Exist!"

        self.logger.info("Generating subtitles...")
        srt_output = generar_subtitulos(video_with_audio)
        assert self.file_exists(srt_output), "SRT Subtitles shall Exist!"
