def menu():
  print("MENU DE OPÇÕES")
  print("")
  print("1: Soma")
  print("2: Subtração")
  print("3: Multiplicação")
  print("4: Divisão")
  print("0: Sair")

def resultado(n1, n2, operacao):
  if (operacao == 1):
    return n1 + n2
  elif (operacao == 2):
    return n1 - n2
  elif (operacao == 3):
    return n1 * n2
  elif (operacao == 4):
    return n1 / n2

def calculadora():
  menu()

  print("")
  operacao = int(input("Escolha uma opcão ou 0 para sair: "))

  while (operacao != 0):
    if (operacao > 0 and operacao < 5):
      print("")
      n1 = int(input("Digite o primeiro número: "))
      n2 = int(input("Digite o segundo número: "))
      print("")

      print("O resultado é " + str(resultado(n1, n2, operacao)))
      print("")
    else:
      print("")
      print("Essa opção não existe")
      print("")
    
    menu()

    print("")
    operacao = int(input("Escolha outra opcao ou 0 para sair: "))
  else:
    print("")
    print("Fim do programa!")

calculadora()