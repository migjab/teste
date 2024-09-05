valorhora = int(input('Quanto voce ganha por hora ? '))
horatrabalhada = int(input('Quantas horas trabalhadas ? '))

salariobruto = valorhora * horatrabalhada

ir = salariobruto * (11/100)
inss = salariobruto * (8/100)
sindicato = salariobruto * (5/100)

print(f'Salario Bruto = R${salariobruto}')
print(f'IR = - R${ir}')
print(f'INSS = - R${inss}')
print(f'Sendicato = - R${sindicato}')
print(f'Salario liquido = {salariobruto - ir - inss - sindicato}')