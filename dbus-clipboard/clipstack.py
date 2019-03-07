
class Clipping:

    self.data = None

    def __init__(self, mime, data):
        self._mimetype = mime
        self.data = data

    @property
    def mimetype(self):
        pass

class ClipStack(object):

    def __init__(self, inital_objects=None, size=None):

        # Set size if given
        if size is not None:
            self.list = [size]
        else:
            self.list = list()

        # Add any starter objects if necessary
        if inital_objects is not None:
            for obj in inital_objects:
                self.list.append(obj)
