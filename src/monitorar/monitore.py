import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileMonitor(FileSystemEventHandler):
    modified_file = None
    event_occurred = threading.Event()
    observer = None

    @staticmethod
    def on_modified(event):
        if not event.is_directory:
            FileMonitor.modified_file = event.src_path
            FileMonitor.event_occurred.set()  # Sinaliza que o evento ocorreu

    @staticmethod
    def monitorar_diretorio(diretorio):
        """Monitora o diretório especificado e retorna o caminho completo do arquivo modificado.

        Args:
            diretorio (str): O caminho do diretório a ser monitorado.

        Returns:
            str: O caminho completo do arquivo modificado, ou None se nenhum arquivo foi modificado.
        """
        event_handler = FileMonitor()
        FileMonitor.observer = Observer()
        FileMonitor.observer.schedule(event_handler, diretorio, recursive=True)
        FileMonitor.observer.start()

        # Aguarda até que um arquivo seja modificado
        FileMonitor.event_occurred.wait()
        FileMonitor.observer.stop()
        FileMonitor.observer.join()

        return FileMonitor.modified_file  # Retorna o arquivo modificado

    @staticmethod
    def reset_monitoring():
        """Reseta e desliga o monitoramento."""
        if FileMonitor.observer:
            FileMonitor.observer.stop()
            FileMonitor.observer.join()
            FileMonitor.event_occurred.clear()
            FileMonitor.modified_file = None
            FileMonitor.observer = None
