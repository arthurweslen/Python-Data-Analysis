print('='*28)
print(f'\033[1:7m{"Operação Matemática":=^28}\033[m')
print('='*28)

import pandas as pd
dataset = pd.read_excel('C:/Users/Suporte/Documents/Mini_Projeto/Operações Matemáticas/Soma_Contagem_Máximo_Mínimo.xlsx')
#print(dataset)


#MULTIPLICAR colunas
dataset['TOTAL'] = dataset['QTD'] * dataset['VALOR']
#print(dataset)

#MÁXIMO - Mair Total (Melhor venda)
maior_valor = dataset['TOTAL'].max()

#MÍNIMO - Menor Valor (Valor Mais barato)
menor_valor = dataset['VALOR'].min()

#CONTAR - Total de Produtos
qtd_produto = dataset['PRODUTO'].count()

# SOMAR QTD (Total de Quantidade)
total_produto = dataset['QTD'].sum()
#print(dataset)


print("\n")
print("Maior valor: " + str(maior_valor))
print("Menor valor: " + str(menor_valor))
print("Quantidade produto: " + str(qtd_produto))
print("Total produto: " + str(total_produto))
print("\n")
print(dataset)

