#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
#carregando diretórios e módulos do projeto
diretorio = os.environ["HOME"] + "/sistema_loja"
sys.path.insert(0,diretorio)
from tkinter import *
from modelo.produto import Produto
from tkinter import messagebox


class CadProduto:
    def __init__(self, master = None):
        

        #setando fontes e cores
        self.fonte = ("Liberation Sans", "12")
        self.corfundo = ("#FFFFFF")
        self.corfonte = ("#33ccff")
        
        
        #inicializando a tela
        self.frame = Frame(master)
        self.frame.pack()
        
        #tela de titulo
        self.containerTitulo = Frame(self.frame)
        self.containerTitulo.pack(pady=5)
        self.labelTitulo = Label(self.frame, text="Cadastro Produto", font=self.fonte)
        self.labelTitulo.pack(side=TOP)
        
        #criando o containeres de entrada dos dados
        self.containerCodigo = Frame(self.frame)
        self.containerCodigo.pack()
        self.containerCodigo["pady"] = 5
        self.containerCodigo["padx"] = 27
        
        '''self.containerReferencia = Frame(self.frame)
        self.containerReferencia.pack()
        self.containerReferencia["pady"] = 5
        self.containerReferencia["padx"] = 20'''
        
        self.containerNomeProduto = Frame(self.frame)
        self.containerNomeProduto.pack()
        self.containerNomeProduto["pady"] = 5
        self.containerNomeProduto["padx"] = 20
        
        '''self.containerMarca = Frame(self.frame)
        self.containerMarca.pack()
        self.containerMarca["pady"] = 5
        self.containerMarca["padx"] = 20'''
        
        '''self.containerTamanho = Frame(self.frame)
        self.containerTamanho.pack()
        self.containerTamanho["pady"] = 5
        self.containerTamanho["padx"] = 20'''
        
        self.containerDescricao = Frame(self.frame)
        self.containerDescricao.pack()
        self.containerDescricao["pady"] = 5
        self.containerDescricao["padx"] = 20
        
        self.containerPreco = Frame(self.frame)
        self.containerPreco.pack()
        self.containerPreco["pady"] = 5
        self.containerPreco["padx"] = 20
        
        self.containerPrecoVenda = Frame(self.frame)
        self.containerPrecoVenda.pack()
        self.containerPrecoVenda["pady"] = 5
        self.containerPrecoVenda["padx"] = 20
        
        self.containerBotoes = Frame(self.frame)
        self.containerBotoes.pack()
        self.containerBotoes["pady"] = 5
        self.containerBotoes["padx"] = 20
        
        self.containerSeparador = Frame(self.frame)
        self.containerSeparador.pack()
        self.containerSeparador["pady"] = 5
        self.containerSeparador["padx"] = 20
        
        self.lbCodigo = Label(self.containerCodigo, text = " Código : ")
        self.lbCodigo["pady"] = 5
        self.lbCodigo["padx"] = 20
        self.lbCodigo.pack(side = LEFT)
        self.txtCodigo = Entry(self.containerCodigo, width = 20)
        self.txtCodigo.pack(side = LEFT)
        self.containerSeparador.pack(side = RIGHT)
        
        '''self.lbReferencia = Label(self.containerReferencia, text = " Referência : ")
        self.lbReferencia["pady"] = 5
        self.lbReferencia["padx"] = 5
        self.lbReferencia.pack(side = LEFT)
        self.txtReferencia = Entry(self.containerReferencia, width = 10)
        self.txtReferencia.pack(side = LEFT)
        self.containerSeparador.pack(side = RIGHT)
        self.containerSeparador["pady"] = 5
        self.containerSeparador["padx"] = 40'''
        
        
        self.lbNomeProduto = Label(self.containerNomeProduto, text = " NomeProduto : ")
        self.lbNomeProduto["pady"] = 5
        self.lbNomeProduto["padx"] = 9
        self.lbNomeProduto.pack(side = LEFT)
        self.txtNomeProduto = Entry(self.containerNomeProduto, width = 20)
        self.txtNomeProduto.pack(side = RIGHT)
        
        '''self.lbMarca = Label(self.containerMarca, text = " Marca  : ")
        self.lbMarca["pady"] = 5
        self.lbMarca["padx"] = 17
        self.lbMarca.pack(side = LEFT)
        self.txtMarca = Entry(self.containerMarca, width = 10)
        self.txtMarca.pack(side = LEFT)
        self.containerSeparador.pack(side = RIGHT)'''
        
        '''self.separator = Label(self.containerMarca, width=5, text = "  ")
        self.separator["pady"] = 5
        self.separator["padx"] = 15
        self.separator.pack(side = RIGHT)'''
        
        '''self.lbTamanho = Label(self.containerTamanho, text = " Tamanho  : ")
        self.lbTamanho["pady"] = 5
        self.lbTamanho["padx"] = 17
        self.lbTamanho.pack(side = LEFT)
        self.txtTamanho = Entry(self.containerTamanho, width = 30)
        self.txtTamanho.pack(side = RIGHT)'''
        
        
        self.lbDescricao = Label(self.containerDescricao, text = " Descricao  : ")
        self.lbDescricao["pady"] = 5
        self.lbDescricao["padx"] = 17
        self.lbDescricao.pack(side = LEFT)
        self.txtDescricao = Entry(self.containerDescricao, width = 30)
        self.txtDescricao.pack(side = RIGHT)
        
        self.lbPrecoCompra = Label(self.containerPreco, text = " Preco de compra : ")
        self.lbPrecoCompra["pady"] = 5
        self.lbPrecoCompra["padx"] = 10
        self.lbPrecoCompra.pack(side = LEFT)
        self.txtPrecoCompra = Entry(self.containerPreco)
        self.txtPrecoCompra["width"] = 30
        self.txtPrecoCompra.pack(side = RIGHT)
        
        self.lbPrecoVenda = Label(self.containerPrecoVenda, text = " Preco de venda : ")
        self.lbPrecoVenda["pady"] = 5
        self.lbPrecoVenda["padx"] = 10
        self.lbPrecoVenda.pack(side = LEFT)
        self.txtPrecoVenda = Entry(self.containerPrecoVenda)
        self.txtPrecoVenda["width"] = 30
        self.txtPrecoVenda.pack(side = RIGHT)
        
        self.btInserir = Button(self.containerBotoes, text = " Inserir ")
        self.btInserir["pady"] = 5
        self.btInserir["padx"] = 17
        self.btInserir["command"] = self.inserirProduto
        self.btInserir.pack(side = LEFT)
        
        self.btExcluir = Button(self.containerBotoes, text = " Excluir ")
        self.btExcluir["pady"] = 5
        self.btExcluir["padx"] = 17
        self.btExcluir.pack(side =  LEFT)
        
        self.btBuscar = Button(self.containerBotoes, text = " Buscar ")
        self.btBuscar["pady"] = 5
        self.btBuscar["padx"] = 17
        self.btBuscar.pack(side =  LEFT)
        
        
    def inserirProduto(self):
        produto = Produto()
        nomeProduto = self.txtNomeProduto.get()
        codigoProduto = self.txtCodigo.get()
        descricao = self.txtDescricao.get()
        precoCompra = self.txtPrecoCompra.get()
        precoVenda = self.txtPrecoVenda.get()
        self.txtNomeProduto.delete(0, END)
        self.txtCodigo.delete(0, END)
        self.txtDescricao.delete(0, END)
        self.txtPrecoCompra.delete(0, END)
        self.txtPrecoVenda.delete(0, END)
        message = ""
        message = produto.insertProduto(codigoProduto, nomeProduto, descricao, precoCompra, precoVenda)
        if produto.insertProduto():
            messagebox.showinfo("Sucesso : ", message)
        else:
            messagebox.showerror("Erro : ", message)
            
    
        
root = Tk()
CadProduto(root)
#root.geometry("400x500")
root.resizable(width = False, height = False)
root.title("")
root.mainloop()