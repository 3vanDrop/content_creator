from resources.generar_voz import generar_voz as edgetts_generar_voz
from resources.media_join import join_audio
from resources.utils import read_csv
from tests.base_test import BaseTest
import random


class TestTTSAudio(BaseTest):
    inicio_pregunta = ["¿Qué significa.. ", "¿Como traduces.. ", "¿Que quiere decir.. ",
                       "¿Qué es.. ", "¿Sábes que es.. "]
    randomly_pick = lambda self: random.choice(TestTTSAudio.inicio_pregunta)

    def test_audio_edgetts(self):
        intro_audio = self.config["Quizes_v2"]["intro_audio"]
        audios_generados = [intro_audio]

        # Read input csv
        csv_file = read_csv(self.config["Quizes_v2"]["input_csv"])
        self.logger.info(f"csv_file={csv_file}")

        for preguntas in csv_file:
            self.logger.info(f"preguntas={preguntas}")
            # Primer pregunta/respuesta
            pregunta_1 = self._generar_pregunta(1, preguntas[0], preguntas[1],
                                                siguiente=True)
            audios_generados.append(pregunta_1)

            join_audio(*audios_generados, output_file="FinalAudio.mp3")

    def _generar_pregunta(self, num, pregunta, respuesta, siguiente=False):
        audio_to_join = []
        pregunta = edgetts_generar_voz(self.randomly_pick() + pregunta + "?",
                                        output_file="test_audio1.mp3",
                                        expected_duration_ms=4000)
        respuesta = edgetts_generar_voz(f"{respuesta}...",
                                        output_file="test_audio2.mp3",
                                        expected_duration_ms=1500)

        tic_tac_audio = self.config["Quizes_v2"]["tic_tac_audio"]
        success_audio = self.config["Quizes_v2"]["success_audio"]
        siguiente_audio = self.config["Quizes_v2"]["siguiente_audio"]
        audio_to_join += [pregunta, tic_tac_audio, success_audio, respuesta]

        if siguiente:
            audio_to_join.append(siguiente_audio)

        assert self.file_exists(pregunta), f"No Existe {pregunta}!"
        assert self.file_exists(respuesta), f"No Existe {respuesta}!"

        pregunta_output = f"pregunta_{num}.mp3"
        join_audio(*audio_to_join, output_file=pregunta_output)

        return pregunta_output
