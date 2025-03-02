import time
import os
from pathlib import Path
from tests.base_test import BaseTest
from resources.utils import unzip_file, bulk_move_files

class TestUnzipAndMove(BaseTest):
    def test_unzip(self):
        zip_folder = self.config["Quizes"]["zip_filepath"]
        zip_filename = self.config["Quizes"]["zip_filename"]
        dst_folder = self.config["Quizes"]["video_quiz_pages_folder"]

        unzip_file(os.path.join(zip_folder, zip_filename),
                   destination_folder=dst_folder)

    def test_cleanup_files(self):
        pages_vid_folder = str(Path(self.config["Quizes"]["video_quiz_pages_folder"]))
        audio_path = str(Path(self.config["Quizes"]["audio_to_join"]).parent)
        non_audio_videos = str(Path(self.config["Quizes"]["video_to_join"]).parent)
        final_videos = str(Path(self.config["Quizes"]["video_output_join"]).parent)
        self.clean_up_workspace(pages_vid_folder)
        self.clean_up_workspace(audio_path)
        self.clean_up_workspace(non_audio_videos)

        new_folder = os.path.join(final_videos, f"old.{int(time.time())}")
        os.mkdir(new_folder)

        bulk_move_files(source_folder=final_videos,
                        file_extension="*.mp4",
                        destination_folder=new_folder)
