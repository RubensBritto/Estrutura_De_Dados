from numpy.lib.function_base import insert
import Fila
import Pilha
#import Lista
from Lista import *
import Tree
from tkinter import * 

class Interface:
    
    def __init__(self):
        self.windows = Tk()
        self.windows.title("Estrutura de Dados")
        self.windows.minsize(width = 1280, height= 720)
        self.windows.config(bg="#1d2f38")
        
        self.frameMain = Frame(self.windows,width = 1020, height= 768, bg="black")
        self.frameMain.pack() #Executar o frameMain

        self.buttonLista = Button(self.frameMain, bg="white", text="Lista", bd=0, width=6, height=2, command= newLista().criarLista)
        self.buttonLista.grid(row=0, column=0) #Executar o Botão
             
        self.windows.mainloop() #Rodar o proprama
       
    
class newLista:
    def criarLista(self):
        self.windowsLista = Tk()
        self.windowsLista.title("Lista")
        self.windowsLista.minsize(width = 1280, height= 720)
        self.windowsLista.config(bg="#1d2f38")

        self.frameLista = Frame(self.windowsLista,width = 1020, height= 768, bg="white", pady="20")
        self.frameLista.pack()

        self.labeName = Label(self.frameLista, text="Inserir Nome", font= "arial 12")
        self.labeName.pack(side="left")

        self.insertName = Entry(self.frameLista)
        self.insertName.pack(side="left")
        print(self.insertName)

        self.salvarData = Button(self.frameLista, bg="red", text="SALVAR", bd="0", fg="white",command=Lista.Main().criarDado)
        self.salvarData.pack()

i = Interface()
#Tree.Main()
#Lista.Main()
#Pilha.Main()
#Fila.Main()