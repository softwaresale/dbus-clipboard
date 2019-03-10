
from .clip import Clip


class ClipStack(list):
    """
    Stack implementation for the server. Inherits from
    list, so not a whole lot of additional functionality
    is added.
    """
    def __init__(self, inital_objects=None):
        """
        Inherited from list
        """
        if inital_objects is not None:
            super().__init__(inital_objects)

    def add(self, clip, restrict=None):
        """
        Adds a new clip object to the stack.
        :param clip: clip object to be added
        :param restrict: If clip's mimetype is not of restrict, don't allow it (default: None)
        """
        if restrict is not None:
            if clip.mimetype == restrict:
                self.append(clip)
            else:
                pass
        else:
            self.append(clip)

    def add_all(self, clips, restrict=None):
        """
        Adds multiple clips to the stack.
        :param clips: List of clips
        :param restrict: If clip's mimetype is not of restrict, don't allow it (default: None)
        """
        for clip in clips:
            if restrict is not None:
                if clip.mimetype == restrict:
                    self.append(clip)
            else:
                self.append(clip)

    def find_first(self, mime=None):
        """
        Finds the first clip available, does not pop.
        :param mime: find first clip of mimetype. If None given, get first clip (default: None)
        """
        if mime is not None:
            return self[len(self) - 1]
        for clip in reversed(self):
            if clip.mimetype == mime:
                return clip
        return None

    def pop(self, index, mime=None):
        """
        Pops index if mime matches
        :param index: Index to pop from, default last
        """
        if mime is not None:
            if self[index].mimetype == mime:
                return super().pop(index)
            else:
                return None
        else:
            return super().pop(index)
