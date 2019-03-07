
import cliptypes

class Clip:
    data = None
    def __init__(self, mime, data):
        self._mimetype = mime
        self._data = data

    @property
    def mimetype(self):
        return self._mimetype

    @mimetype.setter
    def mimetype(self, mime):
        if mime not in cliptypes.mimetypes:
            self._mimetype = None
        else:
            self._mimetype = mime

    @property
    def data(self):
        if self.mimetype in cliptypes.mimetypes:
            converter = cliptypes.mimetypes[self.mimetype]
            return converter.from_data(self._data)
        else:
            return None

    @property
    def raw_data(self):
        return self._data

    @data.setter
    def data(self, d):
        if self.mimetype in cliptypes.mimetypes:
            converter = cliptypes.mimetypes[self.mimetype]
            self._data = converter.to_data(d)

class ClipStack(list):
    def __init__(self, inital_objects=None):
        super().__init__(inital_objects)

    def add(self, clip, restrict=None):
        if restrict is not None:
            if clip.mimetype == restrict:
                self.append(clip)
            else:
                pass
        else:
            self.append(clip)

    def add_all(self, clips, restrict=None):
        for clip in clips:
            if restrict is not None:
                if clip.mimetype == restrict:
                    self.append(clip)
            else:
                self.append(clip)

    def find_first(self, mime):
        for clip in reversed(self.list):
            if clip.mimetype == mime:
                return clip
        return None
