area = int (input('Quantos metros quadrados voce vai pintar ? :'))

if area < 54:
    print('Voce vai precisar um pouco menos de 1 lata de tinta.')
    print('Não vendemos menos que uma lata.')

elif area > 54:
    area = (area / 54)
    print(f'voce vai precisar de {area} latas de tinta no total de {area * 18}')