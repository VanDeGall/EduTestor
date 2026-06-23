from __future__ import annotations

import os
import sqlite3
from pathlib import Path
from typing import Any, Iterable

APP_DIR = Path(__file__).resolve().parent
REPO_ROOT = APP_DIR.parent
DEFAULT_DB_PATH = REPO_ROOT / "sdk_agent.sqlite3"
SCHEMA_PATH = REPO_ROOT / "docs" / "sdk-agent" / "database-schema.sql"


def get_db_path() -> Path:
    """Return the SQLite database path, allowing an environment override."""
    return Path(os.environ.get("SDK_AGENT_DB", DEFAULT_DB_PATH)).resolve()


def connect() -> sqlite3.Connection:
    """Create a SQLite connection with row dictionaries and FK support."""
    conn = sqlite3.connect(get_db_path())
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db() -> None:
    """Create database tables and seed the default user/settings."""
    if not SCHEMA_PATH.exists():
        raise FileNotFoundError(f"Database schema not found: {SCHEMA_PATH}")

    schema_sql = SCHEMA_PATH.read_text(encoding="utf-8")
    with connect() as conn:
        conn.executescript(schema_sql)
        conn.execute(
            """
            INSERT OR IGNORE INTO users (id, display_name, role, school_name, email)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                "user_marcel",
                "Marcel Gallik",
                "School Digital Coordinator",
                "ZS s MS sv. Kriza, Kezmarok",
                "gallik.marcel@gmail.com",
            ),
        )
        conn.execute(
            """
            INSERT OR IGNORE INTO settings (
                id, user_id, voice_input_enabled, voice_output_enabled,
                avatar_enabled, automatic_tracking_enabled, silent_mode
            ) VALUES (?, ?, 0, 0, 1, 0, 0)
            """,
            ("settings_default", "user_marcel"),
        )
        conn.commit()


def rows_to_dicts(rows: Iterable[sqlite3.Row]) -> list[dict[str, Any]]:
    return [dict(row) for row in rows]


def fetch_all(query: str, params: tuple[Any, ...] = ()) -> list[dict[str, Any]]:
    with connect() as conn:
        rows = conn.execute(query, params).fetchall()
    return rows_to_dicts(rows)


def fetch_one(query: str, params: tuple[Any, ...] = ()) -> dict[str, Any] | None:
    with connect() as conn:
        row = conn.execute(query, params).fetchone()
    return dict(row) if row else None
