import pytest
from code_challenge.article import Article
from code_challenge.lib.db.connection import get_connection
from code_challenge.lib.db.seed import seed_data
from code_challenge.scripts.setup_db import setup_database

@pytest.fixture(scope="module", autouse=True)
def setup_and_seed():
    setup_database()
    conn = get_connection()
    conn.execute("DELETE FROM articles")
    conn.execute("DELETE FROM magazines")
    conn.execute("DELETE FROM authors")
    conn.commit()

    # Verify database is empty
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM articles")
    assert cursor.fetchone()[0] == 0
    cursor.execute("SELECT COUNT(*) FROM magazines")
    assert cursor.fetchone()[0] == 0
    cursor.execute("SELECT COUNT(*) FROM authors")
    assert cursor.fetchone()[0] == 0

    conn.close()
    seed_data()

def test_save_article():
    article_id = Article.save("Test Article", 1, 1)
    assert article_id is not None

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM articles WHERE id = ?", (article_id,))
    result = cursor.fetchone()
    conn.execute("DELETE FROM articles WHERE id = ?", (article_id,))  # Clean up test data
    conn.commit()
    conn.close()

    assert result is not None
    assert result[1] == "Test Article"
    assert result[2] == 1
    assert result[3] == 1

def test_find_by_id():
    article = Article.find_by_id(1)
    assert article is not None
    assert article.title == "Article 1"

def test_find_by_title():
    articles = Article.find_by_title("Article 2")
    assert len(articles) == 1
    assert articles[0].id == 2

def test_find_by_author():
    articles = Article.find_by_author(1)
    assert len(articles) == 2

def test_find_by_magazine():
    articles = Article.find_by_magazine(1)
    assert len(articles) == 2