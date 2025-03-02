from resources.subtitles import generar_subtitulos
from tests.base_test import BaseTest

class TestGenerateSubs(BaseTest):

    def test_generate_subtitules_audiolibro(self):
        """Generate subtitles from video with audio"""
        script = [
            "Capítulo 3, La economía política de los medios",
            "¿Quién controla los medios? En este video, exploramos el tercer capítulo de 'Manufacture of Consent' de Noam Chomsky y Edward Herman, donde explican cómo el dinero y el poder influyen en la información que consumimos.",
            
            "El modelo de propaganda",
            "Los medios de comunicación no son entidades neutrales. Están financiados por corporaciones, anunciantes y gobiernos que influyen en su contenido. Esto significa que lo que vemos y leemos está filtrado por intereses económicos y políticos.",
            
            "El poder de la publicidad",
            "Los grandes medios dependen de la publicidad para financiarse. Esto les impide publicar contenido que pueda afectar negativamente a sus anunciantes. Así, ciertos temas son ignorados o suavizados para proteger intereses comerciales.",
            
            "La concentración de medios",
            "Un puñado de corporaciones controla la mayoría de los medios en el mundo. Esto limita la diversidad de opiniones y favorece narrativas que benefician a quienes están en el poder.",
            
            "Ejemplo moderno",
            "Piensa en cómo se presentan las noticias sobre el cambio climático. Muchos medios minimizan el impacto ambiental porque sus anunciantes incluyen empresas petroleras y grandes industrias. Así, la verdad se distorsiona en favor de quienes pagan por la publicidad.",
            
            "En Conclusión",
            "El tercer capítulo de 'Manufacture of Consent' revela que los medios no solo informan, sino que protegen los intereses de quienes los financian. Para entender la realidad, debemos cuestionar lo que consumimos y buscar fuentes diversas. ¿Crees que los medios son imparciales? Déjamelo en los comentarios y comparte este video.",
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
