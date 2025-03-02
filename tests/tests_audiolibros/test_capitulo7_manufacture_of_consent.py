from resources.subtitles import generar_subtitulos
from tests.base_test import BaseTest

class TestGenerateSubs(BaseTest):

    def test_generate_subtitules_audiolibro(self):
        """Generate subtitles from video with audio"""
        script = [
            "Capítulo 7, Alternativas y soluciones",
            "¿Qué podemos hacer frente a esta manipulación? En el capítulo final, los autores proponen alternativas para un sistema mediático más justo.",
            
            "Alternativas",
            "1. Apoyar medios independientes.",
            "2. Crear contenido alternativo en redes sociales.",
            "3. Educar en pensamiento crítico.",
            "4. Exigir transparencia en los medios.",
            
            "Conclusión",
            "Si queremos una sociedad mejor informada, debemos buscar activamente la verdad y promover la diversidad informativa. ¿Qué opinas? Déjamelo en los comentarios y comparte este video."
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
