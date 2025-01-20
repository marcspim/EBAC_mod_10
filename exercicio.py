# Importando as bibliotecas necessárias
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('ecommerce_preparados.csv')

# Exibindo as primeiras linhas para entender a estrutura dos dados
print(df.head())

# Exibindo as informações do DataFrame
print(df.info())

# Gráfico de histograma
plt.figure(figsize=(10, 6))
plt.hist(df['Preço'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribuição do preço')  # Título do gráfico
plt.xlabel('Preço')  # Título do eixo X
plt.ylabel('Frequência')  # Título do eixo Y
plt.show()

# Gráfico de dispersão
plt.figure(figsize=(10,6))
plt.hexbin(df['N_Avaliações_MinMax'], df['Nota_MinMax'], gridsize=40, cmap='Blues')
plt.colorbar(label='Contagem dentro do bin')
plt.title('Dispersão entre número de avaliações e notas (normalizados)')  # Título do gráfico
plt.xlabel('Número de avaliações')  # Título do eixo X
plt.ylabel('Nota')  # Título do eixo Y
plt.show()

# Mapa de calor
plt.figure(figsize=(10, 6))
df_hm = df[['Nota', 'N_Avaliações', 'Desconto', 'Preço', 'Marca_Cod', 'Material_Cod', 'Temporada_Cod', 'Qtd_Vendidos_Cod']]  # Selecionando variáveis para exibição
corr = df_hm.corr()  # Cálculo da correlação
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Mapa de calor das correlações')  # Título do gráfico
plt.show()

# Gráfico de barra
plt.figure(figsize=(10, 6))
category_sales = df['Temporada'].value_counts()  # Definindo as variáveis
category_sales.plot(kind='bar', color='lightcoral')
plt.title('Quantidade por temporada')  # Título do gráfico
plt.xlabel('Temporada')  # Título do eixo X
plt.ylabel('Quantidade')  # Título do eixo Y
plt.xticks(rotation=90)
plt.show()

# Gráfico de pizza
plt.figure(figsize=(10, 6))
category_counts = df['Qtd_Vendidos'].value_counts()
category_counts.plot(kind='pie', autopct='%.1f%%', startangle=90, colors=sns.color_palette('Set3', len(category_counts)))
plt.title('Distribuição de vendas')
plt.ylabel('')  # Remover o rótulo do eixo y
plt.show()

# Gráfico de densidade
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Desconto'], fill=True, color='green')
plt.title('Densidade da distribuição do desconto')  # Título do gráfico
plt.xlabel('Desconto')  # Título do eixo X
plt.ylabel('Densidade')  # Título do eixo Y
plt.show()

# Gráfico de regressão
plt.figure(figsize=(10, 6))
sns.regplot(x='Preço', y='Qtd_Vendidos_Cod', data=df, scatter_kws={'s':10}, line_kws={'color':'red'})
plt.title('Relação de regressão entre preço e quantidade de produtos vendidos')  # Título do gráfico
plt.xlabel('Preço')  # Título do eixo X
plt.ylabel('Quantidade')  # Título do eixo Y
plt.show()
