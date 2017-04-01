#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os


from tkinter import *
diretorio = os.environ["HOME"] + "/sistema_loja"
sys.path.insert(0, diretorio)
from modelo.cliente import Cliente
#from select_cliente import Select_cliente
from tkinter import messagebox


class CadCliente(object):
    def __init__(self, master=None):
        # setando fontes e cores
        self.fonte = ("Liberation Sans", "12")
        self.corfonte = ("#236B8E")
        self.corfundo = ("#FFFFFF")
        # inicializando a tela
        self.frame = Frame(master, bg="#FFFFFF")
        
        self.frame.pack()

        # tela de titulo
        self.containerTitulo = Frame(self.frame, bg="#FFFFFF")
        self.containerTitulo.pack(pady=5)
        self.labelTitulo = Label(
            self.frame, text="Cadastro Cliente", font=self.fonte, bg=self.corfundo, fg=self.corfonte)
        self.labelTitulo.pack(side=TOP)

        # criando o contaieres de entrada dos dados
        self.containerNome = Frame(self.frame, bg=self.corfundo)
        self.containerNome.pack()
        self.containerNome["pady"] = 5
        self.containerNome["padx"] = 20

        self.containerCpf = Frame(self.frame, bg=self.corfundo)
        self.containerCpf.pack()
        self.containerCpf["pady"] = 5
        self.containerCpf["padx"] = 20

        self.containerEndereco = Frame(self.frame, bg=self.corfundo)
        self.containerEndereco.pack()
        self.containerEndereco["pady"] = 5
        self.containerEndereco["padx"] = 20

        self.containerTelefone = Frame(self.frame, bg=self.corfundo)
        self.containerTelefone.pack()
        self.containerTelefone["pady"] = 5
        self.containerTelefone["padx"] = 20

        self.containerEmail = Frame(self.frame, bg=self.corfundo)
        self.containerEmail.pack()
        self.containerEmail["pady"] = 5
        self.containerEmail["padx"] = 20

        self.containerLimite = Frame(self.frame, bg=self.corfundo)
        self.containerLimite.pack(pady=5, padx=20)

        self.containerDataNasc = Frame(self.frame, bg=self.corfundo)
        self.containerDataNasc.pack()
        self.containerDataNasc["pady"] = 5
        self.containerDataNasc["padx"] = 20

        self.containerBotoes = Frame(self.frame, bg=self.corfundo)
        self.containerBotoes.pack()
        self.containerBotoes["pady"] = 5
        self.containerBotoes["padx"] = 20

        self.lbNome = Label(self.containerNome, text=" Nome : ", bg=self.corfundo)
        self.lbNome["pady"] = 5
        self.lbNome["padx"] = 20
        self.lbNome.pack(side=LEFT)
        self.txtNome = Entry(self.containerNome, width=30)
        self.txtNome.focus_force()
        self.txtNome.pack(side=RIGHT)

        self.lbCpf = Label(self.containerCpf, text=" CPF : ", bg=self.corfundo)
        self.lbCpf["pady"] = 5
        self.lbCpf["padx"] = 27
        self.lbCpf.pack(side=LEFT)
        self.txtCpf = Entry(self.containerCpf, width=30)
        self.txtCpf.pack(side=RIGHT)

        self.lbEndereco = Label(self.containerEndereco, text=" Endereco : ", bg=self.corfundo)
        self.lbEndereco["pady"] = 5
        self.lbEndereco["padx"] = 9
        self.lbEndereco.pack(side=LEFT)
        self.txtEndereco = Entry(self.containerEndereco, width=30)
        self.txtEndereco.pack(side=RIGHT)

        self.lbEmail = Label(self.containerEmail, text=" Email  : ", bg=self.corfundo)
        self.lbEmail["pady"] = 5
        self.lbEmail["padx"] = 17
        self.lbEmail.pack(side=LEFT)
        self.txtEmail = Entry(self.containerEmail, width=30)
        self.txtEmail.pack(side=RIGHT)

        self.lbTelefone = Label(self.containerTelefone, text=" Telefone  : ", bg=self.corfundo)
        self.lbTelefone["pady"] = 5
        self.lbTelefone["padx"] = 17
        self.lbTelefone.pack(side=LEFT)
        self.txtTelefone = Entry(self.containerTelefone, width=30)
        self.txtTelefone.pack(side=RIGHT)

        self.lbDataNasc = Label(self.containerDataNasc, text=" Data Nasc  : ", bg=self.corfundo)
        self.lbDataNasc["pady"] = 5
        self.lbDataNasc["padx"] = 17
        self.lbDataNasc.pack(side=LEFT)
        self.txtDataNasc = Entry(self.containerDataNasc, width=30)
        self.txtDataNasc.pack(side=RIGHT)

        self.lbLimite = Label(self.containerLimite, text=" Limite  : ", bg=self.corfundo)
        self.lbLimite.pack(side=LEFT, pady=5, padx=17)
        self.txtLimite = Entry(self.containerLimite, width=30)
        self.txtLimite.pack(side=RIGHT)

        self.btInserir = Button(self.containerBotoes, text=" Inserir ", bg=self.corfundo, fg="#8C7853")
        self.btInserir["pady"] = 5
        self.btInserir["padx"] = 17
        self.btInserir.pack(side=LEFT)
        self.btInserir["command"] = self.insertCliente

        '''self.btExcluir = Button(self.containerBotoes, text = " Excluir ")
        self.btExcluir["pady"] = 5
        self.btExcluir["padx"] = 17
        self.btExcluir.pack(side =  LEFT)'''

        self.btBuscar = Button(self.containerBotoes, text=" Buscar ", bg=self.corfundo, fg="#8C7853")
        self.btBuscar["pady"] = 5
        self.btBuscar["padx"] = 17
        self.btBuscar.pack(side=LEFT)
        self.btBuscar["command"] = self.exibeCliente

    """def selecionaCliente(self):
        cliente = Cliente()
        nome = self.txtNome.get()
        cliente.buscaCliente(nome)"""

    def exibeCliente(self):

        cliente = Cliente()
        nome = ""
        message = ""
        nome = self.txtNome.get()
        message = cliente.buscaCliente(nome)
        if message:
            messagebox.showinfo("Sucesso : ", message)
        else:
            messagebox.showinfo("", "Cliente não cadastrado")

    def alteraCliente(self):
        cliente = Cliente()


    def insertCliente(self):
        cliente = Cliente()
        nome = self.txtNome.get()
        cpf = self.txtCpf.get()
        endereco = self.txtEndereco.get()
        email = self.txtEmail.get()
        telefone = self.txtTelefone.get()
        dataNascimento = self.txtDataNasc.get()
        limite = self.txtLimite.get()
        self.txtNome.delete(0, END)
        self.txtCpf.delete(0, END)
        self.txtEndereco.delete(0, END)
        self.txtEmail.delete(0, END)
        self.txtTelefone.delete(0, END)
        self.txtDataNasc.delete(0, END)
        self.txtLimite.delete(0, END)
        message = ""
        message = cliente.incluirCliente(
            nome, cpf, endereco, telefone, email, limite, dataNascimento)
        if cliente.incluirCliente():
            messagebox.showinfo("Sucesso : ", message)
        else:
            messagebox.showerror("Erro : ", message)


root = Tk()
CadCliente(root)
#root.geometry("600x800")
root.resizable(width=False, height=False)
root.title("Cadastro de Clientes")
root.mainloop()
