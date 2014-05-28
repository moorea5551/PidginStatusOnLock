#!/usr/bin/env python
#coding: utf-8
#vim: set et sw=2

import dbus
import dbus.glib
import os
import subprocess

def screensaver_changed(state):
	try:
		proc = subprocess.Popen(["purple-remote getstatus"], stdout=subprocess.PIPE, shell=True)
		(out, err) = proc.communicate()
		if out == "available\n" and out != 'do not disturb\n':
			os.system("purple-remote 'setstatus?status=away'")
		else:
			os.system("purple-remote 'setstatus?status=available'")
	except:
		print "It's Borked!"

def main():
	import gobject
	gobject.MainLoop().run()

session_bus = dbus.SessionBus()
session_bus.add_signal_receiver(screensaver_changed, signal_name='ActiveChanged', dbus_interface='org.mate.ScreenSaver')
main()
