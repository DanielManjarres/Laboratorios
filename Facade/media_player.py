from typing import List, Optional

# Subsistema: Reproductor de Audio
class AudioPlayer:
    def load_audio(self, file: str) -> None:
        print(f"Cargando archivo de audio: {file}")

    def play(self) -> None:
        print("Reproduciendo audio...")

    def stop(self) -> None:
        print("Deteniendo reproducción de audio")

    def set_volume(self, volume: int) -> None:
        print(f"Estableciendo volumen del audio a {volume}%")

# Subsistema: Reproductor de Video
class VideoPlayer:
    def load_video(self, file: str) -> None:
        print(f"Cargando archivo de video: {file}")

    def play(self) -> None:
        print("Reproduciendo video...")

    def stop(self) -> None:
        print("Deteniendo reproducción de video")

    def set_resolution(self, resolution: str) -> None:
        print(f"Ajustando resolución a {resolution}")

# Subsistema: Subtítulos
class SubtitleManager:
    def load_subtitles(self, file: str) -> None:
        print(f"Cargando archivo de subtítulos: {file}")

    def display(self) -> None:
        print("Mostrando subtítulos")

    def hide(self) -> None:
        print("Ocultando subtítulos")

    def set_language(self, language: str) -> None:
        print(f"Estableciendo idioma de subtítulos a: {language}")

# Subsistema: Gestor de Listas de Reproducción
class PlaylistManager:
    def __init__(self):  # Corregido de _init_ a __init__
        self.playlist: List[str] = []
        self.current_index: int = 0

    def create_playlist(self) -> None:
        self.playlist.clear()
        self.current_index = 0
        print("Lista de reproducción creada")

    def add_to_playlist(self, file: str) -> None:
        self.playlist.append(file)
        print(f"Añadido a la lista de reproducción: {file}")

    def get_next_item(self) -> Optional[str]:
        if not self.playlist:
            return None

        item = self.playlist[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.playlist)
        print(f"Siguiente elemento de la lista: {item}")
        return item

    def display_playlist(self) -> None:
        print("=== Lista de reproducción actual ===")
        for i, item in enumerate(self.playlist):
            prefix = "→ " if (i == self.current_index - 1 or
                              (self.current_index == 0 and i == len(self.playlist) - 1)) else "  "
            print(f"{prefix}{i + 1}. {item}")
        print("===================================")

# Subsistema: Ecualizador (Implementación proporcionada por el usuario)
class Equalizer:
    def __init__(self):  # Corregido de _init_ a __init__
        self.current_mode = "Normal"
        self.available_modes = ["Normal", "Rock", "Pop", "Jazz", "Classical", "Bass Boost"]

    def set_mode(self, mode: str) -> None:
        if mode in self.available_modes:
            self.current_mode = mode
            print(f"Modo de ecualización establecido a: {mode}")
        else:
            print(f"Modo no disponible. Modos disponibles: {', '.join(self.available_modes)}")

    def get_current_mode(self) -> str:
        return self.current_mode

    def list_available_modes(self) -> List[str]:
        print("Modos de ecualización disponibles:")
        for mode in self.available_modes:
            print(f"- {mode}")
        return self.available_modes

# FACHADA (FACADE)
class MediaPlayerFacade:
    def __init__(self):  # Corregido de _init_ a __init__
        self.audio_player = AudioPlayer()
        self.video_player = VideoPlayer()
        self.subtitle_manager = SubtitleManager()
        self.playlist_manager = PlaylistManager()
        self.equalizer = Equalizer()  # Subsistema Equalizer integrado
        self.current_media_type = None

    def _get_file_type(self, file: str) -> str:
        if file.endswith((".mp3", ".wav", ".ogg")):
            return "audio"
        elif file.endswith((".mp4", ".avi", ".mkv")):
            return "video"
        else:
            return "unknown"

    def play_media(self, file: str) -> None:
        print("\n=== INICIANDO REPRODUCCIÓN DE MEDIA ===")
        file_type = self._get_file_type(file)
        self.current_media_type = file_type

        if file_type == "audio":
            self.audio_player.load_audio(file)
            self.audio_player.set_volume(80)
            # Configura modo predeterminado del ecualizador para audio si no está configurado
            if self.equalizer.get_current_mode() == "Normal":
                self.equalizer.set_mode("Normal")
            self.audio_player.play()
        elif file_type == "video":
            self.video_player.load_video(file)
            self.video_player.set_resolution("1080p")
            subtitle_file = file[:file.rfind('.')] + ".srt"
            self.subtitle_manager.load_subtitles(subtitle_file)
            self.subtitle_manager.set_language("Español")
            self.subtitle_manager.display()
            self.video_player.play()
        else:
            print(f"Formato de archivo no soportado: {file}")

    def stop_media(self) -> None:
        print("\n=== DETENIENDO REPRODUCCIÓN ===")

        if self.current_media_type is None:
            print("No hay reproducción activa")
            return

        if self.current_media_type == "audio":
            self.audio_player.stop()
        elif self.current_media_type == "video":
            self.video_player.stop()
            self.subtitle_manager.hide()

        self.current_media_type = None

    def create_playlist(self) -> None:
        self.playlist_manager.create_playlist()

    def add_to_playlist(self, file: str) -> None:
        self.playlist_manager.add_to_playlist(file)

    def play_next(self) -> None:
        next_item = self.playlist_manager.get_next_item()
        if next_item is not None:
            self.play_media(next_item)
        else:
            print("La lista de reproducción está vacía")

    def show_playlist(self) -> None:
        self.playlist_manager.display_playlist()

    def toggle_subtitles(self) -> None:
        if self.current_media_type is not None and self.current_media_type == "video":
            print("Alternando visibilidad de subtítulos")
            self.subtitle_manager.display()  # Simplificado para la demo
        else:
            print("Los subtítulos solo están disponibles durante la reproducción de video")

    def set_volume(self, volume: int) -> None:
        if volume < 0 or volume > 100:
            print("El volumen debe estar entre 0 y 100")
            return
        print(f"Estableciendo volumen a {volume}%")
        self.audio_player.set_volume(volume)

    # Método para configurar el modo del ecualizador (proporcionado por el usuario)
    def set_sound_mode(self, mode: str) -> None:
        print("\n=== CONFIGURANDO ECUALIZADOR ===")
        self.equalizer.set_mode(mode)
        if self.current_media_type is not None:
            print(f"Aplicando modo {mode} a la reproducción actual")
        else:
            print(f"Modo {mode} configurado. Se aplicará en la próxima reproducción")

    # Método para mostrar los modos de sonido disponibles (proporcionado por el usuario)
    def show_sound_modes(self) -> None:
        print("\n=== MODOS DE SONIDO ===")
        self.equalizer.list_available_modes()
        print(f"Modo actual: {self.equalizer.get_current_mode()}")

# Cliente
def main():
    media_player = MediaPlayerFacade()

    # Crear y configurar una lista de reproducción
    media_player.create_playlist()
    media_player.add_to_playlist("cancion1.mp3")
    media_player.add_to_playlist("pelicula.mp4")
    media_player.add_to_playlist("cancion2.mp3")
    media_player.show_playlist()

    # Mostrar y configurar modos de sonido
    media_player.show_sound_modes()
    media_player.set_sound_mode("Rock")

    # Reproducir un archivo específico
    media_player.play_media("documental.mp4")

    # Ajustar volumen
    media_player.set_volume(70)

    # Alternar subtítulos
    media_player.toggle_subtitles()

    # Cambiar modo de sonido durante la reproducción
    media_player.set_sound_mode("Jazz")  # Cambiado a Jazz para variar

    # Detener la reproducción actual
    media_player.stop_media()

    # Reproducir el siguiente elemento de la lista
    media_player.play_next()

if __name__ == "__main__":   
    main()