import math

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