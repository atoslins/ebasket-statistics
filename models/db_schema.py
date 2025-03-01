"""
Referência para o esquema das tabelas do banco de dados.
Este arquivo serve como documentação para a estrutura das tabelas
e pode ser usado como referência rápida durante o desenvolvimento.
"""

SCHEMA = {
    "partidas": {
        "columns": {
            "id": {"type": "INTEGER", "primary_key": True, "nullable": False},
            "data": {"type": "DATE"},
            "hora": {"type": "TEXT"},
            "arena": {"type": "TEXT"},
            "status": {"type": "TEXT"},
            "time1_nome": {"type": "TEXT"},
            "time1_jogador": {"type": "TEXT"},
            "time1_placar_final": {"type": "INTEGER"},
            "time1_placar_periodos": {"type": "TEXT"},
            "time2_nome": {"type": "TEXT"},
            "time2_jogador": {"type": "TEXT"},
            "time2_placar_final": {"type": "INTEGER"},
            "time2_placar_periodos": {"type": "TEXT"}
        }
    }
}

def get_table_schema(table_name):
    """
    Retorna o esquema de uma tabela específica.
    
    Args:
        table_name (str): Nome da tabela
        
    Returns:
        dict: Esquema da tabela ou None se a tabela não existir
    """
    return SCHEMA.get(table_name)

def get_column_info(table_name, column_name):
    """
    Retorna informações sobre uma coluna específica.
    
    Args:
        table_name (str): Nome da tabela
        column_name (str): Nome da coluna
        
    Returns:
        dict: Informações da coluna ou None se a tabela/coluna não existir
    """
    table_schema = get_table_schema(table_name)
    if table_schema and column_name in table_schema["columns"]:
        return table_schema["columns"][column_name]
    return None

def get_all_tables():
    """
    Retorna uma lista com os nomes de todas as tabelas.
    
    Returns:
        list: Lista de nomes de tabelas
    """
    return list(SCHEMA.keys())

def get_all_columns(table_name):
    """
    Retorna uma lista com os nomes de todas as colunas de uma tabela.
    
    Args:
        table_name (str): Nome da tabela
        
    Returns:
        list: Lista de nomes de colunas ou lista vazia se a tabela não existir
    """
    table_schema = get_table_schema(table_name)
    if table_schema:
        return list(table_schema["columns"].keys())
    return []
