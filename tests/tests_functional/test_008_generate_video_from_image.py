from resources.generar_video import generate_video_from_image
from tests.base_test import BaseTest

class TestGenerateVideo(BaseTest):
    def test_video_from_image(self):
        img_src = "/Users/karinalizarraga/Desktop/Workspace/Dogs_v1/AXDZZNZ1dgRXOTRT-generated_image.jpg"
    
        output_video = generate_video_from_image(img_src,
                                                 duration_ms=10000,
                                                 effect="zoom_in",
                                                 output_path="TestVideoFromImage.mp4")

        assert self.file_exists(output_video)