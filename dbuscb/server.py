

from pydbus import SessionBus
from clipstack import ClipStack
from clip import Clip


class ClipboardServer:
    """
    <node>
        <interface name="net.softwaresale.dbus-clipboard.Clipboard">
            <method name="add_clip">
                <arg name="mime" type="s" direction="in" />
                <arg name="data" type="ay" direction="in" />
                <arg name="restrict" type="b" direction="in" />
            </method>
            <method name="first_clip">
                <arg name="mime" type="s" direction="in" />
                <arg name="data" type="ay" direction="out" />
            </method>
            <method name="pop">
                <arg name="mime" type="s" direction="in" />
                <arg name="data" type="ay" direction="out" />
            </method>
        </interface>
    </node>
    """
    def __init__(self):
        self.stack = ClipStack()

    def add_clip(self, mime, data, restrict=None):
        """
        Adds a clip object to clipboard.
        :param
        """
        newclip = Clip(mime, data)
        self.stack.add(newclip, restrict)

    def first_clip(self, mime=None):
        clip = self.stack.find_first(mime)
        if clip is not None:
            # Return serialized form
            return clip.data

    def pop(self, mime):
        return self.stack.pop(len(self.stack) - 1, mime).data
