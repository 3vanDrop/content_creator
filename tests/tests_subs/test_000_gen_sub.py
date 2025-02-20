from resources.subtitles import generar_subtitulos
from tests.base_test import BaseTest

class TestGenerateSubs(BaseTest):
    def test_generate_subtitules(self):
        """Generate subtitles from video with audio"""
        video_with_audio = self.config["testing_samples"]["video_with_audio"]
        srt_output = generar_subtitulos(video_with_audio)

        assert self.file_exists(srt_output), "SRT File shall be created"
