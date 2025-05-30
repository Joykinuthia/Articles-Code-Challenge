from code_challenge.lib.db.connection import get_connection

class Article:
    def __init__(self, id, title, author_id, magazine_id):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id

    @staticmethod
    def save(title, author_id, magazine_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?) RETURNING id",
            (title, author_id, magazine_id)
        )
        article_id = cursor.fetchone()[0]
        conn.commit()
        conn.close()
        return article_id

    @staticmethod
    def find_by_id(article_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE id = ?", (article_id,))
        result = cursor.fetchone()
        conn.close()
        return Article(*result) if result else None

    @staticmethod
    def find_by_title(title):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE title = ?", (title,))
        results = cursor.fetchall()
        conn.close()
        return [Article(*row) for row in results]

    @staticmethod
    def find_by_author(author_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (author_id,))
        results = cursor.fetchall()
        conn.close()
        return [Article(*row) for row in results]

    @staticmethod
    def find_by_magazine(magazine_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (magazine_id,))
        results = cursor.fetchall()
        conn.close()
        return [Article(*row) for row in results]