# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021. A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

def idade():
  controle = True

  while(controle):
    try:
      nomeCompleto = input("Digite o seu nome completo: ")
      anoNascimento = int(input("Digite o seu ano de nascimento: "))

      if (anoNascimento >= 1922 and anoNascimento <= 2021):
        idade = 2022 - anoNascimento
        print("Nome: " + nomeCompleto)
        print("Idade em 2022: " + str(idade))

        controle = False
      else:
        print("O ano de nascimento precisa estar entre 1922 e 2021")
    except:
        print("Digite apenas números!")

idade()