from resources.subtitles import generar_subtitulos
from tests.base_test import BaseTest

class TestGenerateSubs(BaseTest):

    def test_generate_subtitules_audiolibro(self):
        """Generate subtitles from video with audio"""
        script = [
            "Capítulo 6, Medios y democracia",
            "Los medios deberían servir a la democracia, pero ¿realmente lo hacen? Chomsky y Herman explican cómo la manipulación de la información limita la participación ciudadana.",
            
            "El problema",
            "Si la información está sesgada por intereses económicos y políticos, ¿cómo puede la gente tomar decisiones informadas?",
            
            "Ejemplo",
            "Los debates políticos a menudo excluyen visiones alternativas, lo que refuerza el poder de los grupos dominantes.",
            
            "En Conclusión",
            "Para que la democracia funcione, necesitamos medios independientes y ciudadanos críticos. No basta con consumir noticias; hay que analizarlas."
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
