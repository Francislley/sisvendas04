#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import os
import sys
# determinando em qual diretorio se encontra a pasta do sistema para inclusão de modulos
diretorio = os.environ["HOME"] + "/sistema_loja"
sys.path.insert(0, diretorio)

class Banco():

	def __init__(self):
		self.conexao = sqlite3.connect('loja.db')
	
		
	

if __name__ == "__main__":
	Banco()
