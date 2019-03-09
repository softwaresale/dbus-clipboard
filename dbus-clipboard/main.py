#!/usr/bin/env python3

from server import ClipboardServer
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib
from pydbus import SessionBus

if __name__ == "__main__":
    # Get main loop and session bus
    loop = GLib.MainLoop()
    bus = SessionBus()

    # Publish clipboard server to namespace
    bus.publish('net.softwaresale.dbus-clipboard.Clipboard', ClipboardServer())

    # Start
    loop.run()
