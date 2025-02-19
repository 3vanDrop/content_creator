from resources.buscar_clips import VideoDownloader

def test_single_download():
    video_downloader = VideoDownloader(debug=True)  # Activar mensajes de depuración en la consola
    found = video_downloader.query(name="stars", count=2)
    print(f"[{len(found)}] - {found}")
    
    assert len(found) == 2, "2 Elementos"