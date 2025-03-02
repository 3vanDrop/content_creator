from resources.generar_voz import generar_voz as edgetts_generar_voz
from resources.media_join import join_audio
from tests.base_test import BaseTest

class TestQuizIntro(BaseTest):
    VOZ = "es-MX-DaliaNeural"
    def test_intro(self):
        audio_path1 = edgetts_generar_voz("¡Pon a prueba tu inteligencia! Responde antes de que el tiempo se acabe… pero cuidado, solo los más rápidos lo lograrán.",
                                          output_file="intro.mp3",
                                          voz=self.VOZ)

        assert self.file_exists(audio_path1), f"Existe {audio_path1}"

    def test_siguiente_pregunta(self):
        audio_path1 = edgetts_generar_voz("¿Lo resolviste? Vamos con otra…",
                                          output_file="siguiente_1.mp3",
                                          expected_duration_ms=3300,
                                          voz=self.VOZ)
        audio_path2 = edgetts_generar_voz("Siguiente pregunta..",
                                          output_file="siguiente_2.mp3",
                                          expected_duration_ms=3300,
                                          voz=self.VOZ)
        audio_path3 = edgetts_generar_voz("¿Estuvo fácil? Continuemos...",
                                          output_file="siguiente_3.mp3",
                                          expected_duration_ms=3300,
                                          voz=self.VOZ)

        assert self.file_exists(audio_path1), f"Existe {audio_path1}"
        assert self.file_exists(audio_path2), f"Existe {audio_path2}"
        assert self.file_exists(audio_path3), f"Existe {audio_path3}"

    def test_ultima_pregunta(self):
        audio_path1 = edgetts_generar_voz("Última pregunta y solo para expertos. ",
                                          output_file="ultima.mp3",
                                          voz=self.VOZ)
        
        audio_path2 = edgetts_generar_voz("Y tú, ¿Cuántas acertaste?!!. ¡Comenta tu resultado y reta a un amigo!",
                                          output_file="end_audio.mp3",
                                          voz=self.VOZ)

        assert self.file_exists(audio_path1), f"Existe {audio_path1}"
        assert self.file_exists(audio_path2), f"Existe {audio_path2}"
