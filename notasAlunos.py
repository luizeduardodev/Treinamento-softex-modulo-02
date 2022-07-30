# Desenvolva um programa que deve ler um arquivo csv intitulado “notas_alunos.csv”. O arquivo deve ter a seguinte estrutura:

# aluno: Nome do aluno;
# nota_1: Primeira nota;
# nota_2: Segunda nota;
# faltas: Número de faltas;

# O programa lerá esse arquivo e criará duas colunas. A primeira coluna será “media”, que terá a média das duas notas do aluno. A segunda será “situacao”, com os valores: APROVADO ou REPROVADO.

# O aluno que tiver mais de 5 faltas ou possuir média menor que sete, será reprovado. O programa deverá salvar esse novo dataframe com o nome “alunos_situacao.csv”.

# Por fim, o programa deverá mostrar na tela:
# - o maior número de faltas;
# - a média geral das notas dos alunos;
# - e a maior média.

# Veja em anexo um exemplo do arquivo “notas_alunos.csv”.

# Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link desse projeto no campo ao lado para que outros desenvolvedores possam analisá-lo.

import pandas as pd

notas = pd.read_excel(r"C:\Users\Eduardo\Desktop\python\exercicio-softex-site\notas_aluno.xlsx")

media = (notas["nota1"] + notas["nota2"]) / 2

notas["media"] = media

notas.loc[(notas["faltas"] < 5) | (notas['media'] >= 7), "situacao"] = "Aprovado"
notas.loc[(notas['faltas'] > 5) | (notas['media'] < 7), "situacao"] = "Reprovado"

#Maior número de faltas;
faltas = 0
for i in notas["faltas"]:
  if (i > faltas):
    faltas = i

#Média Geral das notas dos alunos;
somaQtdItens = len(notas["nota1"].index)  + len(notas["nota2"].index)

somaNotaOne = notas["nota1"].sum()
somaNotaTwo = notas["nota2"].sum()

mediaGeral = (somaNotaOne + somaNotaTwo) / somaQtdItens

#Maior média;
maiorMedia = 0
for i in notas["media"]:
  if (i > maiorMedia):
    maiorMedia = i

print("")
print("Maior número de faltas: " + str(faltas))
print("Média geral das notas dos alunos: " + str(mediaGeral))
print("Maior média: " + str(maiorMedia))
print("")
print(notas)

notas.to_excel(r"C:\Users\Eduardo\Desktop\python\exercicio-softex-site\alunos_situacao.xlsx")