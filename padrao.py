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