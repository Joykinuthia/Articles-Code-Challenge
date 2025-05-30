from code_challenge.lib.db.connection import get_connection

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @staticmethod
    def save(name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?) RETURNING id", (name,))
        author_id = cursor.fetchone()[0]
        conn.commit()
        conn.close()
        return author_id

    @staticmethod
    def find_by_id(author_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE id = ?", (author_id,))
        result = cursor.fetchone()
        conn.close()
        return Author(*result) if result else None

    @staticmethod
    def find_by_name(name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE name = ?", (name,))
        result = cursor.fetchone()
        conn.close()
        return Author(*result) if result else None

    @staticmethod
    def most_prolific_author():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT a.*, COUNT(ar.id) as article_count FROM authors a
            JOIN articles ar ON a.id = ar.author_id
            GROUP BY a.id
            ORDER BY article_count DESC
            LIMIT 1
            """
        )
        result = cursor.fetchone()
        conn.close()
        return Author(*result) if result else None

    def articles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return articles

    def magazines(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.* FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self.id,))
        magazines = cursor.fetchall()
        conn.close()
        return magazines

    def add_article(self, magazine_id, title):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
            (title, self.id, magazine_id)
        )
        conn.commit()
        conn.close()

    def topic_areas(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT DISTINCT m.category FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
            """,
            (self.id,)
        )
        categories = [row[0] for row in cursor.fetchall()]
        conn.close()
        return categories