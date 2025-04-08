from resources.generar_voz import generar_voz as edgetts_generar_voz
from resources.media_join import join_audio
from resources.utils import read_csv
from tests.base_test import BaseTest
import random
from . import CONFIG_YAML_KEY


class TestPregunta(BaseTest):
    def test_audio_edgetts(self):
        audios_generados = []

        # Read input csv
        csv_file = read_csv(self.config[CONFIG_YAML_KEY]["input_respuestas"].replace("*", "cierto"))
        self.logger.info(f"csv_file={csv_file}")

        for preguntas in csv_file:
            self.logger.info(f"preguntas={preguntas}")
            # Primer pregunta/respuesta
            pregunta_1 = self._generar_pregunta(1, preguntas[0], preguntas[1], preguntas[2],
                                                siguiente=True)
            audios_generados.append(pregunta_1)

            join_audio(*audios_generados, output_file="FinalAudio.mp3")
            break

    def _generar_pregunta(self, num, pregunta, respuesta, explicacion, siguiente=False):
        audio_to_join = []
        pregunta = edgetts_generar_voz(pregunta,
                                        output_file="test_audio1.mp3",
                                        expected_duration_ms=4000)
        respuesta = edgetts_generar_voz(f"{respuesta}...",
                                        output_file="test_audio2.mp3",
                                        expected_duration_ms=1700)
        explicacion = edgetts_generar_voz(f"{explicacion}...",
                                        output_file="test_audio3.mp3",
                                        expected_duration_ms=5000)

        tic_tac_audio = self.config[CONFIG_YAML_KEY]["tic_tac_audio"]
        success_audio = self.config[CONFIG_YAML_KEY]["success_audio"]
        siguiente_audio = self.config[CONFIG_YAML_KEY]["siguiente_audio"]
        audio_to_join += [pregunta, tic_tac_audio, success_audio, respuesta, explicacion]

        if siguiente:
            audio_to_join.append(siguiente_audio)

        assert self.file_exists(pregunta), f"No Existe {pregunta}!"
        assert self.file_exists(respuesta), f"No Existe {respuesta}!"

        pregunta_output = f"pregunta_{num}.mp3"
        join_audio(*audio_to_join, output_file=pregunta_output)

        return pregunta_output
