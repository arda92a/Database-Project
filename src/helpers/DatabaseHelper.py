class DatabaseHelper:
    def __init__(self, db_connection):
        self.db = db_connection

    def execute_query(self, query, params=()):
        cursor = self.db.cursor(buffered=True)
        cursor.execute(query, params)
        return cursor

    def fetch_one(self, query, params=()):
        cursor = self.execute_query(query, params)
        return cursor.fetchone()

    def fetch_all(self, query, params=()):
        cursor = self.execute_query(query, params)
        return cursor.fetchall()

    def commit(self):
        self.db.commit()
        
    def insert(self, query, params=()):
        cursor = self.execute_query(query, params)
        self.commit()
        return cursor.lastrowid

    def update(self, query, params=()):
        self.execute_query(query, params)
        self.commit()

    def delete(self, query, params=()):
        self.execute_query(query, params)
        self.commit()