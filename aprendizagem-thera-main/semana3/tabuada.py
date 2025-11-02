# ==== Tabuada: várias formas ====

num = int(input("Digite o número para a tabuada: "))
print("\n--- 1️⃣ Usando for simples ---")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

print("\n--- 2️⃣ Usando while ---")
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1

print("\n--- 3️⃣ Usando função ---")
def tabuada(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
tabuada(num)

print("\n--- 4️⃣ Tabuada até um número definido pelo usuário ---")
max_val = int(input("Até qual número multiplicar? "))
for i in range(1, max_val+1):
    print(f"{num} x {i} = {num*i}")

print("\n--- 5️⃣ Tabuada de vários números de uma vez ---")
inicio = int(input("Começo da tabuada: "))
fim = int(input("Fim da tabuada: "))
for n in range(inicio, fim+1):
    print(f"\nTabuada do {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
