def multi (n1):
    resultado = n1*2
    return resultado

def triplo (n1):
    resultado1 = n1*3 
    return resultado1

def quadriplo (n1):
    resultado2 = n1*4
    return resultado2

def quintuplo (n1):
    resultado3 = n1*5
    return resultado3

def principal():
    numero1 = int (input("Digite N1: "))
    resultadodobro = multi(numero1)
    resultadotriplo = triplo(numero1)
    resultadoquadriplo = quadriplo(numero1)
    resultadoquintuplo = quintuplo(numero1)
    print(f"o dobro é: {resultadodobro}, o triplo é: {resultadotriplo}, o quadriplo é {resultadoquadriplo}, o quintuplo é {resultadoquintuplo}")

principal()