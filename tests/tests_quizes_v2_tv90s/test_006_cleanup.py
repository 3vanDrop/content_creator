import time
import os
from pathlib import Path
from tests.base_test import BaseTest
from resources.utils import bulk_move_files
from . import CONFIG_YAML_KEY

class TestCleanupWorkspace(BaseTest):
    def test_cleanup_files(self):
        pages_vid_folder = str(Path(self.config[CONFIG_YAML_KEY]["video_quiz_pages_folder"]))
        audio_path = str(Path(self.config[CONFIG_YAML_KEY]["audio_to_join"]).parent)
        non_audio_videos = str(Path(self.config[CONFIG_YAML_KEY]["video_to_join"]).parent)
        final_videos = str(Path(self.config[CONFIG_YAML_KEY]["video_output_join"]).parent)
        self.clean_up_workspace(pages_vid_folder)
        self.clean_up_workspace(audio_path)
        self.clean_up_workspace(non_audio_videos)

        new_folder = os.path.join(final_videos, f"old.{int(time.time())}")
        os.mkdir(new_folder)

        bulk_move_files(source_folder=final_videos,
                        file_extension="*.mp4",
                        destination_folder=new_folder)
