import pytest
from code_challenge.author import Author
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
    conn.close()
    seed_data()

def test_save_author():
    author_id = Author.save("Test Author")
    assert author_id is not None

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM authors WHERE id = ?", (author_id,))
    result = cursor.fetchone()
    conn.close()

    assert result is not None
    assert result[1] == "Test Author"

def test_find_by_id():
    author = Author.find_by_id(1)
    assert author is not None
    assert author.name == "Author 1"

def test_find_by_name():
    author = Author.find_by_name("Author 2")
    assert author is not None
    assert author.id == 2

def test_articles():
    author = Author.find_by_id(1)
    articles = author.articles()
    assert len(articles) == 2

def test_magazines():
    author = Author.find_by_id(1)
    magazines = author.magazines()
    assert len(magazines) == 2

def test_add_article():
    author = Author.find_by_id(1)
    author.add_article(2, "New Article")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM articles WHERE title = ?", ("New Article",))
    result = cursor.fetchone()
    conn.close()

    assert result is not None
    assert result[1] == "New Article"
    assert result[2] == 1
    assert result[3] == 2

def test_topic_areas():
    author = Author.find_by_id(1)
    topics = author.topic_areas()
    assert len(topics) == 2
    assert "Category 1" in topics
    assert "Category 2" in topics