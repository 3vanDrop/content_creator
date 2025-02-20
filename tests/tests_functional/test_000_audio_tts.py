from resources.generar_voz_gtts import generar_voz as gtts_generar_voz
from resources.generar_voz import generar_voz as edgetts_generar_voz
from tests.base_test import BaseTest

class TestTTSAudio(BaseTest):
    def test_audio_gtts(self):
        audio_path = gtts_generar_voz("Hola este es un test case para generar audio.",
                                      idioma="es",
                                      output_file="test_audio.mp3")

        assert self.file_exists(audio_path), f"Existe {audio_path}"

    def test_audio_edgetts(self):
        audio_path = edgetts_generar_voz("Hola este es un segundo test case para generar audio.",
                                         output_file="test_audio2.mp3")

        assert self.file_exists(audio_path), f"Existe {audio_path}"
