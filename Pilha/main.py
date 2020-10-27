# -*- coding: utf-8 -*-
# Usando módulo interno do python para ler arquivos em ssv
import csv
dados=[]
with open('datas/2015.csv', newline='') as arquivo:
    leitor=csv.reader(arquivo)
    leitor.__next__()
    for linha in leitor:
        dados.append(linha)

# Aqui posso imprimir qualquer linha da tabela
print(len(dados))

# Ou qualquer coluna da linha
#print(dados[5][0])