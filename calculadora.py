# Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:

# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão

# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

def calculadora(n1, n2, operacao):
  if (operacao == 1):
    resposta = n1 + n2
  elif (operacao == 2):
    resposta = n1 - n2
  elif (operacao == 3):
    resposta = n1 * n2
  elif (operacao == 4):
    resposta = n1 / n2
  else:
    resposta = 0
  return resposta

resultado = calculadora(10, 10, 3)
print(resultado)