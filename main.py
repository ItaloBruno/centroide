import csv
import os
from padrao import Padrao
from cluster import Cluster


def leitura_arquivo_csv(nome_arquivo, lista_de_resultados):
    with open(nome_arquivo, "r") as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            if len(linha) == 0:
                continue

            for index, atributo in enumerate(linha[:-1]):
                linha[index] = float(atributo)

            # print(f"padrão a ser classificado: {linha}")
            lista_de_resultados.append(Padrao(linha))

    arquivo.close

    return lista_de_resultados

def leitura_arquivo_de_texto(nome_arquivo, lista_de_resultados):
    with open(nome_arquivo, "r") as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            if len(linha) == 0:
                continue

            for index, atributo in enumerate(linha[:-1]):
                linha[index] = float(atributo)

            # print(f"padrão a ser classificado: {linha}")
            lista_de_resultados.append(Padrao(linha))

    arquivo.close

    return lista_de_resultados

base_de_dados = []
padroes_para_classificar = []
menu_de_opcoes = []
classes_dados = set()

os.system("clear")

passo_a_passo = "passo_a_passo.txt"
menu_de_opcoes = open(passo_a_passo, "r")
print(menu_de_opcoes.read())

nome_tabela_de_dados = "base_de_dados.txt"
nome_tabela_padroes_para_classificar = "dados_para_classificar.txt"

base_de_dados = leitura_arquivo_csv(nome_tabela_de_dados, base_de_dados)
padroes_para_classificar = leitura_arquivo_csv(
    nome_tabela_padroes_para_classificar, padroes_para_classificar
)

# Classificação dos clusters
clusters = []
for dado in base_de_dados:
    classes_dados.add(dado.nome_classe)

# Criação dos clusters com os valores do primeiro elemento correspondente com aquela classe
for num_cluster, nome_classe in enumerate(classes_dados):
    for dado in base_de_dados:
        if dado.lista_de_atributos[-1] == nome_classe:
            clusters.append(
                Cluster(
                    num_cluster, 
                    nome_classe, 
                    len(dado.lista_de_atributos[:-1]), 
                    dado.lista_de_atributos[:-1],
                    dado
                )
            )
            break

print("clusters antes da classificação")
for clus in clusters:
    print(clus)

for dado in base_de_dados:
    menor_distancia = 16844484
    cluster_escolhido = None

    for clus in clusters:
        nova_distancia = clus.calcula_distancia_para_esse_cluster(dado)
        if nova_distancia < menor_distancia:
            menor_distancia = nova_distancia
            cluster_escolhido = clus

    cluster_escolhido.adicionar_elemento(dado)
    cluster_escolhido.calcular_mediana()

print("\nclusters depois da classificação inicial")
for clus in clusters:
    print(clus)

classificacoes_corretas = 0
for padrao in padroes_para_classificar:
    menor_distancia = 16844484
    cluster_escolhido = None

    for clus in clusters:
        nova_distancia = clus.calcula_distancia_para_esse_cluster(padrao)
        if nova_distancia < menor_distancia:
            menor_distancia = nova_distancia
            cluster_escolhido = clus

    cluster_escolhido.adicionar_elemento(padrao)
    cluster_escolhido.calcular_mediana()

    print("\n=================================================================")
    print(f"Padrão a ser classificado: {padrao}\n")
    print(f"Cluster escolhido: {cluster_escolhido.classe_cluster}")
    print("=================================================================\n")
    if padrao.nome_classe == cluster_escolhido.classe_cluster:
        classificacoes_corretas += 1

print(f"Quantidade de instâncias classificadas: {len(padroes_para_classificar)}")
print(f"Acertos: {classificacoes_corretas}")
print(
    f"Taxa de acerto do classificador: {(float(classificacoes_corretas)/len(padroes_para_classificar))*100}"
)

print("\nclusters depois da classificação dos novos dados")
for clus in clusters:
    print(clus)
