from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path


class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        """Write a message to the logger output."""


class FileLogger(Logger):
    def __init__(self, log_path: str | Path = "activity_log.txt"):
        self.log_path = Path(log_path)

    def log(self, message: str) -> None:
        current_time = datetime.now()

        with self.log_path.open("a", encoding="utf-8") as file:
            timestamp = current_time.strftime("%d-%m-%y %H:%M")
            file.write(f"[{timestamp}]\n")
            file.write(f"{message}\n\n")


def log_activity(message: str) -> None:
    FileLogger().log(message)


def log_activity(message: str) -> None:
    log_activity(message)