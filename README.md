# Articles Code Challenge

## Overview
The Articles Code Challenge is a Python-based project that demonstrates object-oriented programming (OOP) principles, database interactions using raw SQL, and comprehensive test coverage. The project is structured to handle relationships between Authors, Articles, and Magazines, with a focus on efficient SQL queries and modular design.

## Project Structure
```
code_challenge/
├── lib/                # Main code directory
│   ├── models/         # Model classes
│   │   ├── author.py   # Author class with SQL methods
│   │   ├── article.py  # Article class with SQL methods
│   │   └── magazine.py # Magazine class with SQL methods
│   ├── db/             # Database components
│   │   ├── connection.py # Database connection setup
│   │   ├── seed.py     # Seed data for testing
│   │   └── schema.sql  # SQL schema definitions
│   ├── controllers/    # Optional: Business logic
│   ├── debug.py        # Interactive debugging
│   └── __init__.py     # Makes lib a package
├── scripts/            # Helper scripts
│   ├── setup_db.py     # Script to set up the database
│   └── run_queries.py  # Script to run example queries
├── tests/              # Test directory
│   ├── test_author.py  # Tests for Author class
│   ├── test_article.py # Tests for Article class
│   └── test_magazine.py # Tests for Magazine class
├── database.db         # SQLite database file
├── pytest.ini          # Pytest configuration
├── LICENSE             # License file
├── Pipfile             # Python dependencies
└── README.md           # Project documentation
```

## Features
- **Author Class**: Manage authors and their relationships with articles and magazines.
- **Article Class**: Handle articles and their associations with authors and magazines.
- **Magazine Class**: Manage magazines and their contributors.
- **Database Layer**: Includes connection handling, schema definitions, and seed data.
- **Testing**: Comprehensive test coverage using `pytest`.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Articles-Code-Challenge
   ```

2. Install dependencies:
   ```bash
   pip install pipenv
   pipenv install
   ```

3. Set up the database:
   ```bash
   python code_challenge/scripts/setup_db.py
   ```

4. Seed the database with test data:
   ```bash
   python code_challenge/lib/db/seed.py
   ```

5. Run tests:
   ```bash
   pytest
   ```

## Usage
- **Interactive Debugging**:
  ```bash
  python code_challenge/lib/debug.py
  ```
- **Run Example Queries**:
  ```bash
  python code_challenge/scripts/run_queries.py
  ```

## Testing
- Ensure all tests pass by running:
  ```bash
  pytest
  ```

## License
This project is licensed under the terms of the LICENSE file.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for review.
