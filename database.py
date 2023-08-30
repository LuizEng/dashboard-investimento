import pandas as pd

dataframe = pd.read_excel('D:\Dev\Python\dashboard-investimento\Gerenciamento.xlsx')


def tempo_medio_por_operacao():
    media_valor = dataframe['Tempo Operação'].mean()
    return media_valor

def total_operacoes():
    return dataframe.shape[0]

def capital_inicial():
    capital = dataframe['Capital'].iloc[0]
    return capital

def capital_atual():
    capital = dataframe['Capital'].iloc[-1]
    return capital

def quantidade_operacoes_vencedoras():
    filtro = dataframe.loc[dataframe['Res. Operação'] > 0]
    return filtro['Res. Operação'].count()

def taxa_de_acerto():
    total = total_operacoes()
    total_vencedoras = quantidade_operacoes_vencedoras()
    
    if total_vencedoras == 0:
        return 0 
    
    taxa = (total_vencedoras / total) * 100
    return f"{taxa:.2f} %"  


