import time
import os
from pathlib import Path
from tests.base_test import BaseTest
from resources.utils import unzip_file, bulk_move_files
from resources.media_join import merge_media

class TestMergeMedia(BaseTest):
    def test_merge_audio_video(self):
        workspace_path = self.config["BabyNames"]["workspace"]
        audio_track = os.path.join(self.config["BabyNames"]["songs"],
                                   "track_3.mp3")
        video_track = "/Users/karinalizarraga/Desktop/Workspace/BabyNames_v1/boy_names/boy_names_template_1/video_audio_joined/1741127478_AudioVideoJoined.mp4"

        assert self.file_exists(audio_track)
        assert self.file_exists(video_track)

        merge_media(video_track, audio_track,
                    outputfile="MyOutputMergedAudioVideo.mp4")
