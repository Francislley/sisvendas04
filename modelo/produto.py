#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os

from modelo.banco import Banco


class Produto(object):
    def __init__(self, codigoProduto="", nomeProduto="", descricao="",
                 precoCompra=0, precoVenda=0):

        self.codigoProduto = codigoProduto
        self.nomeProduto = nomeProduto
        self.descricao = descricao
        self.precoCompra = precoCompra
        self.precoVenda = precoVenda
        self.pesquisaProduto()

    def insertProduto(self, codigoProduto="", nomeProduto="",
                      descricao="", precoCompra=0, precoVenda=0):
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
            return "Produto já cadastrado, \
                    por favor verifique se o nome está correto!"
        else:
            try:
                cursor.execute("insert into tb_produto (codigoProduto,\
                                nomeProduto,descricao,precoCompra,\
                                precoVenda) values('" + codigoProduto +
                               "', '" + nomeProduto +
                               "','" + descricao + "', '" +
                               precoCompra + "," + precoVenda + ")")
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
