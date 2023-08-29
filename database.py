import pandas as pd

dataframe = pd.read_excel('D:\Dev\Python\dashboard-investimento\Gerenciamento.xlsx')


def tempo_medio_por_operacao():
    media_valor = dataframe['Tempo Operação'].mean()
    return 33

def total_operacoes():
    return dataframe.shape[0]