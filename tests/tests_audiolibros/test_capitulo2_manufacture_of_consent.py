from resources.subtitles import generar_subtitulos
from tests.base_test import BaseTest

class TestGenerateSubs(BaseTest):

    def test_generate_subtitules_audiolibro(self):
        """Generate subtitles from video with audio"""
        script = [
            "Capítulo 2, La fabricación del consenso",
            "¿Sabías que los medios no solo moldean lo que pensamos, sino también cómo pensamos? En este video, exploraremos el segundo capítulo de 'Manufacture of Consent' de Noam Chomsky y Edward Herman, donde explican cómo la manipulación mediática influye en la opinión pública.",
            
            "La construcción de la opinión pública",
            "Los medios de comunicación no solo informan, sino que también crean la realidad que percibimos. La información que consumimos moldea nuestra forma de entender el mundo y, muchas veces, nuestras decisiones políticas y sociales.",
            
            "Ejemplo de manipulación mediática",
            "Imagina dos protestas: una en un país aliado y otra en un país enemigo. La primera se presenta como un acto de libertad, mientras que la segunda se muestra como un acto de desorden o terrorismo. Esto es un claro ejemplo de cómo los medios manipulan la percepción pública.",
            
            "La repetición como herramienta",
            "Cuando escuchamos una idea repetidamente en diferentes medios, tendemos a aceptarla como verdad. Esto es utilizado para consolidar narrativas específicas y evitar que la audiencia cuestione la información recibida.",
            
            "El papel de los expertos",
            "Muchas veces los medios utilizan a 'expertos' que refuerzan la narrativa dominante. Sin embargo, estos expertos suelen estar alineados con intereses políticos o económicos, limitando así el acceso a opiniones diversas.",

            "Un ejemplo actual es cómo los medios presentan los conflictos internacionales. Dependiendo de los intereses de los países involucrados, la cobertura puede ser totalmente diferente. Las víctimas y los agresores son definidos según la conveniencia de quienes controlan la información.",

            "En conclusión",
            "El segundo capítulo de 'Manufacture of Consent' nos muestra cómo la opinión pública no surge de forma espontánea, sino que es construida estratégicamente. La clave está en desarrollar un pensamiento crítico y cuestionar la información que consumimos. ¿Qué piensas de esto? Déjamelo en los comentarios y comparte este video.",
        ]

        self.logger.info("Creating video with audio...")
        video_with_audio = self.create_video_with_audio(
            keywords=["advertisement", "censorship", "power", "media", "propaganda"],
            video_count=4,
            tts_text=" ".join(script))
        assert self.file_exists(video_with_audio), "Video with Audio shall Exist!"

        self.logger.info("Generating subtitles...")
        srt_output = generar_subtitulos(video_with_audio)
        assert self.file_exists(srt_output), "SRT Subtitles shall Exist!"
