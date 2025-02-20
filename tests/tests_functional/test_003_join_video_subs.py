from resources.media_join import video_join_subs
from tests.base_test import BaseTest

class TestJoinVideoSubs(BaseTest):
    def test_join_video_subs(self):
        """Join video and subtitles"""
        video_with_audio = self.config["testing_samples"]["video_with_audio"]
        subtitulos = self.config["testing_samples"]["subtitles_srt"]

        video_with_subs = video_join_subs(video_input_path=video_with_audio,
                                          srt_input_path=subtitulos,
                                          output_video="video_with_subs.mp4")

        assert self.file_exists(video_with_subs), "Video with Subs File shall be created"
