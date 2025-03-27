import os
from resources.media_join import video_join_old
from resources.utils import read_csv, unzip_file, get_random_file_path
from tests.base_test import BaseTest
from . import CONFIG_YAML_KEY, TOTAL_QUIZES
import shutil


class TestJoinQuizPages(BaseTest):

    def test_join_quiz_video(self):
        total_files_per_quiz = 1
        total_quizes = TOTAL_QUIZES
        total_pages = total_files_per_quiz * total_quizes

        for inciso in ["a", "b", "c", "d"]:
            video_joined_folder = os.path.dirname(self.config[CONFIG_YAML_KEY]["video_to_join"].replace("*", inciso))
            self.clean_up_workspace(video_joined_folder)
            self._unzip_pages(inciso)
            video_counter = 0
            for page in range(1, total_pages+1, total_files_per_quiz):
                try:
                    self._join_quiz_pages(start_page=page,
                                          files_per_quiz=total_files_per_quiz,
                                          video_quiz_count=video_counter,
                                          inciso=inciso,
                                          siguiente=True)
                except TypeError:
                    break  # move to next "inciso"
                video_counter += 1
            
    def _join_quiz_pages(self, start_page, files_per_quiz, video_quiz_count, inciso,
                         siguiente=True):
        self.logger.info(f"Creating Video Quiz #{video_quiz_count} - {inciso}")
        video_path = lambda x: self.config[CONFIG_YAML_KEY]["video_to_join"].replace("#", str(x)).replace("*", inciso)
        pages_path = lambda x: self.config[CONFIG_YAML_KEY]["video_quiz_pages"].replace("#", str(x)).replace("*", inciso)
        sig_video = lambda: get_random_file_path(self.config[CONFIG_YAML_KEY]["siguientes_folder"])  # Fixed video

        self.logger.info(f"== Video Quiz #{video_quiz_count} - Page {start_page}| Inciso {inciso}")
        if siguiente:
            list_of_videos = list()
            list_of_videos.append(pages_path(start_page))
            list_of_videos.append(sig_video())
            video_join_old(*list_of_videos, output_resolution="1080x1920",
                           output_path=video_path(video_quiz_count))
        else:
            self.logger.info("Only one video")
            shutil.copy(src=pages_path(start_page),
                        dst=video_path(video_quiz_count))
        self.logger.info(f"** Completed Video Quiz #{video_quiz_count} | Inciso {inciso}**")

        assert self.file_exists(video_path(video_quiz_count))

    def _unzip_pages(self, inciso):
        zip_folder = self.config[CONFIG_YAML_KEY]["zip_filepath"].replace("*", inciso)
        zip_filename = self.config[CONFIG_YAML_KEY]["zip_filename"]
        dst_folder = self.config[CONFIG_YAML_KEY]["video_quiz_pages_folder"].replace("*", inciso)

        # Removing existing page files
        self.clean_up_workspace(dst_folder)
        unzip_file(os.path.join(zip_folder, zip_filename),
                   destination_folder=dst_folder)