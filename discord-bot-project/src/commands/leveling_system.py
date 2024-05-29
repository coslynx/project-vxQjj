import sqlite3

class LevelingSystem:
    def __init__(self):
        self.conn = sqlite3.connect('leveling_system.db')
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            level INTEGER DEFAULT 1,
            experience INTEGER DEFAULT 0
        )''')
        self.conn.commit()

    def add_experience(self, user_id, exp):
        self.cur.execute('''SELECT experience, level FROM users WHERE user_id = ?''', (user_id,))
        row = self.cur.fetchone()
        if row:
            current_exp, level = row
            new_exp = current_exp + exp
            if new_exp >= 100:
                new_exp -= 100
                level += 1
                self.cur.execute('''UPDATE users SET level = ?, experience = ? WHERE user_id = ?''', (level, new_exp, user_id))
            else:
                self.cur.execute('''UPDATE users SET experience = ? WHERE user_id = ?''', (new_exp, user_id))
            self.conn.commit()

    def get_user_level(self, user_id):
        self.cur.execute('''SELECT level FROM users WHERE user_id = ?''', (user_id,))
        row = self.cur.fetchone()
        if row:
            return row[0]
        else:
            return None

    def get_user_experience(self, user_id):
        self.cur.execute('''SELECT experience FROM users WHERE user_id = ?''', (user_id,))
        row = self.cur.fetchone()
        if row:
            return row[0]
        else:
            return None

    def set_user_level(self, user_id, level):
        self.cur.execute('''UPDATE users SET level = ? WHERE user_id = ?''', (level, user_id))
        self.conn.commit()

    def set_user_experience(self, user_id, exp):
        self.cur.execute('''UPDATE users SET experience = ? WHERE user_id = ?''', (exp, user_id))
        self.conn.commit()

    def reset_user(self, user_id):
        self.cur.execute('''UPDATE users SET level = 1, experience = 0 WHERE user_id = ?''', (user_id,))
        self.conn.commit()

    def get_leaderboard(self):
        self.cur.execute('''SELECT user_id, username, level FROM users ORDER BY level DESC''')
        rows = self.cur.fetchall()
        leaderboard = []
        for row in rows:
            leaderboard.append({'user_id': row[0], 'username': row[1], 'level': row[2]})
        return leaderboard

    def close_connection(self):
        self.conn.close()