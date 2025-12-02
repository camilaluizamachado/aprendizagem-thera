# conversor_temperatura.py
def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

tipo = input("Digite 'C' para converter Celsius -> Fahrenheit ou 'F' para Fahrenheit -> Celsius: ").upper()
valor = float(input("Digite a temperatura: "))

if tipo == 'C':
    print(f"{valor}°C = {celsius_para_fahrenheit(valor):.2f}°F")
elif tipo == 'F':
    print(f"{valor}°F = {fahrenheit_para_celsius(valor):.2f}°C")
else:
    print("Opção inválida")
