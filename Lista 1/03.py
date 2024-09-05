# ESCREVA UM PROGRAMA QUE LEIA A QUANTIDADE DE DIAS, HORAS, MINUTOS E SEGUNDOS DO USARIO. CALCULE O TOTAL EM SEGUNDOS

dia = int(input('Digite a quantidade de dias : '))
hora = int(input('Digite as quantidade de hora : '))
minuto = int(input('Digite os minutos : '))
segundos = int(input('digite os segundos : '))

total = dia * 24 * 60 * 60 + hora * 60 * 60 + minuto * 60 + segundos 
print(f'convertendo essa porra toda da em segundo o total de : {total}')