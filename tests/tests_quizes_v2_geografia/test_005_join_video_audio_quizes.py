from resources.generar_voz import generar_voz as edgetts_generar_voz
from resources.media_join import video_audio_join
from resources.utils import read_csv
from tests.base_test import BaseTest
import time
from . import CONFIG_YAML_KEY


class TestTTSAudio(BaseTest):

    def test_join_quiz_video(self):
        total_quizes = 50 #10
        audio_path = lambda x: self.config[CONFIG_YAML_KEY]["audio_to_join"].replace("*", str(x))
        video_path = lambda x: self.config[CONFIG_YAML_KEY]["video_to_join"].replace("*", str(x))
        timestamp = str(time.time()).replace(".", "_")
        dst_path = lambda x: self.config[CONFIG_YAML_KEY]["video_output_join"].replace("*", str(x)).replace("&", "#").replace(".mp4", f"_{timestamp}.mp4")

        for i in range(total_quizes): # 0 - 9
            self.logger.info(f"Joining Final Video {i}...")
            assert self.file_exists(video_path(i))
            assert self.file_exists(audio_path(i))

            video_audio_join(video_path(i), audio_path(i),
                             output_resolution="1080x1920",
                             output_path=dst_path(i))