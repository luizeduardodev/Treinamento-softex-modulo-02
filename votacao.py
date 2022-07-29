# Desenvolva um código que simule uma eleição com três candidatos.
# - candidato_X => 889
# - candidato_Y => 847
# - candidato_Z => 515
# - branco => 0

# O código deve perguntar se deseja finalizar a votação depois do voto. Caso o número do voto não corresponda a nenhum candidato ou seja branco, ele deve ser tratado como nulo. Se for inserido um texto ao invés de número, o código deve retornar uma mensagem para votar novamente.

# Quando a votação for finalizada, o código deverá mostrar o vencedor, aquele com o maior número de votos e, também, a quantidade de votos de cada candidato, os brancos e nulos 

# Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link desse projeto no campo ao lado para que outros desenvolvedores possam analisá-lo.

from enum import Enum

class candidato(Enum):
  candidatoX = 889 
  candidatoY = 847
  candidatoZ = 515
  branco = 0

#Variáveis
controle = True
vencedorA = 0; vencedorY = 0; vencedorZ = 0; vencedor = 0
votoNulo = 0; votoBranco = 0
nomeVencedorA = ""; nomeVencedorY = ""; nomeVencedorZ = ""

def showInfo(nome, vencedor, vencedorA, vencedorY, vencedorZ, votoBranco, votoNulo):
  print("O " + nome + " é o vencedor com uma quantidade de votos igual a " + str(vencedor))

  print("Quantidade de votos do Candidato X: " + str(vencedorA))
  print("Quantidade de votos do Candidato Y: " + str(vencedorY))
  print("Quantidade de votos do Candidato Z: " + str(vencedorZ))

  print("Quantidade de votos brancos " + str(votoBranco))
  print("Quantidade de votos nulos " + str(votoNulo))

while (controle):
  try:
    print("")
    voto = int(input("Digite o número do candidato: "))
    
    if (voto == candidato.candidatoX.value or voto == candidato.candidatoY.value or voto == candidato.candidatoZ.value):
      print("Voto concluído! você votou no candidato de número " + str(voto))

      if (voto == candidato.candidatoX.value):
        vencedorA = vencedorA + 1
        nomeVencedorA = candidato.candidatoX.name
      elif (voto == candidato.candidatoY.value):
        vencedorY = vencedorY + 1
        nomeVencedorY = candidato.candidatoY.name
      elif (voto == candidato.candidatoZ.value):
        vencedorZ = vencedorZ + 1
        nomeVencedorZ = candidato.candidatoZ.name

      if (vencedorA > vencedorY and vencedorA > vencedorZ):
        vencedor = vencedorA
        nome = nomeVencedorA
      elif (vencedorY > vencedorA and vencedorY > vencedorZ):
        vencedor = vencedorY
        nome = nomeVencedorY
      elif (vencedorZ > vencedorA and vencedorZ > vencedorY):
        vencedor = vencedorZ
        nome = nomeVencedorZ

      print("")
      finalizar = input("Deseja finaizar a votação? (sim/nao) ")
      if (finalizar == "sim"):
        controle = False
    elif (voto != 889 or voto != 847 or voto != 515):
      #O voto deve ser tratado como nulo!
      if (voto == 0):
        votoBranco = votoBranco + 1
        print("Você votou no branco!")
      else:
        votoNulo = votoNulo + 1
        print("Este número não pertence a nenhum candidato!")
  except:
    print("Informe apenas o número do candidato! Por favor, vote novamente.")

print("")
showInfo(nome, vencedor, vencedorA, vencedorY, vencedorZ, votoBranco, votoNulo)