from resources.generar_voz import generar_voz as edgetts_generar_voz
from resources.media_join import join_audio
from resources.utils import read_csv, get_random_file_path
from tests.base_test import BaseTest
import random
from . import CONFIG_YAML_KEY
import shutil
from pydub import AudioSegment
import os


class TestCreateAudios(BaseTest):
    def test_create_audios(self):
        for key in ["cierto", "falso"]:
            # Read input csv
            csv_file = read_csv(self.config[CONFIG_YAML_KEY]["input_respuestas"].replace("*", key))
            output_clips_path = lambda num: self.config[CONFIG_YAML_KEY]["audio_clips"].replace("*", key).replace("#", str(num))
            self.logger.info(f"csv_file={csv_file}")

            # Clean audio clips folder before creating new ones
            audio_folder = os.path.dirname(output_clips_path(0))
            self.clean_up_workspace(audio_folder)

            audio_clip_count = 0
            for preguntas in csv_file:
                self.logger.info(f"preguntas={preguntas}")
                self.logger.info(f"output_path={output_clips_path(audio_clip_count)}")
                # Primer pregunta/respuesta
                self._generar_pregunta(audio_clip_count, preguntas[0], preguntas[1], preguntas[2],
                                       siguiente=True,
                                       output_path=output_clips_path(audio_clip_count))

                self.clean_up_workspace()
                audio_clip_count += 1

    def _generar_pregunta(self, num, pregunta, respuesta, explicacion, output_path, siguiente=False):
        audio_to_join = []
        pregunta = edgetts_generar_voz(pregunta,
                                        output_file="test_audio1.mp3",
                                        expected_duration_ms=3800)
        respuesta = edgetts_generar_voz(f"{respuesta}...",
                                        output_file="test_audio2.mp3",
                                        expected_duration_ms=1800)
        explicacion = edgetts_generar_voz(f"{explicacion}...",
                                        output_file="test_audio3.mp3",
                                        expected_duration_ms=4300)

        tic_tac_audio = self.config[CONFIG_YAML_KEY]["tic_tac_audio"]
        success_audio = self.config[CONFIG_YAML_KEY]["success_audio"]
        siguiente_audio = self.config[CONFIG_YAML_KEY]["siguiente_audio"]
        audio_to_join += [pregunta, tic_tac_audio, success_audio, respuesta, explicacion]

        if siguiente:
            self.file_exists(siguiente_audio)
            audio_to_join.append(siguiente_audio)

        assert self.file_exists(pregunta), f"No Existe {pregunta}!"
        assert self.file_exists(respuesta), f"No Existe {respuesta}!"

        pregunta_output = f"pregunta_{num}.mp3"
        join_audio(*audio_to_join, output_file=output_path)

        self.logger.info(f"** Completed audio clip: {output_path}")
        return pregunta_output
