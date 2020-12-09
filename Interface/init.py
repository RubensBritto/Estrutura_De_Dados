import tkinter
from numpy.lib.function_base import insert
import Fila
import Pilha
import Lista
#from Lista import *
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

        self.buttonLista = Button(self.frameMain, bg="white", text="Lista", bd=0, width=6, height=2, command= newLista().optionLista)
        self.buttonLista.grid(row=0, column=0) #Executar o Botão
             
        self.windows.mainloop() #Rodar o proprama
       
class newLista:
    def optionLista(self):
        self.windowsLista = Tk()
        self.windowsLista.title("Lista")
        self.windowsLista.minsize(width = 1280, height= 720)
        self.windowsLista.config(bg="#1d2f38") 
        
        self.frameLista = Frame(self.windowsLista, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameLista.pack()

        self.labelOption = Label(self.frameLista, text="Marque a Opção Desejada",font= "arial 45")
        self.labelOption.config(bg="#1d2f38")
        self.labelOption.pack()

        self.buttonCriar = Button(self.frameLista, bg="red", text="Criar Pais", bd="5", fg="white",width=10,command=self.criarLista).pack(pady=12)
        self.buttonEditar = Button(self.frameLista, bg="red", text="Editar Dados", bd="5", fg="white",width=10,command=self.editarListaOption).pack(pady=12)
        self.buttonDeletar = Button(self.frameLista, bg="red", text="Deletar Dados", bd="5", fg="white",width=10,command=self.deletarItem).pack(pady=12)
        self.buttonMostraItems = Button(self.frameLista, bg="red", text="Mostrar Dados", bd="5", fg="white",width=10,command= lambda: Lista.Main().showList()).pack(pady=12)
        self.buttonSalva = Button(self.frameLista, bg="red", text="Salvar Dados", bd="5", fg="white",width=10,command= lambda: Lista.Main().salvaData()).pack(pady=12)

        
        self.returnMain = Button(self.frameLista, bg="red", text="Voltar", bd="5", fg="white",command= self.windowsLista.destroy).pack(pady=12, side="left")



    def criarLista(self):
        self.windowsLista = Tk()
        self.windowsLista.title("Lista")
        self.windowsLista.minsize(width = 1280, height= 720)
        self.windowsLista.config(bg="#1d2f38")

        self.frameLista = Frame(self.windowsLista, width = 1280, height= 720, bg="white", pady="20")
        self.frameLista.pack()

        self.labelName = Label(self.frameLista, text="Inserir o Nome Do Pais",font= "arial 12")
        self.labelName.pack()

        self.insertName = Entry(self.frameLista)
        self.insertName.pack()

        self.labelRegion = Label(self.frameLista, text="Inserir a Região", font= "arial 12")
        self.labelRegion.pack()

        self.insertRegion = Entry(self.frameLista)
        self.insertRegion.pack()

        self.labelHappinessRank = Label(self.frameLista, text="Inserir o Rank de Felicidade ", font= "arial 12")
        self.labelHappinessRank.pack()

        self.insertHappinessRank = Entry(self.frameLista)
        self.insertHappinessRank.pack()
        
        self.labelHappinessScore = Label(self.frameLista, text="Inserir o Indice de Felicidade ", font= "arial 12")
        self.labelHappinessScore.pack()

        self.insertHappinessScore = Entry(self.frameLista)
        self.insertHappinessScore.pack()
        
        self.labelStandardError = Label(self.frameLista, text="Inserir o Erro Padrão ", font= "arial 12")
        self.labelStandardError.pack()

        self.insertStandardError = Entry(self.frameLista)
        self.insertStandardError.pack()

        self.labelEconomy = Label(self.frameLista, text="Inserir o indice de Economia ", font= "arial 12")
        self.labelEconomy.pack()

        self.insertEconomy = Entry(self.frameLista)
        self.insertEconomy.pack()

        self.labelFamily = Label(self.frameLista, text="Inserir o indice de Familia ", font= "arial 12")
        self.labelFamily.pack()

        self.insertFamily = Entry(self.frameLista)
        self.insertFamily.pack()
        
        self.labelHealth = Label(self.frameLista, text="Inserir o indice de Vida ", font= "arial 12")
        self.labelHealth.pack()

        self.insertHealth = Entry(self.frameLista)
        self.insertHealth.pack()

        self.labelFreedom = Label(self.frameLista, text="Inserir o indice de Liberdade ", font= "arial 12")
        self.labelFreedom.pack()

        self.insertFreedom = Entry(self.frameLista)
        self.insertFreedom.pack()

        self.labelTrust = Label(self.frameLista, text="Inserir o indice de Confiança ", font= "arial 12")
        self.labelTrust.pack()

        self.insertTrust = Entry(self.frameLista)
        self.insertTrust.pack()

        self.labelGenerosity = Label(self.frameLista, text="Inserir o indice de Genorosidade ", font= "arial 12")
        self.labelGenerosity.pack()

        self.insertGenerosity = Entry(self.frameLista)
        self.insertGenerosity.pack()

        self.labelDystopiaResidual = Label(self.frameLista, text="Inserir o indice de Distopia Residual ", font= "arial 12")
        self.labelDystopiaResidual.pack()

        self.insertDystopiaResidual = Entry(self.frameLista)
        self.insertDystopiaResidual.pack()
    

        self.salvarData = Button(self.frameLista, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Lista.Main().criarDado(str(self.insertName.get()),str(self.insertRegion.get()),
        float(self.insertHappinessRank.get()), float(self.insertHappinessScore.get()), float(self.insertStandardError.get()), float(self.insertEconomy.get()), float(self.insertFamily.get()),
        float(self.insertHealth.get()), float(self.insertFreedom.get()), float(self.insertTrust.get()), float(self.insertGenerosity.get()), float(self.insertDystopiaResidual.get())))
        self.salvarData.pack()

        self.returnMain = Button(self.frameLista, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsLista.destroy).pack()
    
    def editarListaOption(self):

        self.windowsLista = Tk()
        self.windowsLista.title("Lista")
        self.windowsLista.minsize(width = 1280, height= 720)
        self.windowsLista.config(bg="#1d2f38") 
        
        self.frameLista = Frame(self.windowsLista, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameLista.pack()

        self.labelOption = Label(self.frameLista, text="Marque o que deseja Editar",font= "arial 45")
        self.labelOption.config(bg="#1d2f38")
        self.labelOption.pack()

        self.buttonEditarPais = Button(self.frameLista, bg="red", text="Nome do Pais", bd="5", fg="white",width=30,command=self.editarNome).pack(pady=12)
        self.buttonEditarRegion = Button(self.frameLista, bg="red", text="Região", bd="5", fg="white",width=30,command=self.editarRegion).pack(pady=12)
        self.buttonEditarHappinessRank = Button(self.frameLista, bg="red", text="Rank de felicidade", bd="5", fg="white",width=30,command=self.editarHappinessRank).pack(pady=12)
        self.buttonEditarHappinessScore = Button(self.frameLista, bg="red", text="Score de Felicidade", bd="5", fg="white",width=30,command=self.editarHappinessScore).pack(pady=12)
        self.buttonEditarStandardError = Button(self.frameLista, bg="red", text="Erro Padrão", bd="5", fg="white",width=30,command=self.editarStandardError).pack(pady=12)
        self.buttonEditarEconomy = Button(self.frameLista, bg="red", text="Indice de Economia", bd="5", fg="white",width=30,command=self.editarEconomy).pack(pady=12)
        self.buttonEditarFamily = Button(self.frameLista, bg="red", text="Indice da Familia", bd="5", fg="white",width=30,command=self.editarFamily).pack(pady=12)
        self.buttonEditarHealth = Button(self.frameLista, bg="red", text="Expectativa de Vida", bd="5", fg="white",width=30,command=self.editarHealth).pack(pady=12)
        self.buttonEditarFreedom = Button(self.frameLista, bg="red", text="Indice de Liberdade", bd="5", fg="white",width=30,command=self.editarFreedom).pack(pady=12)
        self.buttonEditarTrust = Button(self.frameLista, bg="red", text="Indice de Confiança", bd="5", fg="white",width=30,command=self.editarTrust).pack(pady=12)
        self.buttonEditarGenorosity = Button(self.frameLista, bg="red", text="Indice de Generosidade", bd="5", fg="white",width=30,command=self.editarGenorosity).pack(pady=12)
        self.buttonEditarDystopiaResidual = Button(self.frameLista, bg="red", text="Distopia Residual", bd="5", fg="white",width=30,command=self.editarDystopiaResidual).pack(pady=12)

        self.returnMain = Button(self.frameLista, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsLista.destroy).pack(pady=12,side="left")
    
    def editarNome(self):
        
        self.windowsLista = Tk()
        self.windowsLista.title("Lista")
        self.windowsLista.minsize(width = 1280, height= 720)
        self.windowsLista.config(bg="#1d2f38") 
        
        self.frameLista = Frame(self.windowsLista, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameLista.pack()
        
        self.labelName = Label(self.frameLista, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertName = Entry(self.frameLista)
        self.insertName.pack()
        
        self.labelEditName = Label(self.frameLista, text="Inserir o Novo Nome do Pais",font= "arial 12")
        self.labelEditName.pack()

        self.editName = Entry(self.frameLista)
        self.editName.pack()
        
        self.salvarData = Button(self.frameLista, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Lista.Main().editarDado(1,str(self.insertName.get()),str(self.editName.get()))).pack(pady=12)
        self.returnMain = Button(self.frameLista, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsLista.destroy).pack(pady=12)
    
    def editarRegion(self):
        
        self.windowsLista = Tk()
        self.windowsLista.title("Lista")
        self.windowsLista.minsize(width = 1280, height= 720)
        self.windowsLista.config(bg="#1d2f38") 
        
        self.frameLista = Frame(self.windowsLista, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameLista.pack()
        
        self.labelName = Label(self.frameLista, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertName = Entry(self.frameLista)
        self.insertName.pack()
        
        self.labelEditRegion = Label(self.frameLista, text="Inserir a nova Região",font= "arial 12")
        self.labelEditRegion.pack()

        self.editRegion = Entry(self.frameLista)
        self.editRegion.pack()
        
        self.salvarData = Button(self.frameLista, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Lista.Main().editarDado(2,str(self.insertName.get()),str(self.editRegion.get()))).pack(pady=12)
        self.returnMain = Button(self.frameLista, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsLista.destroy).pack(pady=12)
    
    def editarHappinessRank(self):
        
        self.windowsLista = Tk()
        self.windowsLista.title("Lista")
        self.windowsLista.minsize(width = 1280, height= 720)
        self.windowsLista.config(bg="#1d2f38") 
        
        self.frameLista = Frame(self.windowsLista, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameLista.pack()
        
        self.labelName = Label(self.frameLista, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertName = Entry(self.frameLista)
        self.insertName.pack()
        
        self.labelEditHappinessRank = Label(self.frameLista, text="Inserir o Novo Rank de Felicidade",font= "arial 12")
        self.labelEditHappinessRank.pack()

        self.editHappinessRank = Entry(self.frameLista)
        self.editHappinessRank.pack()
        
        self.salvarData = Button(self.frameLista, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Lista.Main().editarDado(3,str(self.insertName.get()),str(self.editHappinessRank.get()))).pack(pady=12)
        self.returnMain = Button(self.frameLista, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsLista.destroy).pack(pady=12)
    
    def editarHappinessScore (self):
        
        self.windowsLista = Tk()
        self.windowsLista.title("Lista")
        self.windowsLista.minsize(width = 1280, height= 720)
        self.windowsLista.config(bg="#1d2f38") 
        
        self.frameLista = Frame(self.windowsLista, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameLista.pack()
        
        self.labelName = Label(self.frameLista, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertName = Entry(self.frameLista)
        self.insertName.pack()
        
        self.labelEditHappinessScore  = Label(self.frameLista, text="Inserir o novo Score de Felicidade",font= "arial 12")
        self.labelEditHappinessScore.pack()

        self.editHappinessScore  = Entry(self.frameLista)
        self.editHappinessScore.pack()
        
        self.salvarData = Button(self.frameLista, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Lista.Main().editarDado(4,str(self.insertName.get()),str(self.editHappinessScore.get()))).pack(pady=12)
        self.returnMain = Button(self.frameLista, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsLista.destroy).pack(pady=12)
    
    def editarStandardError(self):
        
        self.windowsLista = Tk()
        self.windowsLista.title("Lista")
        self.windowsLista.minsize(width = 1280, height= 720)
        self.windowsLista.config(bg="#1d2f38") 
        
        self.frameLista = Frame(self.windowsLista, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameLista.pack()
        
        self.labelName = Label(self.frameLista, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertName = Entry(self.frameLista)
        self.insertName.pack()
        
        self.labelEditStandardError  = Label(self.frameLista, text="Inserir o novo Erro Padrão",font= "arial 12")
        self.labelEditStandardError.pack()

        self.editStandardError  = Entry(self.frameLista)
        self.editStandardError.pack()
        
        self.salvarData = Button(self.frameLista, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Lista.Main().editarDado(5,str(self.insertName.get()),str(self.editStandardError.get()))).pack(pady=12)
        self.returnMain = Button(self.frameLista, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsLista.destroy).pack(pady=12)

    def editarEconomy(self):
        
        self.windowsLista = Tk()
        self.windowsLista.title("Lista")
        self.windowsLista.minsize(width = 1280, height= 720)
        self.windowsLista.config(bg="#1d2f38") 
        
        self.frameLista = Frame(self.windowsLista, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameLista.pack()
        
        self.labelName = Label(self.frameLista, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertName = Entry(self.frameLista)
        self.insertName.pack()
        
        self.labelEditEconomy  = Label(self.frameLista, text="Inserir o novo Indice de Economia",font= "arial 12")
        self.labelEditEconomy.pack()

        self.editEconomy  = Entry(self.frameLista)
        self.editEconomy.pack()
        
        self.salvarData = Button(self.frameLista, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Lista.Main().editarDado(6,str(self.insertName.get()),str(self.editEconomy.get()))).pack(pady=12)
        self.returnMain = Button(self.frameLista, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsLista.destroy).pack(pady=12)

    def editarFamily(self):
                    
        self.windowsLista = Tk()
        self.windowsLista.title("Lista")
        self.windowsLista.minsize(width = 1280, height= 720)
        self.windowsLista.config(bg="#1d2f38") 
        
        self.frameLista = Frame(self.windowsLista, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameLista.pack()
        
        self.labelName = Label(self.frameLista, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertName = Entry(self.frameLista)
        self.insertName.pack()
        
        self.labelEditFamily  = Label(self.frameLista, text="Inserir o novo Indice da Familia",font= "arial 12")
        self.labelEditFamily.pack()

        self.editFamily  = Entry(self.frameLista)
        self.editFamily.pack()
        
        self.salvarData = Button(self.frameLista, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Lista.Main().editarDado(7,str(self.insertName.get()),str(self.editFamily.get()))).pack(pady=12)
        self.returnMain = Button(self.frameLista, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsLista.destroy).pack(pady=12)
    
    def editarHealth(self):
            
        self.windowsLista = Tk()
        self.windowsLista.title("Lista")
        self.windowsLista.minsize(width = 1280, height= 720)
        self.windowsLista.config(bg="#1d2f38") 
        
        self.frameLista = Frame(self.windowsLista, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameLista.pack()
        
        self.labelName = Label(self.frameLista, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertName = Entry(self.frameLista)
        self.insertName.pack()
        
        self.labelEditHealth  = Label(self.frameLista, text="Inserir o novo Indice de Expectativa de Vida",font= "arial 12")
        self.labelEditHealth.pack()

        self.editHealth  = Entry(self.frameLista)
        self.editHealth.pack()
        
        self.salvarData = Button(self.frameLista, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Lista.Main().editarDado(8,str(self.insertName.get()),str(self.editHealth.get()))).pack(pady=12)
        self.returnMain = Button(self.frameLista, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsLista.destroy).pack(pady=12)
    
    def editarFreedom(self):
            
        self.windowsLista = Tk()
        self.windowsLista.title("Lista")
        self.windowsLista.minsize(width = 1280, height= 720)
        self.windowsLista.config(bg="#1d2f38") 
        
        self.frameLista = Frame(self.windowsLista, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameLista.pack()
        
        self.labelName = Label(self.frameLista, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertName = Entry(self.frameLista)
        self.insertName.pack()
        
        self.labelEditFreedom  = Label(self.frameLista, text="Inserir o novo Indice de Liberdade",font= "arial 12")
        self.labelEditFreedom.pack()

        self.editFreedom  = Entry(self.frameLista)
        self.editFreedom.pack()
        
        self.salvarData = Button(self.frameLista, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Lista.Main().editarDado(9,str(self.insertName.get()),str(self.editFreedom.get()))).pack(pady=12)
        self.returnMain = Button(self.frameLista, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsLista.destroy).pack(pady=12)
    
    def editarTrust(self):
            
        self.windowsLista = Tk()
        self.windowsLista.title("Lista")
        self.windowsLista.minsize(width = 1280, height= 720)
        self.windowsLista.config(bg="#1d2f38") 
        
        self.frameLista = Frame(self.windowsLista, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameLista.pack()
        
        self.labelName = Label(self.frameLista, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertName = Entry(self.frameLista)
        self.insertName.pack()
        
        self.labelEditTrust  = Label(self.frameLista, text="Inserir o novo Indice de confiança",font= "arial 12")
        self.labelEditTrust.pack()

        self.editTrust  = Entry(self.frameLista)
        self.editTrust.pack()
        
        self.salvarData = Button(self.frameLista, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Lista.Main().editarDado(10,str(self.insertName.get()),str(self.editTrust.get()))).pack(pady=12)
        self.returnMain = Button(self.frameLista, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsLista.destroy).pack(pady=12)

    def editarGenorosity(self):
            
        self.windowsLista = Tk()
        self.windowsLista.title("Lista")
        self.windowsLista.minsize(width = 1280, height= 720)
        self.windowsLista.config(bg="#1d2f38") 
        
        self.frameLista = Frame(self.windowsLista, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameLista.pack()
        
        self.labelName = Label(self.frameLista, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertName = Entry(self.frameLista)
        self.insertName.pack()
        
        self.labelEditGenorosity  = Label(self.frameLista, text="Inserir o novo Indice de Genorisidade",font= "arial 12")
        self.labelEditGenorosity.pack()

        self.editGenorosity  = Entry(self.frameLista)
        self.editGenorosity.pack()
        
        self.salvarData = Button(self.frameLista, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Lista.Main().editarDado(11,str(self.insertName.get()),str(self.editGenorosity.get()))).pack(pady=12)
        self.returnMain = Button(self.frameLista, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsLista.destroy).pack(pady=12)

    def editarDystopiaResidual(self):
            
        self.windowsLista = Tk()
        self.windowsLista.title("Lista")
        self.windowsLista.minsize(width = 1280, height= 720)
        self.windowsLista.config(bg="#1d2f38") 
        
        self.frameLista = Frame(self.windowsLista, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameLista.pack()
        
        self.labelName = Label(self.frameLista, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertName = Entry(self.frameLista)
        self.insertName.pack()
        
        self.labelEditDystopiaResidual  = Label(self.frameLista, text="Inserir o novo indice de Distopia Residual",font= "arial 12")
        self.labelEditDystopiaResidual.pack()

        self.editDystopiaResidual  = Entry(self.frameLista)
        self.editDystopiaResidual.pack()
        
        self.salvarData = Button(self.frameLista, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Lista.Main().editarDado(12,str(self.insertName.get()),str(self.editDystopiaResidual.get()))).pack(pady=12)
        self.returnMain = Button(self.frameLista, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsLista.destroy).pack(pady=12)

    def deletarItem(self):
        self.windowsLista = Tk()
        self.windowsLista.title("Lista")
        self.windowsLista.minsize(width = 1280, height= 720)
        self.windowsLista.config(bg="#1d2f38") 
        
        self.frameLista = Frame(self.windowsLista, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameLista.pack()
        
        self.labelName = Label(self.frameLista, text="Inserir o Nome Do Pais Que deseja Deletar",font= "arial 12")
        self.labelName.pack()

        self.insertName = Entry(self.frameLista)
        self.insertName.pack()

        
        self.salvarData = Button(self.frameLista, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Lista.Main().deletarDado(str(self.insertName.get()))).pack(pady=12)
        self.returnMain = Button(self.frameLista, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsLista.destroy).pack(pady=12)
    def mostrarDados():
        print("Mostrar os dados na tela")
        file = open("/data.csv", "r")
        text_area = tkinter.Text(self.windowsLista,font="Arial 12",width=1280,height=720)
        text_area.pack()
        text_area= file.read()
        file.close()

#Lista.Main()
i = Interface()
#Tree.Main()
#Pilha.Main()
#Fila.Main()