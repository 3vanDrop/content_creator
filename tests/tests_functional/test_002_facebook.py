from tests.base_test import BaseTest
from resources.upload_content import upload_to_facebook
import os


class TestUploadFacebook(BaseTest):
    def test_upload_video(self):
        video_path = os.path.join("/Users/karinalizarraga/Desktop/VideosEvan/23-feb-2025", "La Caída de 'El Alacrán'_ Un Impacto en la Seguridad-VEED.mp4")
        assert self.file_exists(video_path)
        upload_to_facebook(video_path)