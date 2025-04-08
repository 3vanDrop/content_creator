from resources.generar_voz import generar_voz as edgetts_generar_voz
from resources.media_join import join_audio
from tests.base_test import BaseTest
from pydub import AudioSegment

class TestBaseVoices(BaseTest):
    voz = "es-MX-DaliaNeural" # "es-MX-JorgeNeural"

    siguiente_pregunta = ["¡Vamos con la siguiente...!",
                          "¿Listo para otra?",
                          "¡Vamos por la siguiente...!",
                          "¡Próxima pregunta...¡",
                          "!Continuamos...¡",
                          "¡Siguiente pregunta...!",
                          "¿Sorprendido?",
                          "¿Acertaste?"]

    def test_siguiente_pregunta(self):
        for i, sig in enumerate(self.siguiente_pregunta):
            audio_path = edgetts_generar_voz(sig,
                                              voz=self.voz,
                                              expected_duration_ms=2000,
                                              output_file=f"siguiente_{i}.mp3")
            self.logger.info(f"siguiente duration={len(AudioSegment.from_file(audio_path))}")

            assert self.file_exists(audio_path), f"Existe {audio_path}"

    def test_ending_1(self):
        audio_path1 = edgetts_generar_voz("¡Cuéntame cuántas acertaste en los comentarios y no olvides suscribirte para más contenido como éste!",
                                          voz=self.voz,
                                          expected_duration_ms=9000,
                                          output_file="ending_1.mp3")
        
        audio_duration = len(AudioSegment.from_file(audio_path1))
        self.logger.info(f"audio_duration={audio_duration}")

        assert self.file_exists(audio_path1), f"Existe {audio_path1}"

    def test_ending_2(self):
        audio_path1 = edgetts_generar_voz("¿Qué puntuación obtuviste? Házmelo saber en los comentarios y no olvides suscribirte para más contenido diario.",
                                          voz=self.voz,
                                          expected_duration_ms=9000,
                                          output_file="ending_2.mp3")

        audio_duration = len(AudioSegment.from_file(audio_path1))
        self.logger.info(f"audio_duration={audio_duration}")

        assert self.file_exists(audio_path1), f"Existe {audio_path1}"

    def test_ending_3(self):
        audio_path1 = edgetts_generar_voz("¿Cuántas acertaste? Déjame tu respuesta en los comentarios y si quieres más quizzes, ¡suscríbete para no perderte el contenido diario!",
                                          voz=self.voz,
                                          expected_duration_ms=9000,
                                          output_file="ending_3.mp3")

        audio_duration = len(AudioSegment.from_file(audio_path1))
        self.logger.info(f"audio_duration={audio_duration}")

        assert self.file_exists(audio_path1), f"Existe {audio_path1}"

    def test_suscribete(self):
        """suscribete"""
        audio_path1 = edgetts_generar_voz("Mira todas las listas de reproduccion que tenemos en el canal!",
                                          voz=self.voz,
                                          output_file="suscribete.mp3")

        audio_duration = len(AudioSegment.from_file(audio_path1))
        self.logger.info(f"audio_duration={audio_duration}")

        assert self.file_exists(audio_path1), f"Existe {audio_path1}"
