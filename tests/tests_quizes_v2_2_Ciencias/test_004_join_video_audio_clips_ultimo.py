from resources.generar_voz import generar_voz as edgetts_generar_voz
from resources.media_join import video_audio_join
from resources.utils import read_csv
from tests.base_test import BaseTest
import time
from . import CONFIG_YAML_KEY, TOTAL_QUIZES


class TestJoinClipsVideoAudio(BaseTest):

    def test_join_clips_video(self):
        total_quizes = TOTAL_QUIZES #10

        for inciso in ["falso"]:
            audio_path = lambda x: self.config[CONFIG_YAML_KEY]["audio_clips"].replace("#", str(x)).replace("*", inciso)
            video_path = lambda x: self.config[CONFIG_YAML_KEY]["video_to_join"].replace("#", str(x)).replace("*", inciso)
            dst_path = lambda x: self.config[CONFIG_YAML_KEY]["ultima_pregunta"].replace(".mp4", f"_{x}.mp4")
            for i in range(total_quizes): # 0 - 9
                timestamp = str(time.time()).replace(".", "_")  # Make them unique
                self.logger.info(f"Joining Final Video {i}...")
                try:
                    assert self.file_exists(video_path(i))
                    assert self.file_exists(audio_path(i))
                    video_audio_join(video_path(i), audio_path(i),
                                     output_resolution="1080x1920",
                                     output_path=dst_path(timestamp))
                except AssertionError:
                    self.logger.info(f"*** Reached the quiz limit ({i}) for inciso {inciso} ***")
                    break  # moving to next inciso