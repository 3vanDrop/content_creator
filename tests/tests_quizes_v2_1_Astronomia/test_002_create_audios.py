from resources.generar_voz import generar_voz as edgetts_generar_voz
from resources.media_join import join_audio
from resources.utils import read_csv
from tests.base_test import BaseTest
import random
from . import CONFIG_YAML_KEY
import shutil
from pydub import AudioSegment
import os


class TestCreateAudios(BaseTest):
    def test_create_audios(self):
        for inciso in ["a", "b", "c", "d"]: #"a", "b", "c", "d"
            # Read input csv
            csv_file = read_csv(self.config[CONFIG_YAML_KEY]["input_respuestas"].replace("*", inciso))
            output_clips_path = lambda num: self.config[CONFIG_YAML_KEY]["audio_clips"].replace("*", inciso).replace("#", str(num))
            self.logger.info(f"csv_file={csv_file}")

            # Clean audio clips folder before creating new ones
            audio_folder = os.path.dirname(output_clips_path(0))
            self.clean_up_workspace(audio_folder)

            audio_clip_count = 0
            for preguntas in csv_file:
                self.logger.info(f"preguntas={preguntas}")
                # Primer pregunta/respuesta
                self._generar_pregunta(audio_clip_count, preguntas[0], preguntas[1],
                                       siguiente=True,
                                       output_path=output_clips_path(audio_clip_count))

                self.clean_up_workspace()
                audio_clip_count += 1

    def _generar_pregunta(self, num, pregunta, respuesta, siguiente=False, output_path="pregunta.mp3"):
        audio_to_join = []
        pregunta = edgetts_generar_voz(pregunta,
                                        output_file="test_audio1.mp3",
                                        expected_duration_ms=4100)
        respuesta = edgetts_generar_voz(f"{respuesta}...",
                                        output_file="test_audio2.mp3",
                                        expected_duration_ms=2000)

        tic_tac_audio = self.config[CONFIG_YAML_KEY]["tic_tac_audio"]
        success_audio = self.config[CONFIG_YAML_KEY]["success_audio"]
        siguiente_audio = self.config[CONFIG_YAML_KEY]["siguiente_audio"]
        audio_to_join += [pregunta, tic_tac_audio, success_audio, respuesta]

        if siguiente:
            audio_to_join.append(siguiente_audio)

        assert self.file_exists(pregunta), f"No Existe {pregunta}!"
        assert self.file_exists(respuesta), f"No Existe {respuesta}!"

        join_audio(*audio_to_join, output_file=output_path)

        return output_path
