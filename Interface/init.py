import Fila
import Pilha
import Lista
import Tree
from tkinter import *

class Interface:
    def __init__(self):
        self.windows = Tk()
        self.windows.title("Estrutura de Dados")
        self.windows.minsize(width = 1280, height= 720)
        self.windows.config(bg="#1d2f38")
        
        self.frame = Frame(self.windows,width = 1020, height= 768, bg="black")
        self.frame.pack() #Executar o frame
        
        self.buttonLista = Button(self.frame, bg="white", text="Lista", bd=0, width=6, height=2, command=None)
        self.buttonLista.grid(row=0, column=0) #Executar o Botão
        self.windows.mainloop() #Rodar o proprama
i = Interface()
#Tree.Main()
#Lista.Main()
#Pilha.Main()
#Fila.Main()