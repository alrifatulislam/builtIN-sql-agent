
# Built-in SQL Agent

A Python class project that uses LangChain and a local Ollama model to answer natural-language questions about a SQLite database. It uses the Chinook sample music-store database and can generate and run SQL queries to answer questions about artists, tracks, invoices, and sales.

## How it works

The agent connects to the Chinook SQLite database, sends your question to the locally running `llama3` model through Ollama, and returns an answer based on the database.

## Requirements

- Python
- [Ollama](https://ollama.com/)
- The `llama3` model downloaded in Ollama

## Setup

1. Clone the repository and open its directory:

   ```bash
   git clone https://github.com/alrifatulislam/builtIN-sql-agent.git
   cd builtIN-sql-agent
   ```

2. Install the Python dependency:

   ```bash
   pip install langchain-community
   ```

3. Download the model:

   ```bash
   ollama pull llama3
   ```

4. Ensure the database path in `builtin_agent.py` matches the filename in the repository:

   ```python
   db = SQLDatabase.from_uri("sqlite:///chinook.db")
   ```

   The included database file is named `chinook.db`.

## Run

Start Ollama, then run:

```bash
python builtin_agent.py
```

The script runs a sample question and then prints results and response times for several example questions.

## Example questions

- List total sales per country and identify the country that spent the most.
- Which artist has the most albums in the database?
- What are the five most popular music genres by number of tracks?

## Database

The repository includes:

- `chinook.db` — the SQLite database used by the agent.
- `Chinook_Sqlite.sql` — SQL script for creating and populating the Chinook database.
- `create_db.py` — script that creates `chinook.db` from `Chinook_Sqlite.sql`.

If the database file is missing, run:

```bash
python create_db.py
```

## Project files

| File | Description |
| --- | --- |
| `builtin_agent.py` | Configures the LangChain SQL agent and runs example questions. |
| `create_db.py` | Builds the SQLite database from the SQL script. |
| `chinook.db` | Included Chinook sample database. |
| `Chinook_Sqlite.sql` | Database schema and sample data. |

## Notes

- The model runs locally through Ollama; the first response may take longer while the model initializes.
- The agent prints verbose execution details to the console.
- Review generated SQL and use trusted inputs when experimenting with databases.
``` 
