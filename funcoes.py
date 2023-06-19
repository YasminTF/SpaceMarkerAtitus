
def criarBaseDados():
    try:
        arquivo = open("banco_dados.txt","r")
        arquivo.close()    
    except:
        arquivo = open("banco_dados.txt","w")
        arquivo.close()
from tkinter import simpledialog
def abrirCaixaPergunta():
    item= simpledialog.askstring("Space" ,  "Nome da estrela:")
    if item is None:
            return        



   