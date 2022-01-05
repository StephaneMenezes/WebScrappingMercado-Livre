import requests
from bs4 import BeautifulSoup
from requests.models import Response
import pandas as pd

url_base='https://lista.mercadolivre.com.br/'
produto_nome = input("Qual produto você deseja? ")                #Escrever o nome do produto 

print(produto_nome)

response = requests.get(url_base + produto_nome)                  #Adicionar o nome do produto a url base
site = BeautifulSoup(response.text, 'html.parser')                #Transformar o conteúdo para BeautifulSoup 

produto = site.findAll("div", attrs={'class':'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'}) #Div com as informações sobre os produtos
lista_produtos = []                                                #Criar uma lista vazia para criar um Dataframe depois 

for produtos in produto:                                          #Criar um for para que o programa vá pegando todos os produtos, geralmente adicionamos o for no final 
    titulo = produtos.find("h2", attrs={'class':'ui-search-item__title'})          #Tag que vai pegar o nome do produto

    link = produtos.find("a", attrs={'class':'ui-search-item__group__element ui-search-link'})  #Tag que vai pegar a url do produto

    preco = produtos.find("span", attrs={'class':'price-tag-text-sr-only'})                     #Tag que vai pegar os preços dos produtos 

    title = "Produto :",titulo.text,"Valor : ",preco.text                               #Criando um título padronizado para todos os produtos. 

    lista_produtos.append([titulo.text, preco.text, link['href'],title])                         #Criando o dataframe com os dados que eu quero apresentar 

news=pd.DataFrame(lista_produtos, columns=["Título", "Preço","Link","Tag Title"])    #Criando uma lista com os dados
news.to_csv('Listadeprodutos.xlsx', index=False)                                          #Salvando esses dados em uma planilha do excel pen