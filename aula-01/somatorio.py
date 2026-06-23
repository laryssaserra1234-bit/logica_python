def soma(n1,n2):
    resultado = n1 + n2
    return resultado

def principal():
    numero1 = int (input("Digite N1: "))
    numero2 = int (input("Digite N2:"))
    resultado = soma(numero1, numero2)
    print ("Somatorio é:" , resultado)

principal()