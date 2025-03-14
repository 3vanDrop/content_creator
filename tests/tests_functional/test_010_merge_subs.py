import os
from resources.subtitles import agregar_subtitulos_a_video, generar_subtitulos
from tests.base_test import BaseTest

class TestGenerateSubs(BaseTest):
    def test_merge_subtitules(self):
        """Merge subtitles to video with audio"""
        video_with_audio = self.config["testing_samples"]["video_with_audio"].replace("\\", "/")
        srt_output = generar_subtitulos(video_with_audio)
        assert self.file_exists(srt_output), "SRT File shall be created"

        agregar_subtitulos_a_video(os.path.abspath(video_with_audio),
                                  srt_output, "output.mp4")

        assert self.file_exists("output.mp4"), "MP4 File shall be created"
