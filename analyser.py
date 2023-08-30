import database;

def get_tempo_medio_operacao():
    return database.tempo_medio_por_operacao()

def get_total_operacoes():
    return database.total_operacoes()

def get_capital_inicial():
    return database.capital_inicial()

def get_capital_atual():
    return database.capital_atual()

def get_quantidade_operacoes_vencedoras():
    return database.quantidade_operacoes_vencedoras()

def get_taxa_de_acerto():
    return database.taxa_de_acerto()
