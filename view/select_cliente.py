#!/usr/bin/env python3
# -*- coding: utf-8
import sys
import os
from tkinter import *
diretorio = os.environ["HOME"]+"/sistema_loja"
sys.path.insert(0, diretorio)
from modelo.banco import Banco
from modelo.cliente import Cliente


class Select_cliente(object):
    def __init__(self, master=None):
        # setando fontes e cores
        self.fonte = ("Liberation Sans", "12")
        self.corfonte = ("#236B8E")
        self.corfundo = ("#FFFFFF")
        # inicializando a tela
        self.frame = Frame(master, bg="#FFFFFF")

        cliente = Cliente()
       # seleciona = cliente.buscaCliente()

        #self.labelNome = cliente.nome.get()

root = Tk()
Select_cliente(root)
root.title("selecionar cliente")
root.mainloop()