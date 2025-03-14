from tests.base_test import BaseTest
from resources.upload_youtube import upload_videos_from_folder

import datetime

class TestUploadYouTube(BaseTest):
    def test_upload_video(self):
        video_path = "/Users/karinalizarraga/Desktop/VideosEvan/29-feb-2025/final_videos"

        upload_videos_from_folder(video_path,
                                  tags=["QuizCultural",
                                        "CulturaGeneral",
                                        "PonATuMenteAPrueba",
                                        "ConocimientoGeneral",
                                        "AprendeJugando",
                                        "Trivia",
                                        "DesafíoMental",
                                        "CulturaYEducación",
                                        "JuegosDeConocimiento",
                                        "AprenderNuncaTermina"],
                                  description="#QuizCultural #CulturaGeneral #PonATuMenteAPrueba #ConocimientoGeneral #AprendeJugando #Trivia #DesafíoMental #CulturaYEducación #JuegosDeConocimiento #AprenderNuncaTermina",
                                  custom_title="#Trivia - #Quiz #CulturaGeneral",
                                  schedule_time=datetime.datetime.now() + datetime.timedelta(hours=1),
                                  schedule_every_several_hours=4)
