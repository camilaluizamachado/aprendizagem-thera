import math

def calculadora():
    while True:
        expr = input("Digite a expressão (ou 'sair'): ").lower()
        if expr == "sair":
            break
        try:
            resultado = eval(expr)
            # Mostrar como inteiro se for número inteiro
            if isinstance(resultado, float) and resultado.is_integer():
                print(int(resultado))
            else:
                print(resultado)
        except:
            print("Erro")

calculadora()
