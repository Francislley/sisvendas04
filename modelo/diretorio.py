import sys
import os


def init(diretorio):
    diretorio = os.environ["HOME"] + "/sistema_loja"
    sys.path.insert(0, diretorio)
