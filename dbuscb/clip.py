
from .cliptypes import mimetypes


class Clip:
    """
    Object that represents a clipping. Each clipping has a mimetype
    and data.
    """

    def __init__(self, mime, data, is_raw=False):
        """
        Initializes a clipping with type and data
        :param mime: string of clipping's mimetype.
        :param data: pay load to assign to clipping
        :param is_raw: if true, then `data` is raw data. Otherwise, it is an object (default: False)
        """
        # Set mimetype and appropriate converter
        self._mimetype = mime
        if self._mimetype in mimetypes:
            self.converter = mimetypes[self._mimetype]
        else:
            self.converter = None
        
        # If the data is raw, then place simple assignment.
        # If
        if is_raw:
            self._data.fromlist(data)
        else:
            self._data = self.converter.to_data(data)

    @property
    def data(self):
        """
        Returns serialized data as a list of bytes
        :returns: byte list
        """
        return self._data.tolist()

    @data.setter
    def data(self, raw):
        """
        Takes in raw data and converts it into an array
        :param raw: raw byte list
        """
        self._data = raw

    @property
    def mimetype(self):
        """
        Textual mimetype for clipping
        :returns: clip's mimetype as a string
        """
        return self._mimetype

    @mimetype.setter
    def mimetype(self, mime):
        """
        Sets the clips mimetype. It also verifies that the mimetype
        is supported.
        :param mime: string mimetype
        """
        if mime not in mimetypes:
            self._mimetype = None
        else:
            self._mimetype = mime

    @property
    def obj(self):
        """
        Gets the object represented by the data. Because the internal
        data is raw, it needs to be converted to be useful.
        :returns: Initilized object or None
        """
        if self.converter is not None:
            return self.converter.to_obj(self._data)
        else:
            return None

    @obj.setter
    def obj(self, o):
        """
        Serializes an object into raw data.
        :param o: object to be serialized
        """
        if self.converter is not None:
            self._data = self.converter.to_data(o)
        else:
            self._data = None
