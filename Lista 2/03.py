peso = int(input('Digite o peso: '))

excesso = 0
multa = 0

if peso > 50:
    excesso = peso - 50
    multa = 4 * excesso

print(f"Excesso: {excesso} kg")
print(f"Multa: R$ {multa},")
