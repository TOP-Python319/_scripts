from abc import ABC, abstractmethod
import os


# Интерфейс для работы с файлами и папками
class IFileSystemObject(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_size(self):
        pass


# Конкретная реализация интерфейса IFileSystemObject для файлов
class File(IFileSystemObject):
    def __init__(self, filename):
        self._filename = filename

    def get_name(self):
        return os.path.basename(self._filename)

    def get_size(self):
        return os.path.getsize(self._filename)


# Конкретная реализация интерфейса IFileSystemObject для папок
class Directory(IFileSystemObject):
    def __init__(self, directoryname):
        self._directoryname = directoryname
        self._objects = []
        for obj in os.scandir(self._directoryname):
            if obj.is_file():
                self._objects.append(File(obj.path))
            elif obj.is_dir():
                self._objects.append(Directory(obj.path))

    def get_name(self):
        return os.path.basename(self._directoryname)

    def get_size(self):
        return sum([obj.get_size() for obj in self._objects])


# Пример использования
if __name__ == "__main__":
    directory = Directory("/home/maks/Work/top-academy")
    print(f"Directory '{directory.get_name()}' size={directory.get_size()}")
