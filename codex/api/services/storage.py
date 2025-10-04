import os
import sqlite3
from typing import Optional

DB_PATH = os.getenv("DB_PATH", "data/app.db")
# Ensure parent directory exists
parent_dir = os.path.dirname(DB_PATH) or "."
os.makedirs(parent_dir, exist_ok=True)

def get_conn() -> sqlite3.Connection:
    """Return a SQLite connection with WAL mode enabled."""
    conn = sqlite3.connect(DB_PATH, isolation_level=None, check_same_thread=False)
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA synchronous=NORMAL;")
    return conn
