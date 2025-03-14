from resources.generar_voz import generar_voz as edgetts_generar_voz
from resources.media_join import join_audio
from tests.base_test import BaseTest
from pydub import AudioSegment

class TestQuizIntro(BaseTest):
    def test_intro(self):
        audio_path1 = edgetts_generar_voz("¡Solo los verdaderos expertos en caricaturas de los 90 podrán acertar todas!",
                                          output_file="intro.mp3")

        audio_duration = len(AudioSegment.from_file(audio_path1))
        self.logger.info(f"audio_duration={audio_duration}")
        assert self.file_exists(audio_path1), f"Existe {audio_path1}"

    def test_siguiente_pregunta(self):
        audio_path1 = edgetts_generar_voz("Siguiente",
                                          output_file="siguiente.mp3")

        audio_path1 = edgetts_generar_voz("Siguiente",
                                          output_file="siguiente.mp3")

        assert self.file_exists(audio_path1), f"Existe {audio_path1}"

