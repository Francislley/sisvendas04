#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys 


diretorio = os.environ["HOME"] + "/sistema_loja"
sys.path.insert(0,diretorio)

from tkinter import *
from tkinter.ttk import *
from collections import OrderedDict
import collections
from modelo.cliente import Cliente
from modelo.produto import Produto




class Venda(object):
    def __init__(self, master = None):
        self.box_valor = StringVar()
        self.opcao = ''
        self.selec_cliente = ''
        self.texto = 0.0
        self.soma2 = 0.0
        self.preco = StringVar()
        self.preco.set("Valor total : 0,0")
        
        self.framePrincipal = Frame(master)
        self.framePrincipal.pack()
        
        self.containerTipoVenda = Frame(self.framePrincipal)
        self.containerTipoVenda.pack(padx = 5, pady = 10)
        
        
        self.containerCliente = Frame(self.framePrincipal)
        self.containerCliente.pack(padx = 5, pady = 10)
        
        
        self.containerProduto = Frame(self.framePrincipal)
        self.containerProduto.pack(padx = 5, pady = 10)
        
        self.containerVenda = Frame(self.framePrincipal)
        self.containerVenda.pack(padx = 5, pady = 10)
        
        self.boxVenda = Combobox(self.containerTipoVenda, textvariable = self.box_valor, state = 'readonly')
        self.boxVenda["values"] = ('Cartão','A vista','Crediário')
        self.boxVenda.current(0)
        self.boxVenda.bind("<<ComboboxSelected>>", self.alteraOpcao)
        self.boxVenda.pack(side = LEFT)
        
        self.lbProduto = Label(self.containerProduto, text = 'Produto: ')
        self.lbProduto.pack(side = LEFT, padx = 5, pady = 10)
        
        self.boxProduto = Combobox(self.containerProduto, textvariable = StringVar(), state = 'normal')
        self.boxProduto.bind("<<ComboboxSelected>>", self.seletaProduto)
        #self.boxProduto = self.buscaProduto
        
        
        pdt = Produto()
        self.texto = list()
        self.num = list()
        self.todo = {}
        self.busca = pdt.pesquisaProduto()
        self.busca = dict(self.busca)
        
        for i in self.busca.keys():
            self.texto.append(i)
            self.num.append(self.busca[i])
            
          
        for i in range(len(self.busca)):
            self.todo[i] = (self.texto[i],self.num[i])
            print(self.todo[i])
        
        

            
        
        self.boxProduto["values"] = self.texto
        self.boxProduto.pack()

        self.listaVenda = Listbox(self.containerVenda, selectmode = MULTIPLE)
        #self.listaVenda.bind("<<ListboxSelected>>",self.precoTotal)
        self.listaVenda.xview()
        self.listaVenda.pack()

        self.precoTotal = Label(self.containerVenda, textvariable = self.preco)#, state = 'readonly')
        
        
        self.precoTotal.pack()
        '''self.btTotal = Button(self.containerVenda, text = "Total")
        self.btTotal["command"] = self.precoTotal
        self.btTotal.pack()'''


    


        
    def seletaProduto(self, nomeProduto):
        self.point = ''
        soma = 0
        

        nomeProduto = ()
        nomeProduto = self.boxProduto.get()
        print(nomeProduto)
        print(self.busca.keys())
        for i in range(len(self.texto)):
            
            if nomeProduto == self.texto[i]:
                
                nomeProduto = (self.texto[i].split(),str(self.num[i]))
                soma = self.num[i]
        soma = self.soma2 + soma 
        self.listaVenda.insert(END,nomeProduto)
        self.preco.set("Valor total: {}".format(soma))
        #self.point = ("Total : {}".format(float(soma)))
        self.soma2 = soma
        print(nomeProduto)
        
 
        

        
          
    def alteraOpcao(self, event):
        sentenca = False
        opcao = str(self.boxVenda.get())
        sentenca = (opcao == "Crediário")
        if sentenca:
            self.lbCliente = Label(self.containerCliente, text = 'Selecionar Cliente: ')
            self.lbCliente.pack(side = LEFT, padx = 5, pady=10)
            self.selCliente = Entry(self.containerCliente)
            self.selCliente.pack(side = LEFT)
            self.btPesquisa = Button(self.containerCliente, text = "Pesquisar",command = self.pesquisaCliente)
            self.btPesquisa.pack(side = RIGHT)
        else:
            self.lbCliente.destroy()
            self.selCliente.destroy()
            self.btPesquisa.destroy()
        print (opcao)
        print(sentenca)
        return opcao
    
    
    def pesquisaCliente(self):
        nome = ''
        cliente = Cliente()
        nome = self.selCliente.get()
        cliente.buscaClienteCompra(nome)
        
   


raiz = Tk()
Venda(raiz)
raiz.title('')
raiz.mainloop()