from resources.generar_voz import generar_voz as edgetts_generar_voz
from resources.media_join import join_audio
from resources.media_join import video_add_silent_audio_track
from resources.utils import get_all_files
from tests.base_test import BaseTest
from pydub import AudioSegment
from . import CONFIG_YAML_KEY
import os

class TestBaseVoices(BaseTest):
    def test_siguiente_pregunta(self):
        thumbnail_path = get_all_files(self.config[CONFIG_YAML_KEY]["thumbnails"])
        for thumbnail in thumbnail_path:
            assert self.file_exists(thumbnail)
            thumbnail_filename = os.path.basename(thumbnail)
            thumbnail_path = os.path.dirname(thumbnail)
            thumbnail_output_path = os.path.join(thumbnail_path,
                                                 "silent",
                                                 thumbnail_filename)
            video_add_silent_audio_track(input_video=thumbnail,
                                         output_path=thumbnail_output_path)

            assert self.file_exists(thumbnail_output_path), f"No Existe {thumbnail_output_path}"
