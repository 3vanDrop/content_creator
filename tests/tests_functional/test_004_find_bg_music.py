from tests.base_test import BaseTest
from resources.find_music import search_open_source_music

class TestFindBackgroundMusic(BaseTest):
    def test_find_bg_music(self):
        files = search_open_source_music(query="instrumental",
                                         time_limit=100)  # seconds
        
        self.logger.info(f"files={files}")

