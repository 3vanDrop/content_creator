from resources.calendario import agregar_eventos_a_calendario
from tests.base_test import BaseTest
import time
from datetime import datetime, timedelta

class TestCalendario(BaseTest):
    def test_calendario(self):
        for i in range(5):
            agregar_eventos_a_calendario(
                titulo="Test Ingles",
                descripcion="Video Test Ingles scheduled.",
                lugar="YouTube - BrainHub Channel",
                inicio=datetime(2025, 3, 10, 9, 4)
            )