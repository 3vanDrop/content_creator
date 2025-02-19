import os
import pathlib
from resources.subtitles import generar_subtitulos
from tests.base_video_assemble import BaseVideoAssemble

class TestGenerateSubs(BaseVideoAssemble):

    def test_generate_subtitules(self):
        """Generate subtitles from video with audio"""
        video_with_audio = self.create_video_with_audio()
        srt_output = generar_subtitulos(video_with_audio)

        assert pathlib.Path(srt_output).exists()

