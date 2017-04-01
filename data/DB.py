#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


class Banco(object):
	def __init__(self):
		try:
			con = MongoClient(host="localhost", port=27017)
		except ConnectionFailure as e:
			sys.stderr.write("Não foi possível conectar ao banco de dados erro: %s" % e)
			sys.exit(1)

		#obtendo o BD
		DBMG = con["loja"]
		#assert DBMG.connection == con
		print ("Conectado ao banco de dados com sucesso")

Banco()
