import pandas as pd

df = pd.read_csv('dados.csv',sep=';')

print(df.head())
print(df.describe())

vendas_2023 = df[df['Ano'] == 2023]

vendas_2023.to_excel('vendas_2023.xlsx', index=False)
