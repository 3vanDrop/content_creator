from resources.generar_voz import generar_voz as edgetts_generar_voz
from resources.media_join import join_audio
from tests.base_test import BaseTest
from pydub import AudioSegment

class TestQuizIntro(BaseTest):
    def test_intro(self):
        audio_path1 = edgetts_generar_voz("¡Solo un Experto en Cine y TV acierta a todas las preguntas!",
                                          output_file="intro.mp3",
                                          expected_duration_ms=4272)

        audio_duration = len(AudioSegment.from_file(audio_path1))
        self.logger.info(f"audio_duration={audio_duration}")
        assert self.file_exists(audio_path1), f"Existe {audio_path1}"

    def test_siguiente_pregunta(self):
        audio_path1 = edgetts_generar_voz("Siguiente",
                                          output_file="siguiente.mp3")

        audio_path1 = edgetts_generar_voz("Siguiente",
                                          output_file="siguiente.mp3")

        assert self.file_exists(audio_path1), f"Existe {audio_path1}"

    def test_niveles(self):
        audio_path1 = edgetts_generar_voz("Nivel Fácil",
                                          output_file="facil.mp3")
        
        audio_path2 = edgetts_generar_voz("¿Estuvo fácil? Continuemos...",
                                          output_file="end_facil.mp3")

        audio_path3 = edgetts_generar_voz("Nivel Medio",
                                          output_file="medio.mp3")

        audio_path3 = edgetts_generar_voz("Nivel Dificil",
                                          output_file="dificil.mp3")

        assert self.file_exists(audio_path1), f"Existe {audio_path1}"
        assert self.file_exists(audio_path2), f"Existe {audio_path2}"
        assert self.file_exists(audio_path3), f"Existe {audio_path3}"

    def test_ultima_pregunta(self):
        audio_path1 = edgetts_generar_voz("Última pregunta y solo para expertos. ",
                                          output_file="ultima.mp3")
        
        audio_path2 = edgetts_generar_voz("¿Sabes la respuesta?, ¡Dejala en los comentarios!",
                                          output_file="end_audio.mp3")
        audio_duration = len(AudioSegment.from_file(audio_path2))
        self.logger.info(f"audio_duration={audio_duration}")

        assert self.file_exists(audio_path1), f"Existe {audio_path1}"
        assert self.file_exists(audio_path2), f"Existe {audio_path2}"
