print('='*28)
print(f'\033[1:7m{" Operações Matemáticas 2 ":=^28}\033[m')
print('='*28)


import pandas as pd
dataset = pd.read_excel('Média_Mediana.xlsx')
print('\033[1:36m Dataframe sem o ETL \033[m')
print(dataset)

#Desvio Padrão da Coluna A
dataset['desvio_padrao'] = dataset['ColunaA'].std()

#Média Coluna B
dataset['media'] =dataset['ColunaB'].mean()

# Variância coluna A
dataset['variancia'] = dataset['ColunaA'].var()

#Mediana Coluna B
dataset['mediana'] = dataset['ColunaB'].median()

# Moda, valores que mais se repetem
dataset['moda'] = dataset['ColunaB'].mode()


# Quantil de 25%.... mas poderia colocar qualquer valor
dataset['quantil 25%'] = dataset['ColunaB'].quantile(0.25)
#dataset['quantil 50%'] = dataset['ColunaB'].quantile(0.50)
#dataset['quantil 75%'] = dataset['ColunaB'].quantile(0.75)

print('\033[1:36m Dataframe com o ETL \033[m')
print(dataset)
#print(dataset.describe())
