import ffmpeg
import os
from PIL import Image
import subprocess

def resize_image(input_path, output_path, resolution="1080x1920", crop_factor=0.3):
    # Verificar y convertir crop_factor a float si es necesario
    if isinstance(crop_factor, str):
        crop_factor = float(crop_factor)
    
    # Verificar y convertir resolution si es una cadena
    if isinstance(resolution, str):
        try:
            width, height = resolution.split("x")
            resolution = (int(width), int(height))
        except (ValueError, AttributeError):
            raise ValueError("El formato de resolution debe ser 'ancho x alto', por ejemplo: '1080x1920'.")
    
    # Verificar que resolution sea una tupla de dos enteros
    if not isinstance(resolution, (tuple, list)) or len(resolution) != 2:
        raise ValueError("resolution debe ser una tupla de dos enteros (ancho, alto).")
    
    try:
        resolution = (int(resolution[0]), int(resolution[1]))
    except (ValueError, TypeError):
        raise ValueError("Los valores de resolution deben ser números enteros.")
    
    # Abrir la imagen
    img = Image.open(input_path)
    
    # Obtener las dimensiones originales de la imagen
    original_width, original_height = img.size
    
    # Calcular el aspect ratio original
    aspect_ratio = original_width / original_height
    
    # Determinar el aspect ratio de la resolución deseada
    target_aspect_ratio = resolution[0] / resolution[1]
    
    # Ajustar el tamaño de la imagen para minimizar el área negra
    if aspect_ratio > target_aspect_ratio:
        # La imagen es más ancha que la resolución deseada
        new_height = resolution[1]
        new_width = int(new_height * aspect_ratio)
    else:
        # La imagen es más alta que la resolución deseada
        new_width = resolution[0]
        new_height = int(new_width / aspect_ratio)
    
    # Redimensionar la imagen para que sea más grande que la resolución deseada
    resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    # Calcular el área de recorte basada en el crop_factor
    crop_width = int(new_width * crop_factor)
    crop_height = int(new_height * crop_factor)
    
    # Coordenadas para el recorte (centro de la imagen)
    left = (new_width - resolution[0]) // 2
    top = (new_height - resolution[1]) // 2
    right = left + resolution[0]
    bottom = top + resolution[1]
    
    # Asegurarse de que el recorte no exceda las dimensiones de la imagen
    left = max(0, left)
    top = max(0, top)
    right = min(new_width, right)
    bottom = min(new_height, bottom)
    
    # Recortar la imagen
    cropped_img = resized_img.crop((left, top, right, bottom))
    
    # Guardar la imagen resultante
    cropped_img.save(output_path)

def resize_image(image_path, output_path, resolution):
    """Escala la imagen a la resolución especificada."""
    (
        ffmpeg
        .input(image_path)
        .filter("scale", resolution.split("x")[0], resolution.split("x")[1], force_original_aspect_ratio="decrease")
        .output(output_path)
        .run(overwrite_output=True)
    )

def generate_video_from_image(image_path, duration_ms, effect, output_path, resolution="1080x1920"):
    duration = duration_ms / 1000  # Convertir duración a segundos
    frames = int(duration * 30)  # 30 FPS
    resized_image = "resized_image.jpg"

    # Escalar la imagen antes de procesarla con FFmpeg
    resize_image(image_path, resized_image, resolution)

    # Configuración del zoom
    if effect == "zoom_in":
        zoom_expr = "min(zoom+0.01,1.5)"  # Zoom in: aumenta el zoom gradualmente
    elif effect == "zoom_out":
        zoom_expr = "max(zoom-0.01,0.5)"  # Zoom out: disminuye el zoom gradualmente (valor mínimo 0.5)
    else:
        raise ValueError("Efecto no válido. Usa: zoom_in o zoom_out")

    output_temp = "temp.mp4"

    (
        ffmpeg
        .input(resized_image, loop=1, framerate=30)  # Imagen escalada como entrada
        .filter("zoompan", z=zoom_expr, d=frames, x="iw/2-(iw/zoom)/2", y="ih/2-(ih/zoom)/2", s=f"{resolution}")  # Aplicar zoom
        .output(output_temp, vcodec="libx264", pix_fmt="yuv420p", crf=23, preset="slow", t=duration)
        .run(overwrite_output=True)
    )

    os.rename(output_temp, output_path)
    print(f"Video generado con éxito: {output_path}")

    return os.path.abspath(generar_video_con_correcion(output_path,
                                                       output_video=output_path.replace(".mp4", "_final.mp4")))

def generar_video_con_correcion(input_video, output_video):
    # Comando FFmpeg para corregir la resolución y el SAR
    comando_corregir_resolucion = [
        'ffmpeg',
        '-i', input_video, 
        '-c:v', 'libx264', 
        '-vf', 'setsar=1',  # Corregir el SAR a 1
        '-s', '1080x1920',  # Establecer la resolución 1080x1920
        '-crf', '23', 
        '-preset', 'fast',
        output_video
    ]
    
    try:
        # Ejecutar la corrección de resolución
        subprocess.run(comando_corregir_resolucion, check=True)
        print(f"Video corregido y guardado en: {output_video}")
    except subprocess.CalledProcessError as e:
        print(f"Ocurrió un error durante la corrección de resolución: {e}")
        return
    
    # Aquí puedes agregar las demás funcionalidades que tu función ya realiza, 
    # como la creación del video o cualquier otro proceso adicional que necesites.
    print("Video generado con éxito.")
    
    # Si necesitas devolver algún resultado (como el nombre del archivo generado):
    return output_video
