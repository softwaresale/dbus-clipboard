
from pydbus import SessionBus
from clipstack import ClipStack, Clip

class ClipboardServer:

    def __init__(self):
        self.stack = ClipStack()

    def add_clip(self, mime, data, restrict=None):
        newclip = Clip(mime, data)
        self.stack.add(newclip, restrict)

    def first_clip(self, mime=None):
        if mime is not None:
            for clip in self.stack:
                if clip.mimetype == mime:
                    return clip
        else:
            return self.stack.pop()