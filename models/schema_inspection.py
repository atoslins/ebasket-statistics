from sqlalchemy import inspect, MetaData, Table, create_engine
from config import Config

def inspect_database():
    """
    Inspect the database schema and return information about tables and columns.
    """
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
    inspector = inspect(engine)
    
    schema_info = {}
    
    # Get all table names
    table_names = inspector.get_table_names()
    
    for table_name in table_names:
        columns = []
        for column in inspector.get_columns(table_name):
            columns.append({
                'name': column['name'],
                'type': str(column['type']),
                'nullable': column.get('nullable', True),
                'default': column.get('default', None),
                'primary_key': column.get('primary_key', False)
            })
        
        foreign_keys = []
        for fk in inspector.get_foreign_keys(table_name):
            foreign_keys.append({
                'constrained_columns': fk['constrained_columns'],
                'referred_table': fk['referred_table'],
                'referred_columns': fk['referred_columns']
            })
        
        schema_info[table_name] = {
            'columns': columns,
            'foreign_keys': foreign_keys
        }
    
    return schema_info

def print_schema_info():
    """
    Print the database schema information in a readable format.
    """
    schema_info = inspect_database()
    
    for table_name, table_info in schema_info.items():
        print(f"Table: {table_name}")
        print("  Columns:")
        for column in table_info['columns']:
            pk_marker = " (PK)" if column['primary_key'] else ""
            nullable = "" if column['nullable'] else " NOT NULL"
            default = f" DEFAULT {column['default']}" if column['default'] is not None else ""
            print(f"    - {column['name']}: {column['type']}{pk_marker}{nullable}{default}")
        
        if table_info['foreign_keys']:
            print("  Foreign Keys:")
            for fk in table_info['foreign_keys']:
                print(f"    - {', '.join(fk['constrained_columns'])} -> {fk['referred_table']}({', '.join(fk['referred_columns'])})")
        
        print()

if __name__ == "__main__":
    print_schema_info()
