


# Solicita ao usuário a quantidade de cigarros fumados por dia e o tempo de fumante em anos
cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))
anos_fumando = int(input("Por quantos anos você fumou? "))

# Calcula o total de cigarros fumados durante todos os anos
total_cigarros = cigarros_por_dia * anos_fumando * 365

# Calcula o total de minutos perdidos (cada cigarro reduz 10 minutos de vida)
minutos_perdidos = total_cigarros * 10

# Converte os minutos perdidos em dias (1 dia = 1440 minutos)
dias_perdidos = minutos_perdidos / 1440

# Exibe o total de dias de vida perdidos
print(f"O total de dias de vida perdidos é: {dias_perdidos:.2f} dias")