import sqlite3

class PrefixCustomization:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS prefixes (
                            server_id TEXT PRIMARY KEY,
                            prefix TEXT)''')
        self.conn.commit()

    def set_prefix(self, server_id, prefix):
        self.cur.execute('''INSERT OR REPLACE INTO prefixes (server_id, prefix) 
                            VALUES (?, ?)''', (server_id, prefix))
        self.conn.commit()

    def get_prefix(self, server_id):
        self.cur.execute('''SELECT prefix FROM prefixes WHERE server_id = ?''', (server_id,))
        row = self.cur.fetchone()
        if row:
            return row[0]
        return '!'

    def delete_prefix(self, server_id):
        self.cur.execute('''DELETE FROM prefixes WHERE server_id = ?''', (server_id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()