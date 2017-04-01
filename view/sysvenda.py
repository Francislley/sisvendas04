#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, os
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, Gio

diretorio = os.environ["HOME"] + "/sistema_loja"
sys.path.insert(0, diretorio)

class Venda(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title= "Sistema Vendas")
        self.set_border_width(10)

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.add(Gtk.TextView())

win = Venda()
win.connect("delete_event", Gtk.main_quit)
win.show_all()
Gtk.main()