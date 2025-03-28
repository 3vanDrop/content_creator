from tests.base_test import BaseTest
from resources.upload_youtube import upload_videos_from_folder_v3
from . import CONFIG_YAML_KEY

import datetime
import random
import os

class TestUploadYouTube(BaseTest):
    TAGS = [
        "QuizCultural", "CulturaGeneral", "PonATuMenteAPrueba",
        "ConocimientoGeneral", "AprendeJugando", "Trivia", "DesafíoMental",
        "CulturaYEducación", "JuegosDeConocimiento", "AprenderNuncaTermina",
        "QuizDeCultura", "CulturaGeneral", "Geografía", "HistoriaUniversal", "CineYMás", 
        "PonATuMenteAPrueba", "TriviaCultural", "AprendeJugando", "ConocimientoGeneral", 
        "DesafíoMental", "JuegosDeSaber", "EducaciónDivertida", "AprenderNuncaTermina", 
        "DatosCuriosos", "SabíasQué", "CuriosidadesHistóricas", "GeografíaMundial", 
        "CulturaPop", "CineClásico", "HistoriaAntigua", "CulturaYEducación", 
        "TriviaGeográfica", "HistoriaDelCine", "PreguntasYRespuestas", "CulturaGlobal", 
        "MundoDeSaber", "ExploraElMundo", "CulturaYArte", "HistoriaModerna", 
        "GeografíaCuriosa", "CineInternacional", "CulturaYEntretenimiento", 
        "AprendizajeContinuo", "TriviaHistórica", "CulturaYConocimiento", 
        "GeografíaFascinante", "CineDeOro", "HistoriaDeAmérica", "CulturaYActualidad", 
        "TriviaDeCine", "SabiduríaPopular", "CulturaYCuriosidades", "GeografíaYMapas", 
        "HistoriaDeEuropa", "CineYTelevisión", "CulturaYSaber", "TriviaDeHistoria", 
        "GeografíaYClima", "CineIndependiente", "HistoriaDeAsia", "CulturaYFilosofía", 
        "TriviaDeArte", "CineDeCulto",
        "CulturaYLiteratura", "TriviaDeMúsica", "GeografíaYPaisajes", "CineDocumental", 
        "HistoriaDeOceanía", "CulturaYCiencia", "TriviaDeDeportes", "GeografíaYCapitales", 
        "CineDeAcción", "HistoriaDeLatinoamérica", "CulturaYTecnología", "TriviaDeCiencia", 
        "GeografíaYRíos", "CineDeTerror", "HistoriaDeMéxico", "CulturaYModa", 
        "TriviaDeLiteratura", "GeografíaYMontañas", "CineDeComedia", "HistoriaDeEspaña", 
        "CulturaYGastronomía", "TriviaDeFamosos", "GeografíaYPaíses", "CineDeDrama", 
        "HistoriaDeEstadosUnidos", "CulturaYViajes", "TriviaDeSeries", "GeografíaYClimas", 
        "CineDeAnimación", "HistoriaDeRusia", "CulturaYDeportes", "TriviaDeVideojuegos", 
        "GeografíaYOcéanos", "CineDeSuspenso", "HistoriaDeChina", "CulturaYArquitectura", 
        "TriviaDeArteModerno", "GeografíaYFronteras", "CineDeFantasía",
        "CulturaYFotografía", "TriviaDeCulturaPop", "GeografíaYContinentes", "CineDeRomance"
    ]
    descripciones = [
        "¿Eres un genio? ¡Demuéstralo!", "Pon a prueba tu conocimiento",
        "¿Te atreves a este desafío?", "¡Solo el 10% lo logra! ¿Podrás tú?",
        "Descubre cuánto sabes en 2 minutos", "¿Eres un experto? ¡Compruébalo!",
        "Un reto que no querrás perderte", "¿Listo para superar este reto?",
        "Demuestra que eres el mejor", "¡Atrévete y sorpréndete!",
        "¿Eres capaz de resolverlo? ¡Inténtalo!", "Un desafío que pondrá a prueba tu mente",
        "¿Crees que lo sabes todo? ¡Compruébalo!", "¡Solo para mentes curiosas!",
        "¿Te atreves a superar este reto?", "Un test que no te puedes perder",
        "¿Eres parte del 5% que lo logra?", "¡Demuestra tu talento en solo 3 minutos!",
        "¿Listo para un desafío sorprendente?", "¡Atrévete a descubrir cuánto sabes!"
    ]
    random_tags = lambda: random.sample(TestUploadYouTube.TAGS, 10)
    descripcion = lambda: (f"{random.choice(TestUploadYouTube.descripciones)}"
                                " - #"+" #".join(TestUploadYouTube.random_tags()))

    def test_upload_video(self):
        video_path = os.path.dirname(self.config[CONFIG_YAML_KEY]["final_videos"])

        # mexico time is -3. So if 7:00am is given, it will do 4:00am
        # datetime.datetime(2025, 3, 3, 15, 26, 40)
        # datetime.datetime.now()
        # datetime.timedelta(hours=1)
        fecha_de_inicio = datetime.datetime(2025, 3, 17, 16)
        tiempo_entre_videos = 24  # horas

        upload_videos_from_folder_v3(video_path,
                                     tags=TestUploadYouTube.random_tags,
                                     description=TestUploadYouTube.descripcion,
                                     custom_title="#Trivia - #Quiz #CulturaGeneral",
                                     schedule_time=fecha_de_inicio,
                                     schedule_every_several_hours=tiempo_entre_videos)
