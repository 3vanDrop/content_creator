import os
from resources.media_join import video_join
from resources.utils import read_csv, unzip_file
from tests.base_test import BaseTest


class TestTTSAudio(BaseTest):

    def test_join_quiz_video(self):
        total_files_per_quiz = 20
        total_quizes = 10
        total_pages = total_files_per_quiz * total_quizes

        self._unzip_pages()

        video_counter = 0
        for page in range(1, total_pages+1, total_files_per_quiz):
            self._join_quiz_pages(start_page=page,
                                  files_per_quiz=total_files_per_quiz,
                                  video_quiz_count=video_counter)
            video_counter += 1
            
    def _join_quiz_pages(self, start_page, files_per_quiz, video_quiz_count):
        self.logger.info(f"Creating Video Quiz #{video_quiz_count}")
        video_path = lambda x: self.config["Quizes"]["video_to_join"].replace("*", str(x))
        pages_path = lambda x: self.config["Quizes"]["video_quiz_pages"].replace("*", str(x))
        list_of_videos = list()
        for i in range(start_page, start_page+files_per_quiz):
            self.logger.info(f"== Video Quiz #{video_quiz_count} - Page {i}")
            list_of_videos.append(pages_path(i))
        
        video_join(*list_of_videos, output_resolution="1080x1920",
                   output_path=video_path(video_quiz_count))
        self.logger.info(f"** Completed Video Quiz #{video_quiz_count} **")

        assert self.file_exists(video_path(video_quiz_count))

    def _unzip_pages(self):
        zip_folder = self.config["Quizes"]["zip_filepath"]
        zip_filename = self.config["Quizes"]["zip_filename"]
        dst_folder = self.config["Quizes"]["video_quiz_pages_folder"]

        unzip_file(os.path.join(zip_folder, zip_filename),
                   destination_folder=dst_folder)