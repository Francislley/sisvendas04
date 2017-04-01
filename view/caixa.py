#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from banco import Banco

class Caixa(object):
	"""docstring for Caixa"""
	def __init__(self, saldo): #construtor
		self.__saldo = saldo   #escondendo o atributo
		
	@property
	def saldo(self):
		return self.__saldo
	
if __name__ == "__main__":
	Caixa()

