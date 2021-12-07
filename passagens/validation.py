def origem_destino_iguais(origem, destino, lista_erros):
    """Verifica se o destino e a origem são iguais"""
    if origem == destino:
        lista_erros['destino'] = 'Origem e destino devem ser diferentes'

def campo_tem_numero(valor_campo, nome_campo, lista_erros):
    """Verifica se há caracter númerico"""
    if any(char.isdigit() for char in valor_campo):
        lista_erros[nome_campo] = "Não inclua números"

def data_ida_maior_data_volta(data_ida, data_volta, lista_erros):
    """Verifica se a data de ida é maior que a de volta"""
    if data_ida > data_volta:
        lista_erros['data_volta'] = 'A data de ida deve ser menor que a data de volta'

def data_ida_maior_data_hoje(data_ida, data_atual, lista_erros):
    """Verifica se a data de compra é igual ou maior que a data do dia atual"""
    if data_ida < data_atual:
        lista_erros['data_ida'] = 'Data de ida não pode ser inferior ao dia de hoje'