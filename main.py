import sys
import csv
import os
import math

class Padrao:
    def __init__(self, lista_de_atributos):
        self.__lista_de_atributos = lista_de_atributos
        self.__nome_classe = lista_de_atributos[-1]

    @property
    def lista_de_atributos(self):
        return self.__lista_de_atributos[:]

    @property
    def nome_classe(self):
        return self.__nome_classe

    def __str__(self):
        return str(self.__lista_de_atributos)


class Cluster:
    def __init__(self, numero_claster, classe_cluster, numero_criterios, mediana_inicial, elemento_inicial):
        self.__numero_claster = numero_claster
        self.__classe_cluster = classe_cluster
        self.__numero_criterios = numero_criterios
        self.__mediana = mediana_inicial
        self.__elementos = [elemento_inicial]

    @property
    def numero_claster(self):
        return self.__numero_claster

    @property
    def classe_cluster(self):
        return self.__classe_cluster

    @property
    def mediana(self):
        return self.mediana[:]

    def __str__(self):
        return f"{str(self.__mediana)} - {self.__numero_claster} - {self.__classe_cluster}"

    def adicionar_elemento(self, novo_elemento):
        self.__elementos.append(novo_elemento)

    def calcula_distancia_para_esse_cluster(self, padrao_a_ser_classificado):
        distancia = 0
        for index, atributo in enumerate(self.__mediana):
            result = padrao_a_ser_classificado.lista_de_atributos[index] - atributo
            distancia += math.pow(result, 2)

        return math.sqrt(distancia)

    def calcular_mediana(self):
        nova_mediana = [0.0 for _ in range(self.__numero_criterios)]
        num_elementos = len(self.__elementos)
        
        if num_elementos > 1:
            for elemento in self.__elementos:
                for indice, parametro in enumerate(elemento.lista_de_atributos[:-1]):
                    nova_mediana[indice] += parametro
            
            for indice, parametro in enumerate(nova_mediana):
                nova_mediana[indice] = nova_mediana[indice]/num_elementos

        self.__mediana = nova_mediana


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

base_de_dados = []
padroes_para_classificar = []
classes_dados = set()

os.system("clear")

print("""
Passo a passo do algoritmo:
1 - ler a base de dados
2 - verificar quantos e quais são os casos específicos existentes nessa base de dados
3 - a partir do resultado acima obtido, estipular um número de clusters
4 - criação dos clusters com a mediana igual ao primeiro elemento de cada tipo (Iris-virginica, Iris-versicolor, Iris-setosa)
5 - calcula a mediana de cada cluster de acordo com os dados usados como base de dados do classificador
6 - adiciona o novo elemento para o cluster com menor distância e recalcula a mediana com o novo elemento adicionado
7 - após esse "treinamento inicial", iremos refazer o passo 6 mas agora com os dados a serem classificados
""")

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
