
from abc import ABC

class AbstractConverter(ABC):
    @staticmethod
    @abc.abstractmethod
    def to_data(in_data):
        pass

    @staticmethod
    @abc.abstractmethod
    def from_data(in_data):
        pass

class TextConverter(AbstractConverter):
    @staticmethod
    def to_data(in_data):
        return in_data

    @staticmethod
    def from_data(in_data):
        return in_data

mimetypes = {
    'text/plain': TextConverter,
}