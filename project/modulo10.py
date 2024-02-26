def getProduto(texto):
    novoTexto=texto.replace("\n","")
    Produto=[]
    dados=novoTexto.split(",")
    for i in range(len(dados)):
        Produto.append(dados[i])
    return Produto

def lerDataset(fnome):
    BD=[]
    with open(fnome, encoding='utf-8') as file:
        bd = csv.reader(file, delimiter=',')
        for produto in bd:
            BD.append(produto)
    return BD

def adicionarProduto(bd,nomeBR,preco,image):
    novoProduto=[]
    novoProduto.append(nomeBR)
    if 'Calcola' in nomeBR:
        nomePT=nomeBR.replace('Calcola','Cueca')
        novoProduto.append(nomePT)
    elif 'Cueca' in nomeBR:
        nomePT=nomeBR.replace('Cueca','Boxer')
        novoProduto.append(nomePT)
    elif 'Tanga Fio' in nomeBR:
        nomePT=nomeBR.replace('Tanga Fio', 'Cueca Brasileira')
        novoProduto.append(nomePT)
    elif 'Samba Cancao' in nomeBR:
        nomePT=nomeBR.replace('Samba Cancao','Boxers Largos')
        novoProduto.append(nomePT)
    elif 'Soutien Bojo' in nomeBR:
        nomePT=nomeBR.replace('Soutien Bojo','Soutien Almofadado')
        novoProduto.append(nomePT)
    else:
        nomePT='-----'
        novoProduto.append(nomePT)
    novoProduto.append(preco)
    novoProduto.append(image)
    return novoProduto

from PIL import Image
import csv
from datetime import datetime
from os.path import join
import pandas as pd

def thumb(path):
    #Relative path
    img=Image.open(path)
    #In-place modification
    img.thumbnail((1000,800))
    img.save((path))

def guardarBD(bd):
    f = open('C:/Users/rafay/Desktop/project/DONT_OPEN/produtos.csv', 'w', newline='', encoding='utf-8')
    w = csv.writer(f)
    for produto in bd:
        w.writerow(produto)
    f.close()

def criarNote(bd,fnome,path1):
    with open(join(path1,fnome),'w',encoding='utf-8') as file:
        spamwriter = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Artigo', 'Entregue', 'D','V','P.Unit','Soma'])
        for linha in bd:
            spamwriter.writerow(linha)
    file.close()

def criarNotaExcel(file1,file2):
    read_file = pd.read_csv (file1)
    read_file.to_excel (file2, index = None, header=True)

