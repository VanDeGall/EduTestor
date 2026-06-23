# SDK Strategic AI Assistant MVP app

## Purpose

This is the first local MVP prototype of the SDK Strategic AI Assistant.

It provides:

- dashboard,
- activity inbox,
- manual work tracking,
- leadership output register,
- deadline register,
- XLSX exports,
- SQLite database.

This is not the final automated assistant yet. It is the first safe and transparent local prototype focused on evidence of work.

## Requirements

- Python 3.11 or newer recommended,
- packages from `requirements.txt`.

## Install

From repository root:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

On macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python run_sdk_agent.py
```

Then open:

```text
http://127.0.0.1:5050
```

## First test workflow

1. Open dashboard.
2. Add one activity in **Rýchly zápis činnosti**.
3. Start a work block in **Začať pracovný blok**.
4. Stop the active work block and add output.
5. Open **Vedenie** and create one leadership briefing.
6. Open **Termíny** and add one deadline.
7. Return to dashboard and export daily XLSX.
8. Export monthly XLSX.
9. Export leadership XLSX.

## Database

The app creates local SQLite database:

```text
sdk_agent.sqlite3
```

The schema is based on:

```text
docs/sdk-agent/database-schema.sql
```

## Exports

Exports are saved into:

```text
exports/
```

Export types currently implemented:

- daily work log XLSX,
- monthly SDK report XLSX,
- leadership evidence XLSX.

## Safety

This MVP does not perform hidden tracking.

It does not:

- record screen,
- capture keystrokes,
- read private messages,
- monitor other employees,
- monitor pupils,
- upload files,
- send documents.

Work blocks are started manually by the user.

## Next implementation steps

Recommended next code features:

1. edit and delete activity records,
2. evidence register screen,
3. settings screen,
4. JSON API endpoints,
5. professional development screen,
6. policy monitor screen,
7. voice note input,
8. avatar notification behaviour,
9. automatic work-context suggestion with explicit user approval.
