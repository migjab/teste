#FAÇA UM PROGRAMA QUE CALCULE O AUMENTO DE UM SALARIO. ELE DEVE SOLICITAR O VALOR DO SALARIO E A 
# PORCENTAGEM DO AUMENTO. EXIBA O VALOR DO AUMENTO E DO NOVO SALARIO


salarioatual = int(input('Qual o seu salario : '))
aumento = int(input('Digiete quantos porcento gostaria de aumentar : '))
aumentoconv = aumento / 100 * salarioatual

print(f'Com esse aumento voce vai receber {aumentoconv} a mais no total seu novo salario será {salarioatual + aumentoconv}')