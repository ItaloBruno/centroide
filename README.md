# centroide

Passo a passo do algoritmo:

1 - Ler a base de dados

2 - Verificar quantos e quais são os casos específicos existentes nessa base de dados

3 - A partir do resultado acima obtido, estipular um número de clusters

4 - Criar os clusters com a mediana igual ao primeiro elemento de cada tipo (Iris-virginica, Iris-versicolor, Iris-setosa)

5 - Calcular a mediana de cada cluster de acordo com os dados usados como base de dados do classificador

6 - Adicionar o novo elemento para o cluster com menor distância e recalcula a mediana com o novo elemento adicionado

7 - Após esse "treinamento inicial", iremos refazer o passo 6, mas agora com os dados a serem classificados

A saída deve ser algo parecido com isso:

```
Quantidade de instâncias classificadas: 60
Acertos: 54
Taxa de acerto do classificador: 90.0

clusters depois da classificação dos novos dados
[6.875675675675676, 3.091891891891892, 5.764864864864866, 2.105405405405405] - 0 - Iris-virginica
[5.916923076923077, 2.756923076923077, 4.427692307692307, 1.443076923076923] - 1 - Iris-versicolor
[5.01372549019608, 3.41764705882353, 1.468627450980392, 0.24313725490196075] - 2 - Iris-setosa
```
