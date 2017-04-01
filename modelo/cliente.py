#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
diretorio = os.environ["HOME"] + "/.sistema_loja"
sys.path.insert(0, diretorio)

#from modelo.banco import Banco
from data.DB import Banco



class Cliente(object):
    def __int__(self, nomeCli="", cpf="", telefone="",
                endereco="", email="", nascimento="", limite=""):
        banco = Banco()
        self.cursor = banco.conexao.cursor()
        self.nomeCli = nomeCli
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.email = email
        self.nascimento = nascimento
        self.limite = limite

    def limite(self, limite):
        self.__limite = limite

    def buscaCliente(self, nomeCli):
        banco = Banco()
        self.cursor = banco.conexao.cursor()
        self.cursor.execute("select nome, cpf, endereco,\
                             telefone, email, nascimento\
                             from tb_cliente  where nome like '%" + nomeCli + "%' ")
        banco.conexao.commit()
        seleciona = self.cursor.fetchall()
        self.cursor.close()
        
        return seleciona

    def buscaClienteCompra(self, nomeCli):
        banco = Banco()
        dados = ""
        try:
            self.cursor = banco.conexao.cursor()
            self.cursor.execute(
            "select nome,limite from tb_cliente \
             where nome like '%" + nomeCli + "%' ")
            banco.conexao.commit()
            self.cursor.close()
            dados = self.cursor.fetchone()
            return dados
        except Exception as e:
            return "Erro ", e
        
        

    def incluirCliente(self, nomeCli="", cpf="", endereco="",
                       telefone="", email="", nascimento="", limite=""):
        banco = Banco()
        formato = ''
        formatoCpf = []
        nome = nomeCli.split()
        cpf = cpf.replace(' ', '')
        for i in nome:
            formato = formato + ' ' + i

        cpfjusto = ''
        for x in cpf:
            cpfjusto = cpfjusto + i
        for j in cpfjusto:
            formatoCpf = cpf[:3] + '.' + cpf[3:6] + \
                '.' + cpf[6:9] + '-' + cpf[9:11]

        nomeCli = formato.title()
        cpf = formatoCpf
        #sql = ("SELECT nome FROM tb_cliente where nome = '" + nomeCli + "'")
        #cursor = banco.conexao.cursor()
        #cursor.execute(sql)
        verifica = cursor.fetchone()
        if verifica:
            return "cliente já cadastrado, digite o nome novamente e clique em busca para obter o registro"
        else:
            try:
                cursor = banco.conexao.cursor()
                cursor.execute("insert into tb_cliente ( nome, cpf, endereco,  telefone, email,\
                         nascimento, limite) values \
                        ('" + nomeCli + "','" + cpf + "','" + endereco +
                               "','" + telefone + "','" + email + "','" +
                               nascimento + "'," + limite + ")")

                banco.conexao.commit()
                cursor.close()
                return "Cliente cadastrado com sucesso!"
            except Exception as err:
                return "Erro ao inserir dados,por favor verifique se \
                o cliente em questão já é cadastrado!", err
