pmercadoria = int(input('Digite o preço do produto'))
desconto = int(input('Digite o desconto : '))
descontoconv = desconto / 100 * pmercadoria

print(f'Sub total preço da mercadoria : {pmercadoria} Desconto : {descontoconv}  Total : {pmercadoria - descontoconv}')