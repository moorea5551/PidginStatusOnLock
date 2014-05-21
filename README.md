PidginStatusOnLock
==================

Sets your pidgin status to away when the screen is locked and available when it's unlocked.  Currently works for Mate and will work for others with a simple config change.

##Usage
To use this script, run `python onLockUnlock.py` at startup or from your console.
If you're not using Mate as your window manager, the dbus_interface will have to be changed at the bottom of the script to the interface name for your particular screensaver.  For example, if you're using gnome screensaver, it's a simple change from `org.mate.ScreenSaver` to `org.gnome.ScreenSaver`.
