#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import mysql.connector as db
import sqlite3
import os
import sys
diretorio = os.environ["HOME"] + "/sistema_loja"
sys.path.insert(0, diretorio)
from data.banco import Banco


class Banco():

    def __init__(self):
        self.conexao = sqlite3.connect(diretorio + '/data/loja.db')
        self.createTableUsuario()
        self.createTableProduto()
        self.createTableCliente()

    def createTableUsuario(self):
        self.conex = self.conexao.cursor()
        #self.conex.executeself.conex.execute("""create database if not exists loja; use loja;""")

        self.conex.execute("""create table if not exists usuario (
			idusuario integer primary key autoincrement ,
			login text,senha text)""")
        self.conexao.commit()
        self.conex.close()

    def createTableProduto(self):
        self.conex = self.conexao.cursor()

        self.conex.execute("""create table if not exists tb_produto (
			id_produto integer PRIMARY KEY AUTOINCREMENT,
			codigoProduto text NOT NULL,
			nomeProduto text NOT NULL,
			descricao text,
			precoCompra real,
			precoVenda real)""")
        self.conexao.commit()
        self.conex.close()

    def createTableCliente(self):
        self.conex = self.conexao.cursor()

        self.conex.execute("""create table if not exists tb_cliente (
			idCliente integer PRIMARY KEY AUTOINCREMENT,
			nome text NOT NULL,
			cpf text,
			endereco text,
			telefone text
			email text
			dt_nascimento text
			limite real)""")
        self.conexao.commit()
        self.conex.close()

    def insertProduto(self, codigoProduto="", nomeProduto="", descricao="", precoCompra="", precoVenda=""):
        banco = Banco()
        formato = ''
        nome = nomeProduto.split()
        for i in nome:
            formato = formato + ' ' + i

        nomeProduto = formato.upper()
        cursor = banco.conexao.cursor()
        sql = (
            "SELECT nomeProduto FROM tb_produto where nomeProduto = '" + nomeProduto + "'")
        cursor = banco.conexao.cursor()
        cursor.execute(sql)
        verifica = cursor.fetchone()
        if verifica:
            return "Produto já cadastrado, por favor verifique se o nome está correto!"
        else:
            try:
                cursor.execute("insert into tb_produto (codigoProduto,nomeProduto,descricao,precoCompra,\
						   precoVenda) values('" + codigoProduto + "', '" + nomeProduto + "','" + descricao + "', '" + precoCompra + "',\
				'" + precoVenda + "')")
                banco.conexao.commit()
                return "produto cadastrado com sucesso"

            except ValueError as err:
                return ("Erro ao inserir produto! Erro: " + err)

    def pesquisaProduto(self):
        banco = Banco()
        # cria um dicionario vazio para recebe nome e preço dos produtos da
        # tabela
        produtoPreco = {}
        nomeProduto = ''
        precoVenda = ''
        cursor = banco.conexao.cursor()

        cursor.execute("select nomeProduto, precoVenda from tb_produto")
        lista = cursor.fetchall()

        return lista
        print (lista)

Banco()
