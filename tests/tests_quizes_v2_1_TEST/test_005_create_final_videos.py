from resources.generar_voz import generar_voz as edgetts_generar_voz
from resources.utils import get_random_file_path, bulk_move_files_from_list
from resources.media_join import video_join
from resources.utils import read_csv
from tests.base_test import BaseTest
import time
from . import CONFIG_YAML_KEY, TOTAL_QUIZES
import random
import os


class TestJoinClipsVideoAudio(BaseTest):
    how_many_clips_per_video = 3 # 15 seconds per video. 3 + 1 ending
    how_many_videos_to_create = 100

    outro_number = lambda self: random.choice(["1", "2"])
    outro_inciso = lambda self: random.choice(["a", "b", "c"])

    def test_join_clips_video(self):
        total_quizes = TOTAL_QUIZES #10
        already_used_clips_folder = self.config[CONFIG_YAML_KEY]["already_used_clips"]

        already_used_clips_ultima_folder = os.path.join(os.path.dirname(self.config[CONFIG_YAML_KEY]["ultima_pregunta"]), "already_used")
        outro_path = lambda: self.config[CONFIG_YAML_KEY]["outro_video"].replace("#", self.outro_number()).replace("*", self.outro_inciso())
        thumbnail_path = lambda: get_random_file_path(self.config[CONFIG_YAML_KEY]["thumbnails"])
        pick_random_clip = lambda: get_random_file_path(os.path.dirname(self.config[CONFIG_YAML_KEY]["video_output_join"]))
        pick_random_ultimo_clip = lambda: get_random_file_path(os.path.dirname(self.config[CONFIG_YAML_KEY]["ultima_pregunta"]))
        preguntas_num = self.how_many_clips_per_video + 1
        dst_path = lambda x: self.config[CONFIG_YAML_KEY]["final_videos"].replace(".mp4", f"_#{preguntas_num}_{x}.mp4")

        for i in range(self.how_many_videos_to_create):
            timestamp = str(time.time()).replace(".", "_")  # Make them unique
            self.logger.info(f"Joining FinalVideo {i}...")
            outro = outro_path()
            thumbnail = thumbnail_path()
            ultima_pregunta = pick_random_ultimo_clip()
            video_clips = []
            for i in range(self.how_many_clips_per_video):
                video_clips.append(pick_random_clip())
            assert len(video_clips) == self.how_many_clips_per_video, f"Debe haber al menos {self.how_many_clips_per_video} para poder armar un nuevo video."
            output_video_path = dst_path(timestamp)
            self.logger.info(f"outro={outro}, thumbnail={thumbnail}, video_clips={video_clips}, output_video_path={output_video_path}, ultima_pregunta={ultima_pregunta}")
            
            final_video_clips = [thumbnail] + video_clips + [ultima_pregunta, outro]
            video_join(*final_video_clips,
                       output_resolution="1080x1920",
                       output_path=output_video_path)
            assert self.file_exists(output_video_path), f"Expecting output_video_path={output_video_path} to be created!"
            bulk_move_files_from_list(video_clips, destination_folder=already_used_clips_folder)
            bulk_move_files_from_list([ultima_pregunta], destination_folder=already_used_clips_ultima_folder)