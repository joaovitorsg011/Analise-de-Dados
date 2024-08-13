# Passo a passo
# Passo 1 - Importar a base d dados
# Passo 2 - Visualizar a base de dados
    # Colunas inuteis - Informacoes que nao te ajuda te atrapalha
    # Informacoes no formato errado
    # Valores vazios
# Passo 3 - Tratamentos de dados - corrigir os erros da base de dados
# Passo 4 - Analise inicial dos cancelamentos
# Passo 5 - Analise de causas do cancelamento dos clientes

# Passo 1 - Importar a base d dados
import pandas as pd
tabela = pd.read_csv('cancelamentos_sample.csv')

# Colunas inuteis - Informacoes que nao te ajuda te atrapalha
tabela = tabela.drop(columns='CustomerID') # Para apagar uma coluna

# Valores vazios
tabela = tabela.dropna() # Para eliminar valores vazios

# Passo 4 - Analise inicial dos cancelamentos
print(tabela['cancelou'].value_counts()) # Para visualizar os valores da coluna
print(tabela['cancelou'].value_counts(normalize=True)) # Para visualizar em percentual

# Passo 5 - Analise de causas do cancelamento dos clientes
import plotly.express as px

for coluna in tabela.columns:
    # criar o grafico
    grafico = px.histogram(tabela, x=coluna, color='cancelou')

    # exibir o grafico
    grafico.show()

# Passo 2 - Visualizar a base de dados
print(tabela.info())

# ---- PROBLEMAS E SOLUCOES ----

# todos os clientes que ligaram mais de 4x pro call center, cancelaram
    # criar um processo interno para resolver os problemas do cliente em no maximo 3 ligacoes
# todos os clientes que atrasaram mais de 20 dias o pagamento, cancelaram
    # criar um processo de que quando bate 10 dias de atraso no pagamento, liga um alerta vermelho
# todos os clientes de contrato mensal, cancelaram
    # oferecer desconto no contrato anual ou trimestral

# filtrar uma base de dados

# Se eu resolver o call center, para quanto cai o cancelamento?
filtro = tabela['ligacoes_callcenter'] <=4
tabela = tabela[filtro]
# E o atraso?
filtro = tabela['dias_atraso'] <=20
tabela = tabela[filtro]
# E o contrato mensal?
filtro = tabela['duracao_contrato'] != 'Monthly'
tabela = tabela[filtro]

print(tabela['cancelou'].value_counts(normalize=True))
