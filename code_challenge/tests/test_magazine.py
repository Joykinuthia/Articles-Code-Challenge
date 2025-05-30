import pytest
from code_challenge.magazine import Magazine
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

def test_save_magazine():
    magazine_id = Magazine.save("Test Magazine", "Test Category")
    assert magazine_id is not None

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM magazines WHERE id = ?", (magazine_id,))
    result = cursor.fetchone()
    conn.close()

    assert result is not None
    assert result[1] == "Test Magazine"
    assert result[2] == "Test Category"

def test_find_by_id():
    magazine = Magazine.find_by_id(1)
    assert magazine is not None
    assert magazine.name == "Magazine 1"

def test_find_by_name():
    magazine = Magazine.find_by_name("Magazine 2")
    assert magazine is not None
    assert magazine.id == 2

def test_find_by_category():
    magazines = Magazine.find_by_category("Category 1")
    assert len(magazines) == 1
    assert magazines[0].id == 1

def test_articles():
    magazine = Magazine.find_by_id(1)
    articles = magazine.articles()
    assert len(articles) == 2

def test_contributors():
    magazine = Magazine.find_by_id(1)
    contributors = magazine.contributors()
    assert len(contributors) == 2

def test_article_titles():
    magazine = Magazine.find_by_id(1)
    titles = magazine.article_titles()
    assert len(titles) == 2
    assert "Article 1" in titles
    assert "Article 3" in titles

def test_contributing_authors():
    magazine = Magazine.find_by_id(1)
    authors = magazine.contributing_authors()
    assert len(authors) == 0