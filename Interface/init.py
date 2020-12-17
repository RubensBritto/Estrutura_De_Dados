from numpy.lib.function_base import insert
import Fila
import Pilha
import Lista
import Grafo
#from Lista import *
import Tree
from tkinter import * 
from tkinter import messagebox

class Interface:
    
    def __init__(self):
        self.windows = Tk()
        self.windows.title("Estrutura de Dados")
        self.windows.minsize(width = 1280, height= 720)
        self.windows.config(bg="#1d2f38")
        
        self.frameMain = Frame(self.windows,width = 1020, height= 768, bg="#1d2f38")
        self.frameMain.pack() #Executar o frameMain

        self.buttonLista = Button(self.frameMain, bg="#b5706b", text="Lista", bd="5",width=10, height=2, command= newLista().optionLista).pack(pady=12)
        self.buttonFila = Button(self.frameMain, bg="#b5706b", text="Fila", bd="5", width=10, height=2, command= newFila().optionFila).pack(pady=12)
        self.buttonPilha = Button(self.frameMain, bg="#b5706b", text="Pilha", bd="5", width=10, height=2, command= newPilha().optionPilha).pack(pady=12)
        self.buttonTree = Button(self.frameMain, bg="#b5706b", text="Tree", bd="5", width=10, height=2, command= newTree().optionOrdnenarTree).pack(pady=12)
        self.buttonGrafo = Button(self.frameMain, bg="#b5706b", text="Grafo", bd="5", width=10, height=2, command= newGrafo().optionGrafo).pack(pady=12)
        self.returnMain = Button(self.frameMain, bg="#db2316", text="Voltar", bd="5", fg="white",width=10, height=2,command= self.windows.destroy).pack(pady=12,side="left")


             
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
        Lista.Main().iniciar()

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
        
        self.salvarData = Button(self.frameLista, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Lista.Main().editar(1,str(self.insertName.get()),str(self.editName.get()))).pack(pady=12)
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
        
        self.salvarData = Button(self.frameLista, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Lista.Main().editar(2,str(self.insertName.get()),str(self.editRegion.get()))).pack(pady=12)
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
        
        self.salvarData = Button(self.frameLista, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Lista.Main().editar(3,str(self.insertName.get()),str(self.editHappinessRank.get()))).pack(pady=12)
        self.returnMain = Button(self.frameLista, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsLista.destroy).pack(pady=12)
    
    def editarHappinessScore(self):
        
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
        
        self.salvarData = Button(self.frameLista, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Lista.Main().editar(4,str(self.insertName.get()),str(self.editHappinessScore.get()))).pack(pady=12)
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
        
        self.salvarData = Button(self.frameLista, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Lista.Main().editar(5,str(self.insertName.get()),str(self.editStandardError.get()))).pack(pady=12)
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
        
        self.salvarData = Button(self.frameLista, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Lista.Main().editar(6,str(self.insertName.get()),str(self.editEconomy.get()))).pack(pady=12)
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
        
        self.salvarData = Button(self.frameLista, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Lista.Main().editar(7,str(self.insertName.get()),str(self.editFamily.get()))).pack(pady=12)
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
        
        self.salvarData = Button(self.frameLista, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Lista.Main().editar(8,str(self.insertName.get()),str(self.editHealth.get()))).pack(pady=12)
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
        
        self.salvarData = Button(self.frameLista, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Lista.Main().editar(9,str(self.insertName.get()),str(self.editFreedom.get()))).pack(pady=12)
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
        
        self.salvarData = Button(self.frameLista, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Lista.Main().editar(10,str(self.insertName.get()),str(self.editTrust.get()))).pack(pady=12)
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
        
        self.salvarData = Button(self.frameLista, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Lista.Main().editar(11,str(self.insertName.get()),str(self.editGenorosity.get()))).pack(pady=12)
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
        
        self.salvarData = Button(self.frameLista, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Lista.Main().editar(12,str(self.insertName.get()),str(self.editDystopiaResidual.get()))).pack(pady=12)
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

class newFila:
    def optionFila(self):
        self.windowsFila = Tk()
        self.windowsFila.title("Esturuta de Dados")
        self.windowsFila.minsize(width = 1280, height= 720)
        self.windowsFila.config(bg="#1d2f38")
        
        self.frameFila = Frame(self.windowsFila, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameFila.pack()

        self.labelOption = Label(self.frameFila, text="Marque a Opção Desejada",font= "arial 45")
        self.labelOption.config(bg="#1d2f38")
        self.labelOption.pack()
        Fila.Main().iniciar()

        self.buttonCriar = Button(self.frameFila, bg="red", text="Criar Pais", bd="5", fg="white",width=10,command= self.criarFila).pack(pady=12)
        self.buttonEditar = Button(self.frameFila, bg="red", text="Editar Dados", bd="5", fg="white",width=10,command=self.editarFilaOption).pack(pady=12)
        self.buttonDeletar = Button(self.frameFila, bg="red", text="Deletar Dados", bd="5", fg="white",width=10,command=self.deletarFila).pack(pady=12)
        self.buttonMostraItems = Button(self.frameFila, bg="red", text="Mostrar Dados", bd="5", fg="white",width=10,command= lambda: Fila.Main().showQueue()).pack(pady=12)
        self.buttonSalva = Button(self.frameFila, bg="red", text="Salvar Dados", bd="5", fg="white",width=10,command= lambda: Fila.Main().salvaCSV()).pack(pady=12)
        self.returnMain = Button(self.frameFila, bg="red", text="Voltar", bd="5", fg="white",command= self.windowsFila.destroy).pack(pady=12, side="left")
    
    def criarFila(self):
        self.windowsFila = Tk()
        self.windowsFila.title("Esturuta de Dados")
        self.windowsFila.minsize(width = 1280, height= 720)
        self.windowsFila.config(bg="#1d2f38")

        self.frameFila = Frame(self.windowsFila, width = 1280, height= 720, bg="white", pady="20")
        self.frameFila.pack()
    
        self.labelName = Label(self.frameFila, text="Inserir o Nome Do Pais",font= "arial 12")
        self.labelName.pack()

        self.insertName = Entry(self.frameFila)
        self.insertName.pack()

        self.labelRegion = Label(self.frameFila, text="Inserir a Região", font= "arial 12")
        self.labelRegion.pack()

        self.insertRegion = Entry(self.frameFila)
        self.insertRegion.pack()

        self.labelHappinessRank = Label(self.frameFila, text="Inserir o Rank de Felicidade ", font= "arial 12")
        self.labelHappinessRank.pack()

        self.insertHappinessRank = Entry(self.frameFila)
        self.insertHappinessRank.pack()
        
        self.labelHappinessScore = Label(self.frameFila, text="Inserir o Indice de Felicidade ", font= "arial 12")
        self.labelHappinessScore.pack()

        self.insertHappinessScore = Entry(self.frameFila)
        self.insertHappinessScore.pack()
        
        self.labelStandardError = Label(self.frameFila, text="Inserir o Erro Padrão ", font= "arial 12")
        self.labelStandardError.pack()

        self.insertStandardError = Entry(self.frameFila)
        self.insertStandardError.pack()

        self.labelEconomy = Label(self.frameFila, text="Inserir o indice de Economia ", font= "arial 12")
        self.labelEconomy.pack()

        self.insertEconomy = Entry(self.frameFila)
        self.insertEconomy.pack()

        self.labelFamily = Label(self.frameFila, text="Inserir o indice de Familia ", font= "arial 12")
        self.labelFamily.pack()

        self.insertFamily = Entry(self.frameFila)
        self.insertFamily.pack()
        
        self.labelHealth = Label(self.frameFila, text="Inserir o indice de Vida ", font= "arial 12")
        self.labelHealth.pack()

        self.insertHealth = Entry(self.frameFila)
        self.insertHealth.pack()

        self.labelFreedom = Label(self.frameFila, text="Inserir o indice de Liberdade ", font= "arial 12")
        self.labelFreedom.pack()

        self.insertFreedom = Entry(self.frameFila)
        self.insertFreedom.pack()

        self.labelTrust = Label(self.frameFila, text="Inserir o indice de Confiança ", font= "arial 12")
        self.labelTrust.pack()

        self.insertTrust = Entry(self.frameFila)
        self.insertTrust.pack()

        self.labelGenerosity = Label(self.frameFila, text="Inserir o indice de Genorosidade ", font= "arial 12")
        self.labelGenerosity.pack()

        self.insertGenerosity = Entry(self.frameFila)
        self.insertGenerosity.pack()

        self.labelDystopiaResidual = Label(self.frameFila, text="Inserir o indice de Distopia Residual ", font= "arial 12")
        self.labelDystopiaResidual.pack()

        self.insertDystopiaResidual = Entry(self.frameFila)
        self.insertDystopiaResidual.pack()
    

        self.salvarData = Button(self.frameFila, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Fila.Pais().insert(str(self.insertName.get()),str(self.insertRegion.get()),
        int(self.insertHappinessRank.get()), float(self.insertHappinessScore.get()), float(self.insertStandardError.get()), float(self.insertEconomy.get()), float(self.insertFamily.get()),
        float(self.insertHealth.get()), float(self.insertFreedom.get()), float(self.insertTrust.get()), float(self.insertGenerosity.get()), float(self.insertDystopiaResidual.get())))
        self.salvarData.pack()

        
        self.returnMain = Button(self.frameFila, bg="red", text="Voltar", bd="5", fg="white",command= self.windowsFila.destroy).pack(pady=12, side="left")

    def editarFilaOption(self):
    
        self.windowsFila = Tk()
        self.windowsFila.title("Fila")
        self.windowsFila.minsize(width = 1280, height= 720)
        self.windowsFila.config(bg="#1d2f38") 
        
        self.frameFila = Frame(self.windowsFila, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameFila.pack()

        self.labelOption = Label(self.frameFila, text="Marque o que deseja Editar",font= "arial 45")
        self.labelOption.config(bg="#1d2f38")
        self.labelOption.pack()

        self.buttonEditarPais = Button(self.frameFila, bg="red", text="Nome do Pais", bd="5", fg="white",width=30,command=self.editarNomeFila).pack(pady=12)
        self.buttonEditarRegion = Button(self.frameFila, bg="red", text="Região", bd="5", fg="white",width=30,command=self.editarRegionFila).pack(pady=12)
        self.buttonEditarHappinessRank = Button(self.frameFila, bg="red", text="Rank de felicidade", bd="5", fg="white",width=30,command=self.editarHappinessRankFila).pack(pady=12)
        self.buttonEditarHappinessScore = Button(self.frameFila, bg="red", text="Score de Felicidade", bd="5", fg="white",width=30,command=self.editarHappinessScoreFila).pack(pady=12)
        self.buttonEditarStandardError = Button(self.frameFila, bg="red", text="Erro Padrão", bd="5", fg="white",width=30,command=self.editarStandardErrorFila).pack(pady=12)
        self.buttonEditarEconomy = Button(self.frameFila, bg="red", text="Indice de Economia", bd="5", fg="white",width=30,command=self.editarEconomyFila).pack(pady=12)
        self.buttonEditarFamily = Button(self.frameFila, bg="red", text="Indice da Familia", bd="5", fg="white",width=30,command=self.editarFamilyFila).pack(pady=12)
        self.buttonEditarHealth = Button(self.frameFila, bg="red", text="Expectativa de Vida", bd="5", fg="white",width=30,command=self.editarHealthFila).pack(pady=12)
        self.buttonEditarFreedom = Button(self.frameFila, bg="red", text="Indice de Liberdade", bd="5", fg="white",width=30,command=self.editarFreedomFila).pack(pady=12)
        self.buttonEditarTrust = Button(self.frameFila, bg="red", text="Indice de Confiança", bd="5", fg="white",width=30,command=self.editarTrustFila).pack(pady=12)
        self.buttonEditarGenorosity = Button(self.frameFila, bg="red", text="Indice de Generosidade", bd="5", fg="white",width=30,command=self.editarGenorosityFila).pack(pady=12)
        self.buttonEditarDystopiaResidual = Button(self.frameFila, bg="red", text="Distopia Residual", bd="5", fg="white",width=30,command=self.editarDystopiaResidualFila).pack(pady=12)

        self.returnMain = Button(self.frameFila, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsFila.destroy).pack(pady=12,side="left")
        
    def editarNomeFila(self):
        
        self.windowsFila = Tk()
        self.windowsFila.title("Fila")
        self.windowsFila.minsize(width = 1280, height= 720)
        self.windowsFila.config(bg="#1d2f38") 
        
        self.frameFila = Frame(self.windowsFila, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameFila.pack()
        
        self.labelName = Label(self.frameFila, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertNameFila = Entry(self.frameFila)
        self.insertNameFila.pack()
        
        self.labelEditName = Label(self.frameFila, text="Inserir o Novo Nome do Pais",font= "arial 12")
        self.labelEditName.pack()

        self.editNameFila = Entry(self.frameFila)
        self.editNameFila.pack()
        
        self.salvarData = Button(self.frameFila, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Fila.Main().editar(0,str(self.insertNameFila.get()),str(self.editNameFila.get()))).pack(pady=12)
        self.returnMain = Button(self.frameFila, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsFila.destroy).pack(pady=12)
    
    def editarRegionFila(self):
            
        self.windowsFila = Tk()
        self.windowsFila.title("Fila")
        self.windowsFila.minsize(width = 1280, height= 720)
        self.windowsFila.config(bg="#1d2f38") 
        
        self.frameFila = Frame(self.windowsFila, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameFila.pack()
        
        self.labelName = Label(self.frameFila, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertNameFila = Entry(self.frameFila)
        self.insertNameFila.pack()
        
        self.labelEditRegion = Label(self.frameFila, text="Inserir a Nova Região",font= "arial 12")
        self.labelEditRegion.pack()

        self.editRegionFila = Entry(self.frameFila)
        self.editRegionFila.pack()
        
        self.salvarData = Button(self.frameFila, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Fila.Main().editar(1,str(self.insertNameFila.get()),str(self.editRegionFila.get()))).pack(pady=12)
        self.returnMain = Button(self.frameFila, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsFila.destroy).pack(pady=12)
    
    def editarHappinessRankFila(self):
            
        self.windowsFila = Tk()
        self.windowsFila.title("Fila")
        self.windowsFila.minsize(width = 1280, height= 720)
        self.windowsFila.config(bg="#1d2f38") 
        
        self.frameFila = Frame(self.windowsFila, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameFila.pack()
        
        self.labelName = Label(self.frameFila, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertNameFila = Entry(self.frameFila)
        self.insertNameFila.pack()
        
        self.labelEditHappinessRank = Label(self.frameFila, text="Inserir o Novo Rank de Felicidade",font= "arial 12")
        self.labelEditHappinessRank.pack()

        self.editHappinessRankFila = Entry(self.frameFila)
        self.editHappinessRankFila.pack()
        
        self.salvarData = Button(self.frameFila, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Fila.Main().editar(2,str(self.insertNameFila.get()),str(self.editHappinessRankFila.get()))).pack(pady=12)
        self.returnMain = Button(self.frameFila, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsFila.destroy).pack(pady=12)

    def editarHappinessScoreFila(self):
            
        self.windowsFila = Tk()
        self.windowsFila.title("Fila")
        self.windowsFila.minsize(width = 1280, height= 720)
        self.windowsFila.config(bg="#1d2f38") 
        
        self.frameFila = Frame(self.windowsFila, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameFila.pack()
        
        self.labelName = Label(self.frameFila, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertNameFila = Entry(self.frameFila)
        self.insertNameFila.pack()
        
        self.labelEditHappinessScore = Label(self.frameFila, text="Inserir o Novo Score da Felicidade",font= "arial 12")
        self.labelEditHappinessScore.pack()

        self.editHappinessScoreFila = Entry(self.frameFila)
        self.editHappinessScoreFila.pack()
        
        self.salvarData = Button(self.frameFila, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Fila.Main().editar(3,str(self.insertNameFila.get()),str(self.editHappinessScoreFila.get()))).pack(pady=12)
        self.returnMain = Button(self.frameFila, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsFila.destroy).pack(pady=12)

    def editarStandardErrorFila(self):
            
        self.windowsFila = Tk()
        self.windowsFila.title("Fila")
        self.windowsFila.minsize(width = 1280, height= 720)
        self.windowsFila.config(bg="#1d2f38") 
        
        self.frameFila = Frame(self.windowsFila, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameFila.pack()
        
        self.labelName = Label(self.frameFila, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertNameFila = Entry(self.frameFila)
        self.insertNameFila.pack()
        
        self.labelEditStandardError = Label(self.frameFila, text="Inserir o Novo Erro Padrão",font= "arial 12")
        self.labelEditStandardError.pack()

        self.editStandardErrorFila = Entry(self.frameFila)
        self.editStandardErrorFila.pack()
        
        self.salvarData = Button(self.frameFila, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Fila.Main().editar(4,str(self.insertNameFila.get()),str(self.editStandardErrorFila.get()))).pack(pady=12)
        self.returnMain = Button(self.frameFila, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsFila.destroy).pack(pady=12)

    def editarEconomyFila(self):
            
        self.windowsFila = Tk()
        self.windowsFila.title("Fila")
        self.windowsFila.minsize(width = 1280, height= 720)
        self.windowsFila.config(bg="#1d2f38") 
        
        self.frameFila = Frame(self.windowsFila, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameFila.pack()
        
        self.labelName = Label(self.frameFila, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertNameFila = Entry(self.frameFila)
        self.insertNameFila.pack()
        
        self.labelEditEconomy = Label(self.frameFila, text="Inserir o Novo Indice de Economia",font= "arial 12")
        self.labelEditEconomy.pack()

        self.editEconomyFila = Entry(self.frameFila)
        self.editEconomyFila.pack()
        
        self.salvarData = Button(self.frameFila, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Fila.Main().editar(5,str(self.insertNameFila.get()),str(self.editEconomyFila.get()))).pack(pady=12)
        self.returnMain = Button(self.frameFila, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsFila.destroy).pack(pady=12)

    def editarFamilyFila(self):
            
        self.windowsFila = Tk()
        self.windowsFila.title("Fila")
        self.windowsFila.minsize(width = 1280, height= 720)
        self.windowsFila.config(bg="#1d2f38") 
        
        self.frameFila = Frame(self.windowsFila, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameFila.pack()
        
        self.labelName = Label(self.frameFila, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertNameFila = Entry(self.frameFila)
        self.insertNameFila.pack()
        
        self.labelEditFamily = Label(self.frameFila, text="Inserir o Novo Indice da Familia",font= "arial 12")
        self.labelEditFamily.pack()

        self.editFamilyFila = Entry(self.frameFila)
        self.editFamilyFila.pack()
        
        self.salvarData = Button(self.frameFila, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Fila.Main().editar(6,str(self.insertNameFila.get()),str(self.editFamilyFila.get()))).pack(pady=12)
        self.returnMain = Button(self.frameFila, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsFila.destroy).pack(pady=12)

    def editarHealthFila(self):
            
        self.windowsFila = Tk()
        self.windowsFila.title("Fila")
        self.windowsFila.minsize(width = 1280, height= 720)
        self.windowsFila.config(bg="#1d2f38") 
        
        self.frameFila = Frame(self.windowsFila, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameFila.pack()
        
        self.labelName = Label(self.frameFila, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertNameFila = Entry(self.frameFila)
        self.insertNameFila.pack()
        
        self.labelEditHealth = Label(self.frameFila, text="Inserir o Novo Indice da Expectativa de Vida",font= "arial 12")
        self.labelEditHealth.pack()

        self.editHealthFila = Entry(self.frameFila)
        self.editHealthFila.pack()
        
        self.salvarData = Button(self.frameFila, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Fila.Main().editarDado(7,str(self.insertNameFila.get()),str(self.editHealthFila.get()))).pack(pady=12)
        self.returnMain = Button(self.frameFila, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsFila.destroy).pack(pady=12)
    
    def editarFreedomFila(self):
                
        self.windowsFila = Tk()
        self.windowsFila.title("Fila")
        self.windowsFila.minsize(width = 1280, height= 720)
        self.windowsFila.config(bg="#1d2f38") 
        
        self.frameFila = Frame(self.windowsFila, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameFila.pack()
        
        self.labelName = Label(self.frameFila, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertNameFila = Entry(self.frameFila)
        self.insertNameFila.pack()
        
        self.labelEditFreedom = Label(self.frameFila, text="Inserir o Novo Indice de Liberdade",font= "arial 12")
        self.labelEditFreedom.pack()

        self.editFreedomFila = Entry(self.frameFila)
        self.editFreedomFila.pack()
        
        self.salvarData = Button(self.frameFila, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Fila.Main().editarDado(8,str(self.insertNameFila.get()),str(self.editFreedomFila.get()))).pack(pady=12)
        self.returnMain = Button(self.frameFila, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsFila.destroy).pack(pady=12)
    
    def editarTrustFila(self):
                
        self.windowsFila = Tk()
        self.windowsFila.title("Fila")
        self.windowsFila.minsize(width = 1280, height= 720)
        self.windowsFila.config(bg="#1d2f38") 
        
        self.frameFila = Frame(self.windowsFila, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameFila.pack()
        
        self.labelName = Label(self.frameFila, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertNameFila = Entry(self.frameFila)
        self.insertNameFila.pack()
        
        self.labelEditTrust = Label(self.frameFila, text="Inserir o Novo Indice de Confiança",font= "arial 12")
        self.labelEditTrust.pack()

        self.editTrustFila = Entry(self.frameFila)
        self.editTrustFila.pack()
        
        self.salvarData = Button(self.frameFila, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Fila.Main().editarDado(9,str(self.insertNameFila.get()),str(self.editTrustFila.get()))).pack(pady=12)
        self.returnMain = Button(self.frameFila, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsFila.destroy).pack(pady=12)

    def editarGenorosityFila(self):
                
        self.windowsFila = Tk()
        self.windowsFila.title("Fila")
        self.windowsFila.minsize(width = 1280, height= 720)
        self.windowsFila.config(bg="#1d2f38") 
        
        self.frameFila = Frame(self.windowsFila, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameFila.pack()
        
        self.labelName = Label(self.frameFila, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertNameFila = Entry(self.frameFila)
        self.insertNameFila.pack()
        
        self.labelEditGenorosity = Label(self.frameFila, text="Inserir o Novo Indice de Generosidade",font= "arial 12")
        self.labelEditGenorosity.pack()

        self.editGenorosityFila = Entry(self.frameFila)
        self.editGenorosityFila.pack()
        
        self.salvarData = Button(self.frameFila, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Fila.Main().editarDado(10,str(self.insertNameFila.get()),str(self.editGenorosityFila.get()))).pack(pady=12)
        self.returnMain = Button(self.frameFila, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsFila.destroy).pack(pady=12)

    def editarDystopiaResidualFila(self):
                
        self.windowsFila = Tk()
        self.windowsFila.title("Fila")
        self.windowsFila.minsize(width = 1280, height= 720)
        self.windowsFila.config(bg="#1d2f38") 
        
        self.frameFila = Frame(self.windowsFila, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameFila.pack()
        
        self.labelName = Label(self.frameFila, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertNameFila = Entry(self.frameFila)
        self.insertNameFila.pack()
        
        self.labelEditDystopiaResidual = Label(self.frameFila, text="Inserir o Novo Indice de Distopia Residual",font= "arial 12")
        self.labelEditDystopiaResidual.pack()

        self.editDystopiaResidualFila = Entry(self.frameFila)
        self.editDystopiaResidualFila.pack()
        
        self.salvarData = Button(self.frameFila, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Fila.Main().editarDado(11,str(self.insertNameFila.get()),str(self.editDystopiaResidualFila.get()))).pack(pady=12)
        self.returnMain = Button(self.frameFila, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsFila.destroy).pack(pady=12)

    def deletarFila(self):
        
        self.windowsFila = Tk()
        self.windowsFila.title("Fila")
        self.windowsFila.minsize(width = 1280, height= 720)
        self.windowsFila.config(bg="#1d2f38") 
        
        self.frameFila = Frame(self.windowsFila, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameFila.pack()
        
        self.labelName = Label(self.frameFila, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertNameFila = Entry(self.frameFila)
        self.insertNameFila.pack()
        
        
        self.salvarData = Button(self.frameFila, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Fila.Main().deletarDado(str(self.insertNameFila.get()))).pack(pady=12)
        self.returnMain = Button(self.frameFila, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsFila.destroy).pack(pady=12)

class newPilha:
    def optionPilha(self):
        self.windowsPilha = Tk()
        self.windowsPilha.title("Esturuta de Dados")
        self.windowsPilha.minsize(width = 1280, height= 720)
        self.windowsPilha.config(bg="#1d2f38")
        
        self.framePilha = Frame(self.windowsPilha, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.framePilha.pack()

        self.labelOption = Label(self.framePilha, text="Marque a Opção Desejada",font= "arial 45")
        self.labelOption.config(bg="#1d2f38")
        self.labelOption.pack()
        Pilha.Main().iniciar()

        self.buttonCriar = Button(self.framePilha, bg="red", text="Criar Pais", bd="5", fg="white",width=10,command= self.criarPilha).pack(pady=12)
        self.buttonEditar = Button(self.framePilha, bg="red", text="Editar Dados", bd="5", fg="white",width=10,command=self.editarPilhaOption).pack(pady=12)
        self.buttonDeletar = Button(self.framePilha, bg="red", text="Deletar Dados", bd="5", fg="white",width=10,command=self.deletarPilha).pack(pady=12)
        self.buttonMostraItems = Button(self.framePilha, bg="red", text="Mostrar Dados", bd="5", fg="white",width=10,command= lambda: Pilha.Main().showStack()).pack(pady=12)
        self.buttonSalva = Button(self.framePilha, bg="red", text="Salvar Dados", bd="5", fg="white",width=10,command= lambda: Pilha.Main().salvaCSV()).pack(pady=12)
        self.returnMain = Button(self.framePilha, bg="red", text="Voltar", bd="5", fg="white",command= self.windowsPilha.destroy).pack(pady=12, side="left")
    
    def criarPilha(self):
        self.windowsPilha = Tk()
        self.windowsPilha.title("Esturuta de Dados")
        self.windowsPilha.minsize(width = 1280, height= 720)
        self.windowsPilha.config(bg="#1d2f38")

        self.framePilha = Frame(self.windowsPilha, width = 1280, height= 720, bg="white", pady="20")
        self.framePilha.pack()
    
        self.labelName = Label(self.framePilha, text="Inserir o Nome Do Pais",font= "arial 12")
        self.labelName.pack()

        self.insertName = Entry(self.framePilha)
        self.insertName.pack()

        self.labelRegion = Label(self.framePilha, text="Inserir a Região", font= "arial 12")
        self.labelRegion.pack()

        self.insertRegion = Entry(self.framePilha)
        self.insertRegion.pack()

        self.labelHappinessRank = Label(self.framePilha, text="Inserir o Rank de Felicidade ", font= "arial 12")
        self.labelHappinessRank.pack()

        self.insertHappinessRank = Entry(self.framePilha)
        self.insertHappinessRank.pack()
        
        self.labelHappinessScore = Label(self.framePilha, text="Inserir o Indice de Felicidade ", font= "arial 12")
        self.labelHappinessScore.pack()

        self.insertHappinessScore = Entry(self.framePilha)
        self.insertHappinessScore.pack()
        
        self.labelStandardError = Label(self.framePilha, text="Inserir o Erro Padrão ", font= "arial 12")
        self.labelStandardError.pack()

        self.insertStandardError = Entry(self.framePilha)
        self.insertStandardError.pack()

        self.labelEconomy = Label(self.framePilha, text="Inserir o indice de Economia ", font= "arial 12")
        self.labelEconomy.pack()

        self.insertEconomy = Entry(self.framePilha)
        self.insertEconomy.pack()

        self.labelFamily = Label(self.framePilha, text="Inserir o indice de Familia ", font= "arial 12")
        self.labelFamily.pack()

        self.insertFamily = Entry(self.framePilha)
        self.insertFamily.pack()
        
        self.labelHealth = Label(self.framePilha, text="Inserir o indice de Vida ", font= "arial 12")
        self.labelHealth.pack()

        self.insertHealth = Entry(self.framePilha)
        self.insertHealth.pack()

        self.labelFreedom = Label(self.framePilha, text="Inserir o indice de Liberdade ", font= "arial 12")
        self.labelFreedom.pack()

        self.insertFreedom = Entry(self.framePilha)
        self.insertFreedom.pack()

        self.labelTrust = Label(self.framePilha, text="Inserir o indice de Confiança ", font= "arial 12")
        self.labelTrust.pack()

        self.insertTrust = Entry(self.framePilha)
        self.insertTrust.pack()

        self.labelGenerosity = Label(self.framePilha, text="Inserir o indice de Genorosidade ", font= "arial 12")
        self.labelGenerosity.pack()

        self.insertGenerosity = Entry(self.framePilha)
        self.insertGenerosity.pack()

        self.labelDystopiaResidual = Label(self.framePilha, text="Inserir o indice de Distopia Residual ", font= "arial 12")
        self.labelDystopiaResidual.pack()

        self.insertDystopiaResidual = Entry(self.framePilha)
        self.insertDystopiaResidual.pack()
    

        self.salvarData = Button(self.framePilha, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Pilha.Main().criarDado(str(self.insertName.get()),str(self.insertRegion.get()),
        int(self.insertHappinessRank.get()), float(self.insertHappinessScore.get()), float(self.insertStandardError.get()), float(self.insertEconomy.get()), float(self.insertFamily.get()),
        float(self.insertHealth.get()), float(self.insertFreedom.get()), float(self.insertTrust.get()), float(self.insertGenerosity.get()), float(self.insertDystopiaResidual.get())))
        self.salvarData.pack()

        
        self.returnMain = Button(self.framePilha, bg="red", text="Voltar", bd="5", fg="white",command= self.windowsPilha.destroy).pack(pady=12, side="left")

    def editarPilhaOption(self):
    
        self.windowsPilha = Tk()
        self.windowsPilha.title("Pilha")
        self.windowsPilha.minsize(width = 1280, height= 720)
        self.windowsPilha.config(bg="#1d2f38") 
        
        self.framePilha = Frame(self.windowsPilha, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.framePilha.pack()

        self.labelOption = Label(self.framePilha, text="Marque o que deseja Editar",font= "arial 45")
        self.labelOption.config(bg="#1d2f38")
        self.labelOption.pack()

        self.buttonEditarPais = Button(self.framePilha, bg="red", text="Nome do Pais", bd="5", fg="white",width=30,command=self.editarNomePilha).pack(pady=12)
        self.buttonEditarRegion = Button(self.framePilha, bg="red", text="Região", bd="5", fg="white",width=30,command=self.editarRegionPilha).pack(pady=12)
        self.buttonEditarHappinessRank = Button(self.framePilha, bg="red", text="Rank de felicidade", bd="5", fg="white",width=30,command=self.editarHappinessRankPilha).pack(pady=12)
        self.buttonEditarHappinessScore = Button(self.framePilha, bg="red", text="Score de Felicidade", bd="5", fg="white",width=30,command=self.editarHappinessScorePilha).pack(pady=12)
        self.buttonEditarStandardError = Button(self.framePilha, bg="red", text="Erro Padrão", bd="5", fg="white",width=30,command=self.editarStandardErrorPilha).pack(pady=12)
        self.buttonEditarEconomy = Button(self.framePilha, bg="red", text="Indice de Economia", bd="5", fg="white",width=30,command=self.editarEconomyPilha).pack(pady=12)
        self.buttonEditarFamily = Button(self.framePilha, bg="red", text="Indice da Familia", bd="5", fg="white",width=30,command=self.editarFamilyPilha).pack(pady=12)
        self.buttonEditarHealth = Button(self.framePilha, bg="red", text="Expectativa de Vida", bd="5", fg="white",width=30,command=self.editarHealthPilha).pack(pady=12)
        self.buttonEditarFreedom = Button(self.framePilha, bg="red", text="Indice de Liberdade", bd="5", fg="white",width=30,command=self.editarFreedomPilha).pack(pady=12)
        self.buttonEditarTrust = Button(self.framePilha, bg="red", text="Indice de Confiança", bd="5", fg="white",width=30,command=self.editarTrustPilha).pack(pady=12)
        self.buttonEditarGenorosity = Button(self.framePilha, bg="red", text="Indice de Generosidade", bd="5", fg="white",width=30,command=self.editarGenorosityPilha).pack(pady=12)
        self.buttonEditarDystopiaResidual = Button(self.framePilha, bg="red", text="Distopia Residual", bd="5", fg="white",width=30,command=self.editarDystopiaResidualPilha).pack(pady=12)

        self.returnMain = Button(self.framePilha, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsPilha.destroy).pack(pady=12,side="left")
        
    def editarNomePilha(self):
        
        self.windowsPilha = Tk()
        self.windowsPilha.title("Pilha")
        self.windowsPilha.minsize(width = 1280, height= 720)
        self.windowsPilha.config(bg="#1d2f38") 
        
        self.framePilha = Frame(self.windowsPilha, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.framePilha.pack()
        
        self.labelName = Label(self.framePilha, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertNamePilha = Entry(self.framePilha)
        self.insertNamePilha.pack()
        
        self.labelEditName = Label(self.framePilha, text="Inserir o Novo Nome do Pais",font= "arial 12")
        self.labelEditName.pack()

        self.editNamePilha = Entry(self.framePilha)
        self.editNamePilha.pack()
        
        self.salvarData = Button(self.framePilha, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Pilha.Main().editarDado(0,str(self.insertNamePilha.get()),str(self.editNamePilha.get()))).pack(pady=12)
        self.returnMain = Button(self.framePilha, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsPilha.destroy).pack(pady=12)
    
    def editarRegionPilha(self):
            
        self.windowsPilha = Tk()
        self.windowsPilha.title("Pilha")
        self.windowsPilha.minsize(width = 1280, height= 720)
        self.windowsPilha.config(bg="#1d2f38") 
        
        self.framePilha = Frame(self.windowsPilha, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.framePilha.pack()
        
        self.labelName = Label(self.framePilha, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertNamePilha = Entry(self.framePilha)
        self.insertNamePilha.pack()
        
        self.labelEditRegion = Label(self.framePilha, text="Inserir a Nova Região",font= "arial 12")
        self.labelEditRegion.pack()

        self.editRegionPilha = Entry(self.framePilha)
        self.editRegionPilha.pack()
        
        self.salvarData = Button(self.framePilha, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Pilha.Main().editarDado(1,str(self.insertNamePilha.get()),str(self.editRegionPilha.get()))).pack(pady=12)
        self.returnMain = Button(self.framePilha, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsPilha.destroy).pack(pady=12)
    
    def editarHappinessRankPilha(self):
            
        self.windowsPilha = Tk()
        self.windowsPilha.title("Pilha")
        self.windowsPilha.minsize(width = 1280, height= 720)
        self.windowsPilha.config(bg="#1d2f38") 
        
        self.framePilha = Frame(self.windowsPilha, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.framePilha.pack()
        
        self.labelName = Label(self.framePilha, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertNamePilha = Entry(self.framePilha)
        self.insertNamePilha.pack()
        
        self.labelEditHappinessRank = Label(self.framePilha, text="Inserir o Novo Rank de Felicidade",font= "arial 12")
        self.labelEditHappinessRank.pack()

        self.editHappinessRankPilha = Entry(self.framePilha)
        self.editHappinessRankPilha.pack()
        
        self.salvarData = Button(self.framePilha, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Pilha.Main().editarDado(2,str(self.insertNamePilha.get()),str(self.editHappinessRankPilha.get()))).pack(pady=12)
        self.returnMain = Button(self.framePilha, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsPilha.destroy).pack(pady=12)

    def editarHappinessScorePilha(self):
            
        self.windowsPilha = Tk()
        self.windowsPilha.title("Pilha")
        self.windowsPilha.minsize(width = 1280, height= 720)
        self.windowsPilha.config(bg="#1d2f38") 
        
        self.framePilha = Frame(self.windowsPilha, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.framePilha.pack()
        
        self.labelName = Label(self.framePilha, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertNamePilha = Entry(self.framePilha)
        self.insertNamePilha.pack()
        
        self.labelEditHappinessScore = Label(self.framePilha, text="Inserir o Novo Score da Felicidade",font= "arial 12")
        self.labelEditHappinessScore.pack()

        self.editHappinessScorePilha = Entry(self.framePilha)
        self.editHappinessScorePilha.pack()
        
        self.salvarData = Button(self.framePilha, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Pilha.Main().editarDado(3,str(self.insertNamePilha.get()),str(self.editHappinessScorePilha.get()))).pack(pady=12)
        self.returnMain = Button(self.framePilha, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsPilha.destroy).pack(pady=12)

    def editarStandardErrorPilha(self):
            
        self.windowsPilha = Tk()
        self.windowsPilha.title("Pilha")
        self.windowsPilha.minsize(width = 1280, height= 720)
        self.windowsPilha.config(bg="#1d2f38") 
        
        self.framePilha = Frame(self.windowsPilha, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.framePilha.pack()
        
        self.labelName = Label(self.framePilha, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertNamePilha = Entry(self.framePilha)
        self.insertNamePilha.pack()
        
        self.labelEditStandardError = Label(self.framePilha, text="Inserir o Novo Erro Padrão",font= "arial 12")
        self.labelEditStandardError.pack()

        self.editStandardErrorPilha = Entry(self.framePilha)
        self.editStandardErrorPilha.pack()
        
        self.salvarData = Button(self.framePilha, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Pilha.Main().editarDado(4,str(self.insertNamePilha.get()),str(self.editStandardErrorPilha.get()))).pack(pady=12)
        self.returnMain = Button(self.framePilha, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsPilha.destroy).pack(pady=12)

    def editarEconomyPilha(self):
            
        self.windowsPilha = Tk()
        self.windowsPilha.title("Pilha")
        self.windowsPilha.minsize(width = 1280, height= 720)
        self.windowsPilha.config(bg="#1d2f38") 
        
        self.framePilha = Frame(self.windowsPilha, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.framePilha.pack()
        
        self.labelName = Label(self.framePilha, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertNamePilha = Entry(self.framePilha)
        self.insertNamePilha.pack()
        
        self.labelEditEconomy = Label(self.framePilha, text="Inserir o Novo Indice de Economia",font= "arial 12")
        self.labelEditEconomy.pack()

        self.editEconomyPilha = Entry(self.framePilha)
        self.editEconomyPilha.pack()
        
        self.salvarData = Button(self.framePilha, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Pilha.Main().editarDado(5,str(self.insertNamePilha.get()),str(self.editEconomyPilha.get()))).pack(pady=12)
        self.returnMain = Button(self.framePilha, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsPilha.destroy).pack(pady=12)

    def editarFamilyPilha(self):
            
        self.windowsPilha = Tk()
        self.windowsPilha.title("Pilha")
        self.windowsPilha.minsize(width = 1280, height= 720)
        self.windowsPilha.config(bg="#1d2f38") 
        
        self.framePilha = Frame(self.windowsPilha, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.framePilha.pack()
        
        self.labelName = Label(self.framePilha, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertNamePilha = Entry(self.framePilha)
        self.insertNamePilha.pack()
        
        self.labelEditFamily = Label(self.framePilha, text="Inserir o Novo Indice da Familia",font= "arial 12")
        self.labelEditFamily.pack()

        self.editFamilyPilha = Entry(self.framePilha)
        self.editFamilyPilha.pack()
        
        self.salvarData = Button(self.framePilha, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Pilha.Main().editarDado(6,str(self.insertNamePilha.get()),str(self.editFamilyPilha.get()))).pack(pady=12)
        self.returnMain = Button(self.framePilha, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsPilha.destroy).pack(pady=12)

    def editarHealthPilha(self):
            
        self.windowsPilha = Tk()
        self.windowsPilha.title("Pilha")
        self.windowsPilha.minsize(width = 1280, height= 720)
        self.windowsPilha.config(bg="#1d2f38") 
        
        self.framePilha = Frame(self.windowsPilha, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.framePilha.pack()
        
        self.labelName = Label(self.framePilha, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertNamePilha = Entry(self.framePilha)
        self.insertNamePilha.pack()
        
        self.labelEditHealth = Label(self.framePilha, text="Inserir o Novo Indice da Expectativa de Vida",font= "arial 12")
        self.labelEditHealth.pack()

        self.editHealthPilha = Entry(self.framePilha)
        self.editHealthPilha.pack()
        
        self.salvarData = Button(self.framePilha, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Pilha.Main().editarDado(7,str(self.insertNamePilha.get()),str(self.editHealthPilha.get()))).pack(pady=12)
        self.returnMain = Button(self.framePilha, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsPilha.destroy).pack(pady=12)
    
    def editarFreedomPilha(self):
                
        self.windowsPilha = Tk()
        self.windowsPilha.title("Pilha")
        self.windowsPilha.minsize(width = 1280, height= 720)
        self.windowsPilha.config(bg="#1d2f38") 
        
        self.framePilha = Frame(self.windowsPilha, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.framePilha.pack()
        
        self.labelName = Label(self.framePilha, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertNamePilha = Entry(self.framePilha)
        self.insertNamePilha.pack()
        
        self.labelEditFreedom = Label(self.framePilha, text="Inserir o Novo Indice de Liberdade",font= "arial 12")
        self.labelEditFreedom.pack()

        self.editFreedomPilha = Entry(self.framePilha)
        self.editFreedomPilha.pack()
        
        self.salvarData = Button(self.framePilha, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Pilha.Main().editarDado(8,str(self.insertNamePilha.get()),str(self.editFreedomPilha.get()))).pack(pady=12)
        self.returnMain = Button(self.framePilha, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsPilha.destroy).pack(pady=12)
    
    def editarTrustPilha(self):
                
        self.windowsPilha = Tk()
        self.windowsPilha.title("Pilha")
        self.windowsPilha.minsize(width = 1280, height= 720)
        self.windowsPilha.config(bg="#1d2f38") 
        
        self.framePilha = Frame(self.windowsPilha, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.framePilha.pack()
        
        self.labelName = Label(self.framePilha, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertNamePilha = Entry(self.framePilha)
        self.insertNamePilha.pack()
        
        self.labelEditTrust = Label(self.framePilha, text="Inserir o Novo Indice de Confiança",font= "arial 12")
        self.labelEditTrust.pack()

        self.editTrustPilha = Entry(self.framePilha)
        self.editTrustPilha.pack()
        
        self.salvarData = Button(self.framePilha, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Pilha.Main().editarDado(9,str(self.insertNamePilha.get()),str(self.editTrustPilha.get()))).pack(pady=12)
        self.returnMain = Button(self.framePilha, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsPilha.destroy).pack(pady=12)

    def editarGenorosityPilha(self):
                
        self.windowsPilha = Tk()
        self.windowsPilha.title("Pilha")
        self.windowsPilha.minsize(width = 1280, height= 720)
        self.windowsPilha.config(bg="#1d2f38") 
        
        self.framePilha = Frame(self.windowsPilha, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.framePilha.pack()
        
        self.labelName = Label(self.framePilha, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertNamePilha = Entry(self.framePilha)
        self.insertNamePilha.pack()
        
        self.labelEditGenorosity = Label(self.framePilha, text="Inserir o Novo Indice de Generosidade",font= "arial 12")
        self.labelEditGenorosity.pack()

        self.editGenorosityPilha = Entry(self.framePilha)
        self.editGenorosityPilha.pack()
        
        self.salvarData = Button(self.framePilha, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Pilha.Main().editarDado(10,str(self.insertNamePilha.get()),str(self.editGenorosityPilha.get()))).pack(pady=12)
        self.returnMain = Button(self.framePilha, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsPilha.destroy).pack(pady=12)

    def editarDystopiaResidualPilha(self):
                
        self.windowsPilha = Tk()
        self.windowsPilha.title("Pilha")
        self.windowsPilha.minsize(width = 1280, height= 720)
        self.windowsPilha.config(bg="#1d2f38") 
        
        self.framePilha = Frame(self.windowsPilha, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.framePilha.pack()
        
        self.labelName = Label(self.framePilha, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertNamePilha = Entry(self.framePilha)
        self.insertNamePilha.pack()
        
        self.labelEditDystopiaResidual = Label(self.framePilha, text="Inserir o Novo Indice de Distopia Residual",font= "arial 12")
        self.labelEditDystopiaResidual.pack()

        self.editDystopiaResidualPilha = Entry(self.framePilha)
        self.editDystopiaResidualPilha.pack()
        
        self.salvarData = Button(self.framePilha, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Pilha.Main().editarDado(11,str(self.insertNamePilha.get()),str(self.editDystopiaResidualPilha.get()))).pack(pady=12)
        self.returnMain = Button(self.framePilha, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsPilha.destroy).pack(pady=12)

    def deletarPilha(self):
        
        self.windowsPilha = Tk()
        self.windowsPilha.title("Pilha")
        self.windowsPilha.minsize(width = 1280, height= 720)
        self.windowsPilha.config(bg="#1d2f38") 
        
        self.framePilha = Frame(self.windowsPilha, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.framePilha.pack()
        
        self.labelName = Label(self.framePilha, text="Inserir o Nome Do Pais Que deseja Editar",font= "arial 12")
        self.labelName.pack()

        self.insertNamePilha = Entry(self.framePilha)
        self.insertNamePilha.pack()
        
        
        self.salvarData = Button(self.framePilha, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Pilha.Main().deletarDado(str(self.insertNamePilha.get()))).pack(pady=12)
        self.returnMain = Button(self.framePilha, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsPilha.destroy).pack(pady=12)

class newTree:
    
    def ordernarTree(self,value):
        if value == '1':
            self.optionTree(1)
            return
        if value == '2':
            self.optionTree(2)
            return
        if value == '3':
            self.optionTree(3)
            return
        else:
            messagebox.showerror("Error", "Opção Invalida")

    def optionOrdnenarTree(self):
        self.windowsTree = Tk()
        self.windowsTree.title("Esturuta de Dados")
        self.windowsTree.minsize(width = 1280, height= 720)
        self.windowsTree.config(bg="#1d2f38")
        
        self.frameTree = Frame(self.windowsTree, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameTree.pack()

        self.labelOption = Label(self.frameTree, text="Marque a Opção Desejada",font= "arial 45")
        self.labelOption.config(bg="#1d2f38")
        self.labelOption.pack()
        
        self.labelEscolha1 = Label(self.frameTree, text="Como deseja ordenar os dados",font= "arial 20")
        self.labelEscolha1.pack(padx=12)

        self.labelEscolha = Label(self.frameTree, text="1-Rank\n\n 2-Economia\n\n 3- Expectativa de Vida",font= "arial 16")
        self.labelEscolha.pack()
        
        self.insertEscolha = Entry(self.frameTree)
        self.insertEscolha.pack()

        self.buttonCriar = Button(self.frameTree, bg="red", text="Ordenar", bd="5", fg="white",width=10,command= lambda: self.ordernarTree(self.insertEscolha.get())).pack(padx=12)
    
    def optionTree(self,esc):
        global value
        value = esc 
        self.windowsTree = Tk()
        self.windowsTree.title("Esturuta de Dados")
        self.windowsTree.minsize(width = 1280, height= 720)
        self.windowsTree.config(bg="#1d2f38")
        
        self.frameTree = Frame(self.windowsTree, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameTree.pack()

        self.labelOption = Label(self.frameTree, text="Marque a Opção Desejada",font= "arial 45")
        self.labelOption.config(bg="#1d2f38")
        self.labelOption.pack()
        
        retorno,escolha,rank = Tree.Main().iniciar(esc)
    
        self.buttonCriar = Button(self.frameTree, bg="red", text="Criar", bd="5", fg="white",width=10,command=lambda: self.criarTree(retorno,escolha,rank)).pack(pady=12)
        self.buttonEditar = Button(self.frameTree, bg="red", text="Editar Dados", bd="5", fg="white",width=10,command=self.editarTreeOption).pack(pady=12)
        self.buttonDeletar = Button(self.frameTree, bg="red", text="Deletar Dados", bd="5", fg="white",width=10,command=self.deletarTree).pack(pady=12)
        self.buttonMostraItems = Button(self.frameTree, bg="red", text="Mostrar Dados", bd="5", fg="white",width=10,command= lambda: Tree.Main().showTree()).pack(pady=12)
        self.buttonSalva = Button(self.frameTree, bg="red", text="Salvar Dados", bd="5", fg="white",width=10,command= lambda: Tree.Main().saveNewDataCsv()).pack(pady=12)
        self.returnMain = Button(self.frameTree, bg="red", text="Voltar", bd="5", fg="white",command= self.windowsTree.destroy).pack(pady=12, side="left")

    def criarTree(self,retorno,escolha,rank):

        self.windowsTree = Tk()
        self.windowsTree.title("Esturuta de Dados")
        self.windowsTree.minsize(width = 1280, height= 720)
        self.windowsTree.config(bg="#1d2f38")

        self.frameTree = Frame(self.windowsTree, width = 1280, height= 720, bg="white", pady="20")
        self.frameTree.pack()
    
        self.labelName = Label(self.frameTree, text="Inserir o Nome Do Pais",font= "arial 12")
        self.labelName.pack()

        self.insertName = Entry(self.frameTree)
        self.insertName.pack()

        self.labelRegion = Label(self.frameTree, text="Inserir a Região", font= "arial 12")
        self.labelRegion.pack()

        self.insertRegion = Entry(self.frameTree)
        self.insertRegion.pack()

        self.labelHappinessRank = Label(self.frameTree, text="Inserir o Rank de Felicidade ", font= "arial 12")
        self.labelHappinessRank.pack()

        self.insertHappinessRank = Entry(self.frameTree)
        self.insertHappinessRank.pack()
        
        self.labelHappinessScore = Label(self.frameTree, text="Inserir o Indice de Felicidade ", font= "arial 12")
        self.labelHappinessScore.pack()

        self.insertHappinessScore = Entry(self.frameTree)
        self.insertHappinessScore.pack()
        
        self.labelStandardError = Label(self.frameTree, text="Inserir o Erro Padrão ", font= "arial 12")
        self.labelStandardError.pack()

        self.insertStandardError = Entry(self.frameTree)
        self.insertStandardError.pack()

        self.labelEconomy = Label(self.frameTree, text="Inserir o indice de Economia ", font= "arial 12")
        self.labelEconomy.pack()

        self.insertEconomy = Entry(self.frameTree)
        self.insertEconomy.pack()

        self.labelFamily = Label(self.frameTree, text="Inserir o indice de Familia ", font= "arial 12")
        self.labelFamily.pack()

        self.insertFamily = Entry(self.frameTree)
        self.insertFamily.pack()
        
        self.labelHealth = Label(self.frameTree, text="Inserir o indice de Vida ", font= "arial 12")
        self.labelHealth.pack()

        self.insertHealth = Entry(self.frameTree)
        self.insertHealth.pack()

        self.labelFreedom = Label(self.frameTree, text="Inserir o indice de Liberdade ", font= "arial 12")
        self.labelFreedom.pack()

        self.insertFreedom = Entry(self.frameTree)
        self.insertFreedom.pack()

        self.labelTrust = Label(self.frameTree, text="Inserir o indice de Confiança ", font= "arial 12")
        self.labelTrust.pack()

        self.insertTrust = Entry(self.frameTree)
        self.insertTrust.pack()

        self.labelGenerosity = Label(self.frameTree, text="Inserir o indice de Genorosidade ", font= "arial 12")
        self.labelGenerosity.pack()

        self.insertGenerosity = Entry(self.frameTree)
        self.insertGenerosity.pack()

        self.labelDystopiaResidual = Label(self.frameTree, text="Inserir o indice de Distopia Residual ", font= "arial 12")
        self.labelDystopiaResidual.pack()

        self.insertDystopiaResidual = Entry(self.frameTree)
        self.insertDystopiaResidual.pack()
  

        self.salvarData = Button(self.frameTree, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Tree.Pais().insert(escolha,retorno,str(self.insertName.get()),str(self.insertRegion.get()),
        int(self.insertHappinessRank.get()), float(self.insertHappinessScore.get()), float(self.insertStandardError.get()), float(self.insertEconomy.get()), float(self.insertFamily.get()),
        float(self.insertHealth.get()), float(self.insertFreedom.get()), float(self.insertTrust.get()), float(self.insertGenerosity.get()), float(self.insertDystopiaResidual.get())))
        self.salvarData.pack()

        
        self.returnMain = Button(self.frameTree, bg="red", text="Voltar", bd="5", fg="white",command= self.windowsTree.destroy).pack(pady=12, side="left")

    def editarTreeOption(self):
    
        self.windowsTree = Tk()
        self.windowsTree.title("Tree")
        self.windowsTree.minsize(width = 1280, height= 720)
        self.windowsTree.config(bg="#1d2f38") 
        
        self.frameTree = Frame(self.windowsTree, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameTree.pack()

        self.labelOption = Label(self.frameTree, text="Marque o que deseja Editar",font= "arial 45")
        self.labelOption.config(bg="#1d2f38")
        self.labelOption.pack()

        self.buttonEditarPais = Button(self.frameTree, bg="red", text="Nome do Pais", bd="5", fg="white",width=30,command=self.editarNomeTree).pack(pady=12)
        self.buttonEditarRegion = Button(self.frameTree, bg="red", text="Região", bd="5", fg="white",width=30,command=self.editarRegionTree).pack(pady=12)
        #self.buttonEditarHappinessRank = Button(self.frameTree, bg="red", text="Rank de felicidade", bd="5", fg="white",width=30,command=self.editarHappinessRankTree).pack(pady=12)
        self.buttonEditarHappinessScore = Button(self.frameTree, bg="red", text="Score de Felicidade", bd="5", fg="white",width=30,command=self.editarHappinessScoreTree).pack(pady=12)
        self.buttonEditarStandardError = Button(self.frameTree, bg="red", text="Erro Padrão", bd="5", fg="white",width=30,command=self.editarStandardErrorTree).pack(pady=12)
        #self.buttonEditarEconomy = Button(self.frameTree, bg="red", text="Indice de Economia", bd="5", fg="white",width=30,command=self.editarEconomyTree).pack(pady=12)
        self.buttonEditarFamily = Button(self.frameTree, bg="red", text="Indice da Familia", bd="5", fg="white",width=30,command=self.editarFamilyTree).pack(pady=12)
        #self.buttonEditarHealth = Button(self.frameTree, bg="red", text="Expectativa de Vida", bd="5", fg="white",width=30,command=self.editarHealthTree).pack(pady=12)
        self.buttonEditarFreedom = Button(self.frameTree, bg="red", text="Indice de Liberdade", bd="5", fg="white",width=30,command=self.editarFreedomTree).pack(pady=12)
        self.buttonEditarTrust = Button(self.frameTree, bg="red", text="Indice de Confiança", bd="5", fg="white",width=30,command=self.editarTrustTree).pack(pady=12)
        self.buttonEditarGenorosity = Button(self.frameTree, bg="red", text="Indice de Generosidade", bd="5", fg="white",width=30,command=self.editarGenorosityTree).pack(pady=12)
        self.buttonEditarDystopiaResidual = Button(self.frameTree, bg="red", text="Distopia Residual", bd="5", fg="white",width=30,command=self.editarDystopiaResidualTree).pack(pady=12)

        self.returnMain = Button(self.frameTree, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsTree.destroy).pack(pady=12,side="left")
        
    def editarNomeTree(self):
        
        self.windowsTree = Tk()
        self.windowsTree.title("Tree")
        self.windowsTree.minsize(width = 1280, height= 720)
        self.windowsTree.config(bg="#1d2f38") 
        
        self.frameTree = Frame(self.windowsTree, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameTree.pack()
        
        self.labelId = Label(self.frameTree, text="Inserir o Id  Do Pais Que deseja Editar (ID = Rank de felicidade)",font= "arial 12")
        self.labelId.pack()

        self.insertIdTree = Entry(self.frameTree)
        self.insertIdTree.pack()
        
        self.labelEditName = Label(self.frameTree, text="Inserir o Novo Nome do Pais",font= "arial 12")
        self.labelEditName.pack()

        self.editNameTree = Entry(self.frameTree)
        self.editNameTree.pack()
        
        self.salvarData = Button(self.frameTree, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Tree.Pais().editar(1,str(self.insertIdTree.get()),str(self.editNameTree.get()))).pack(pady=12)
        self.returnMain = Button(self.frameTree, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsTree.destroy).pack(pady=12)
    
    def editarRegionTree(self):
            
        self.windowsTree = Tk()
        self.windowsTree.title("Tree")
        self.windowsTree.minsize(width = 1280, height= 720)
        self.windowsTree.config(bg="#1d2f38") 
        
        self.frameTree = Frame(self.windowsTree, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameTree.pack()
        
        self.labelId = Label(self.frameTree, text="Inserir o Id  Do Pais Que deseja Editar (ID = Rank de felicidade)",font= "arial 12")
        self.labelId.pack()

        self.insertIdTree = Entry(self.frameTree)
        self.insertIdTree.pack()

        self.labelEditRegion = Label(self.frameTree, text="Inserir a Nova Região",font= "arial 12")
        self.labelEditRegion.pack()

        self.editRegionTree = Entry(self.frameTree)
        self.editRegionTree.pack()
        
        self.salvarData = Button(self.frameTree, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Tree.Main().editar(2,str(self.insertIdTree.get()),str(self.editRegionTree.get()))).pack(pady=12)
        self.returnMain = Button(self.frameTree, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsTree.destroy).pack(pady=12)
     
    def editarHappinessScoreTree(self):
            
        self.windowsTree = Tk()
        self.windowsTree.title("Tree")
        self.windowsTree.minsize(width = 1280, height= 720)
        self.windowsTree.config(bg="#1d2f38") 
        
        self.frameTree = Frame(self.windowsTree, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameTree.pack()
        
        self.labelId = Label(self.frameTree, text="Inserir o Id  Do Pais Que deseja Editar (ID = Rank de felicidade)",font= "arial 12")
        self.labelId.pack()

        self.insertIdTree = Entry(self.frameTree)
        self.insertIdTree.pack()
        
        self.labelEditHappinessScore = Label(self.frameTree, text="Inserir o Novo Score da Felicidade",font= "arial 12")
        self.labelEditHappinessScore.pack()

        self.editHappinessScoreTree = Entry(self.frameTree)
        self.editHappinessScoreTree.pack()
        
        self.salvarData = Button(self.frameTree, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Tree.Main().editar(3,str(self.insertIdTree.get()),str(self.editHappinessScoreTree.get()))).pack(pady=12)
        self.returnMain = Button(self.frameTree, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsTree.destroy).pack(pady=12)

    def editarStandardErrorTree(self):
            
        self.windowsTree = Tk()
        self.windowsTree.title("Tree")
        self.windowsTree.minsize(width = 1280, height= 720)
        self.windowsTree.config(bg="#1d2f38") 
        
        self.frameTree = Frame(self.windowsTree, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameTree.pack()
        
        self.labelId = Label(self.frameTree, text="Inserir o Id  Do Pais Que deseja Editar (ID = Rank de felicidade)",font= "arial 12")
        self.labelId.pack()

        self.insertIdTree = Entry(self.frameTree)
        self.insertIdTree.pack()
        
        self.labelEditStandardError = Label(self.frameTree, text="Inserir o Novo Erro Padrão",font= "arial 12")
        self.labelEditStandardError.pack()

        self.editStandardErrorTree = Entry(self.frameTree)
        self.editStandardErrorTree.pack()
        
        self.salvarData = Button(self.frameTree, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Tree.Main().editar(4,str(self.insertIdTree.get()),str(self.editStandardErrorTree.get()))).pack(pady=12)
        self.returnMain = Button(self.frameTree, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsTree.destroy).pack(pady=12)

    def editarFamilyTree(self):
            
        self.windowsTree = Tk()
        self.windowsTree.title("Tree")
        self.windowsTree.minsize(width = 1280, height= 720)
        self.windowsTree.config(bg="#1d2f38") 
        
        self.frameTree = Frame(self.windowsTree, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameTree.pack()
        
        self.labelId = Label(self.frameTree, text="Inserir o Id  Do Pais Que deseja Editar (ID = Rank de felicidade)",font= "arial 12")
        self.labelId.pack()

        self.insertIdTree = Entry(self.frameTree)
        self.insertIdTree.pack()
        
        self.labelEditFamily = Label(self.frameTree, text="Inserir o Novo Indice da Familia",font= "arial 12")
        self.labelEditFamily.pack()

        self.editFamilyTree = Entry(self.frameTree)
        self.editFamilyTree.pack()
        
        self.salvarData = Button(self.frameTree, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Tree.Main().editar(5,str(self.insertIdTree.get()),str(self.editFamilyTree.get()))).pack(pady=12)
        self.returnMain = Button(self.frameTree, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsTree.destroy).pack(pady=12)
    
    def editarFreedomTree(self):
                
        self.windowsTree = Tk()
        self.windowsTree.title("Tree")
        self.windowsTree.minsize(width = 1280, height= 720)
        self.windowsTree.config(bg="#1d2f38") 
        
        self.frameTree = Frame(self.windowsTree, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameTree.pack()
        
        self.labelId = Label(self.frameTree, text="Inserir o Id  Do Pais Que deseja Editar (ID = Rank de felicidade)",font= "arial 12")
        self.labelId.pack()

        self.insertIdTree = Entry(self.frameTree)
        self.insertIdTree.pack()
        
        self.labelEditFreedom = Label(self.frameTree, text="Inserir o Novo Indice de Liberdade",font= "arial 12")
        self.labelEditFreedom.pack()

        self.editFreedomTree = Entry(self.frameTree)
        self.editFreedomTree.pack()
        
        self.salvarData = Button(self.frameTree, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Tree.Main().editar(6,str(self.insertIdTree.get()),str(self.editFreedomTree.get()))).pack(pady=12)
        self.returnMain = Button(self.frameTree, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsTree.destroy).pack(pady=12)
    
    def editarTrustTree(self):
                
        self.windowsTree = Tk()
        self.windowsTree.title("Tree")
        self.windowsTree.minsize(width = 1280, height= 720)
        self.windowsTree.config(bg="#1d2f38") 
        
        self.frameTree = Frame(self.windowsTree, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameTree.pack()
        
        self.labelId = Label(self.frameTree, text="Inserir o Id  Do Pais Que deseja Editar (ID = Rank de felicidade)",font= "arial 12")
        self.labelId.pack()

        self.insertIdTree = Entry(self.frameTree)
        self.insertIdTree.pack()
        
        self.labelEditTrust = Label(self.frameTree, text="Inserir o Novo Indice de Confiança",font= "arial 12")
        self.labelEditTrust.pack()

        self.editTrustTree = Entry(self.frameTree)
        self.editTrustTree.pack()
        
        self.salvarData = Button(self.frameTree, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Tree.Main().editar(7,str(self.insertIdTree.get()),str(self.editTrustTree.get()))).pack(pady=12)
        self.returnMain = Button(self.frameTree, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsTree.destroy).pack(pady=12)

    def editarGenorosityTree(self):
                
        self.windowsTree = Tk()
        self.windowsTree.title("Tree")
        self.windowsTree.minsize(width = 1280, height= 720)
        self.windowsTree.config(bg="#1d2f38") 
        
        self.frameTree = Frame(self.windowsTree, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameTree.pack()
        
        self.labelId = Label(self.frameTree, text="Inserir o Id  Do Pais Que deseja Editar (ID = Rank de felicidade)",font= "arial 12")
        self.labelId.pack()

        self.insertIdTree = Entry(self.frameTree)
        self.insertIdTree.pack()
        
        self.labelEditGenorosity = Label(self.frameTree, text="Inserir o Novo Indice de Generosidade",font= "arial 12")
        self.labelEditGenorosity.pack()

        self.editGenorosityTree = Entry(self.frameTree)
        self.editGenorosityTree.pack()
        
        self.salvarData = Button(self.frameTree, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Tree.Main().editar(8,str(self.insertIdTree.get()),str(self.editGenorosityTree.get()))).pack(pady=12)
        self.returnMain = Button(self.frameTree, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsTree.destroy).pack(pady=12)

    def editarDystopiaResidualTree(self):
                
        self.windowsTree = Tk()
        self.windowsTree.title("Tree")
        self.windowsTree.minsize(width = 1280, height= 720)
        self.windowsTree.config(bg="#1d2f38") 
        
        self.frameTree = Frame(self.windowsTree, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameTree.pack()
        
        self.labelId = Label(self.frameTree, text="Inserir o Id  Do Pais Que deseja Editar (ID = Rank de felicidade)",font= "arial 12")
        self.labelId.pack()

        self.insertIdTree = Entry(self.frameTree)
        self.insertIdTree.pack()
        
        self.labelEditDystopiaResidual = Label(self.frameTree, text="Inserir o Novo Indice de Distopia Residual",font= "arial 12")
        self.labelEditDystopiaResidual.pack()

        self.editDystopiaResidualTree = Entry(self.frameTree)
        self.editDystopiaResidualTree.pack()
        
        self.salvarData = Button(self.frameTree, bg="red", text="SALVAR", bd="0", fg="white",command=lambda: Tree.Main().editar(9,str(self.insertIdTree.get()),str(self.editDystopiaResidualTree.get()))).pack(pady=12)
        self.returnMain = Button(self.frameTree, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsTree.destroy).pack(pady=12)

    def deletarTree(self):
        if value == 1:
            self.windowsTree = Tk()
            self.windowsTree.title("Tree")
            self.windowsTree.minsize(width = 1280, height= 720)
            self.windowsTree.config(bg="#1d2f38") 
            
            self.frameTree = Frame(self.windowsTree, width = 1280, height= 720, bg="#1d2f38", pady="20")
            self.frameTree.pack()
            
            self.labelTitle = Label(self.frameTree, text = "Exclusão Por ordenação de Rank", font="16")
            self.labelTitle.pack()

            self.labelName = Label(self.frameTree, text="Digite o indice do pais deseja remover: ",font= "arial 12")
            self.labelName.pack()
            
            self.insertNameTree = Entry(self.frameTree)
            self.insertNameTree.pack()
            
            self.salvarData = Button(self.frameTree, bg="red", text="Deletar", bd="0", fg="white",command=lambda: Tree.Main().removeHappinessRank(int(self.insertNameTree.get()))).pack(pady=12)
            
        
        if value == 2:
            self.windowsTree = Tk()
            self.windowsTree.title("Tree")
            self.windowsTree.minsize(width = 1280, height= 720)
            self.windowsTree.config(bg="#1d2f38") 
            
            self.frameTree = Frame(self.windowsTree, width = 1280, height= 720, bg="#1d2f38", pady="20")
            self.frameTree.pack()
            
            self.labelTitle = Label(self.frameTree, text = "Exclusão Por ordenação de Economia", font="16")
            self.labelTitle.pack()

            self.labelName = Label(self.frameTree, text="Digite o indice de Economia que deseja remover: ",font= "arial 12")
            self.labelName.pack() 

            self.insertNameTree = Entry(self.frameTree)
            self.insertNameTree.pack()
        
            self.salvarData = Button(self.frameTree, bg="red", text="Deletar", bd="0", fg="white",command=lambda: Tree.Main().removeEconomy(float(self.insertNameTree.get()))).pack(pady=12)
        
        if value == 3:
            self.windowsTree = Tk()
            self.windowsTree.title("Tree")
            self.windowsTree.minsize(width = 1280, height= 720)
            self.windowsTree.config(bg="#1d2f38") 
            
            self.frameTree = Frame(self.windowsTree, width = 1280, height= 720, bg="#1d2f38", pady="20")
            self.frameTree.pack()
            
            self.labelTitle = Label(self.frameTree, text = "Exclusão Por ordenação de Expectativa de vida", font="16")
            self.labelTitle.pack()

            self.labelName = Label(self.frameTree, text="Digite o indice de Expectativa de vida que deseja remover: ",font= "arial 12")
            self.labelName.pack() 

            self.insertNameTree = Entry(self.frameTree)
            self.insertNameTree.pack()
        
            self.salvarData = Button(self.frameTree, bg="red", text="Deletar", bd="0", fg="white",command=lambda: Tree.Main().removeHealth(float(self.insertNameTree.get()))).pack(pady=12)
        
        self.returnMain = Button(self.frameTree, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsTree.destroy).pack(pady=12)

class newGrafo:
    def optionGrafo(self):
        self.windowsGrafo = Tk()
        self.windowsGrafo.title("Esturuta de Dados")
        self.windowsGrafo.minsize(width = 1280, height= 720)
        self.windowsGrafo.config(bg="#1d2f38")
        
        self.frameGrafo = Frame(self.windowsGrafo, width = 1280, height= 720, bg="#1d2f38", pady="20")
        self.frameGrafo.pack()

        self.labelOption = Label(self.frameGrafo, text="Marque a Opção Desejada",font= "arial 45")
        self.labelOption.config(bg="#1d2f38")
        self.labelOption.pack()
        Grafo.Main().iniciar()

        self.buttonBuscar = Button(self.frameGrafo, bg="red", text="Buscar Caminho", bd="5", fg="white",width=20,command= self.buscarGrafo).pack(pady=12)
        self.buttonPrintar = Button(self.frameGrafo, bg="red", text="Printar", bd="5", fg="white",width=20,command=  self.showGrafo).pack(pady=12)
        self.returnMain = Button(self.frameGrafo, bg="red", text="Voltar", bd="5", fg="white",command= self.windowsGrafo.destroy).pack(pady=12, side="left")
    
    def buscarGrafo(self):
        self.windowsGrafo = Tk()
        self.windowsGrafo.title("Grafo")
        self.windowsGrafo.minsize(width = 1280, height= 720)
        self.windowsGrafo.config(bg="#1d2f38")

        self.frameGrafo = Frame(self.windowsGrafo, width = 1280, height= 720, bg="white", pady="20")
        self.frameGrafo.pack()
    
        self.labelNode1 = Label(self.frameGrafo, text="Inserir o Valor do Primeiro Nó",font= "arial 12",width=30)
        self.labelNode1.pack()

        self.insertNode1 = Entry(self.frameGrafo)
        self.insertNode1.pack()

        self.labelNode2 = Label(self.frameGrafo, text="Inserir o Valor do Segundo Nó", font= "arial 12",width=30)
        self.labelNode2.pack()

        self.insertNode2 = Entry(self.frameGrafo)
        self.insertNode2.pack()
        
        self.salvarData = Button(self.frameGrafo, bg="red", text="Buscar", bd="0", fg="white",command= lambda: Grafo.Main().search(int(self.insertNode1.get()), int(self.insertNode2.get()))).pack()

        self.returnMain = Button(self.frameGrafo, bg="red", text="Voltar", bd="0", fg="white",command= self.windowsGrafo.destroy).pack()
    def showGrafo(self):
        self.windowsGrafo = Tk()
        self.windowsGrafo.title("Grafo")
        self.windowsGrafo.minsize(width = 1280, height= 720)
        self.windowsGrafo.config(bg="#1d2f38")
        self.buttonPrintarCaminho = Button(self.windowsGrafo, bg="red", text="Printar Os Caminhos", bd="5", fg="white",width=30,command= lambda: Grafo.Main().showData('1')).pack(pady=12)
        self.buttonPrintarAdjacencia = Button(self.windowsGrafo, bg="red", text="Printar Lista de Adjacencia", bd="5", fg="white",width=30,command= lambda: Grafo.Main().showData('2')).pack(pady=12)
        self.buttonPrintarNos = Button(self.windowsGrafo, bg="red", text="Printar Nós", bd="5", fg="white",width=30,command= lambda: Grafo.Main().showData('3')).pack(pady=12)
        self.returnMain = Button(self.windowsGrafo, bg="red", text="Voltar", bd="5", fg="white",command= self.windowsGrafo.destroy).pack(pady=12)

i = Interface()
