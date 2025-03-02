from tests.base_test import BaseTest
from resources.utils import read_csv

class TestCSVFileReader(BaseTest):
    def test_csv_reader_single(self):
        quizes = read_csv(self.config["Quizes"]["input_csv"])
        for quiz in quizes:
            self.logger.info(f"len={len(quiz)}, preguntas={quiz}")

    def test_csv_reader_multiple(self):
        quizes = read_csv(self.config["Quizes"]["input_multiple_csv"])
        for quiz in quizes:
            self.logger.info(f"len={len(quiz)}, preguntas={quiz}")
