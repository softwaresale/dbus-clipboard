
from abc import ABC
from abc import abstractmethod
import array


class AbstractConverter(ABC):
    """
    Abstract base class that outlines functionality for converting
    objects to supported clipboard data and vice versa. Each supported
    mimetype should have a corresponding converter.
    """
    @staticmethod
    @abstractmethod
    def to_data(obj):
        """
        Static Method to convert an object into raw data
        :param obj: Object to be converted
        :returns: Transformed raw data
        :raises TypeError: If obj is invalid
        """
        pass

    @staticmethod
    @abstractmethod
    def to_object(data):
        """
        Static Method to convert raw data into an object
        :param data: Data to be converted
        :returns: Transformed object
        """
        pass


class TextConverter(AbstractConverter):
    """
    Converts plain text into serializable data. This simply passes the data through
    :param obj: Text object to be serialized
    :returns: Raw data
    :throws TypeError: `obj` is not of type string
    """
    @staticmethod
    def to_data(obj):
        if isinstance(obj, str):
            barray = array.array('b')
            for b in bytes(obj, 'utf-8'):
                barray.append(b)
            return barray
        else:
            raise TypeError('Obj is not of type string')

    @staticmethod
    def to_object(arr):
        """
        Converts data into plain text.
        :param data: Python array of bytes to be deserialized
        :returns: String object
        """
        return arr.tostring()


mimetypes = {
    'text/plain': TextConverter,
}
