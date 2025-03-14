from tests.base_test import BaseTest
from resources.upload_youtube import upload_videos_from_folder

import datetime
import random

class TestUploadYouTube(BaseTest):
    TAGS = [
        "TestDeInglés", "NivelDeInglés", "AprendeInglés", "InglésParaTodos",
        "PruebaTuInglés", "ExamenDeInglés", "EnglishTest", "DesafíoDeInglés",
        "MejoraTuInglés", "InglésFácil", "GramáticaInglés", "VocabularioInglés",
        "ListeningInglés", "ReadingInglés", "SpeakingInglés", "WritingInglés",
        "EjerciciosDeInglés", "AprenderInglésJugando", "QuizDeInglés",
        "TestDeVocabulario", "ComprensiónLectora", "InglésBásico", "InglésIntermedio",
        "InglésAvanzado", "CertificaciónInglés", "PreparaciónTOEFL", "PreparaciónIELTS",
        "TOEIC", "PruebaDeIdiomas", "ExamenDeIdiomas", "FluidezEnInglés",
        "TrucosParaAprenderInglés", "ConsejosDeInglés", "TestDeListening",
        "TestDeReading", "TestDeWriting", "TestDeSpeaking", "Idiomas",
        "EducaciónEnInglés", "AprendizajeDeIdiomas", "HabilidadesLingüísticas",
        "ExpresionesEnInglés", "VerbosEnInglés", "PronunciaciónEnInglés",
        "ComprensiónAuditiva", "EjerciciosInteractivos", "DesafíoLingüístico",
        "InglésParaViajar", "InglésParaNegocios", "InglésAcadémico"
    ]
    descripciones = [
        "¿Qué nivel de inglés tienes? ¡Descúbrelo ahora!", 
        "Pon a prueba tu inglés con este test rápido",
        "¿Te atreves a este desafío de inglés?", 
        "¡Solo el 10% obtiene el nivel más alto! ¿Podrás tú?", 
        "Averigua tu nivel de inglés en solo 2 minutos", 
        "¿Eres un experto en inglés? ¡Compruébalo!", 
        "Un reto de inglés que no querrás perderte", 
        "¿Listo para demostrar tu dominio del inglés?", 
        "Demuestra qué tan bien hablas inglés", 
        "¡Atrévete y sorpréndete con tu nivel!", 
        "¿Puedes responder correctamente en inglés? ¡Inténtalo!", 
        "Un test que pondrá a prueba tu gramática y vocabulario", 
        "¿Crees que dominas el inglés? ¡Compruébalo!", 
        "¡Solo para los que realmente saben inglés!", 
        "¿Podrás alcanzar el nivel más alto? ¡Descúbrelo!", 
        "Un test de inglés que no te puedes perder", 
        "¿Eres parte del 5% que obtiene nivel avanzado?", 
        "¡Demuestra tu talento en inglés en solo 3 minutos!", 
        "¿Listo para un desafío sorprendente en inglés?", 
        "¡Atrévete a descubrir qué nivel de inglés tienes!"
    ]
    random_tags = random.sample(TAGS, 10)
    descripcion = random.choice(descripciones)

    def test_upload_video(self):
        video_path = "/Users/karinalizarraga/Desktop/Workspace/Quizes_v2_Ingles/final_videos"

        # mexico time is -3. So if 7:00am is given, it will do 4:00am
        # datetime.datetime(2025, 3, 3, 15, 26, 40)
        # datetime.datetime.now()
        # datetime.timedelta(hours=1)
        fecha_de_inicio = datetime.datetime(2025, 3, 12, 8)
        tiempo_entre_videos = 2  # horas

        upload_videos_from_folder(video_path,
                                  tags=[self.random_tags],
                                  description=(f"{self.descripcion}"
                                               " - #"+" #".join(self.random_tags)),
                                  custom_title="#DesafíoDeInglés - #Test #AprendeJugando",
                                  schedule_time=fecha_de_inicio,
                                  schedule_every_several_hours=tiempo_entre_videos)
