import sqlite3
from pathlib import Path

def setup_database():
    schema_path = Path(__file__).parent.parent / 'lib' / 'db' / 'schema.sql'
    conn = sqlite3.connect('database.db')
    with open(schema_path, 'r') as schema_file:
        conn.executescript(schema_file.read())
    conn.close()

if __name__ == '__main__':
    setup_database()
    print("Database setup complete.")