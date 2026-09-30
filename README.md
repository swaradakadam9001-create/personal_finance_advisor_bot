# Personal Finance Advisor Bot

A ready-to-run college project based on the supplied project description/screenshots.

## Features
- Dashboard with income, expenses, savings and budget-health metrics
- Add monthly income
- Track daily/weekly expenses by category
- Spending analysis chart
- Rule-based AI-style financial recommendations
- Savings goals
- Recent transaction tables
- JSON summary API at `/api/summary`
- SQLite database with SQLAlchemy
- Responsive UI for desktop and mobile

## Technology
- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML/CSS/JavaScript
- Chart.js

## Run locally

### 1. Create a virtual environment
Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Start the app
```bash
python run.py
```

Open `http://127.0.0.1:5000`

The database is automatically created in `instance/finance.db` and demo data is inserted on the first run.

## Project structure
```text
personal_finance_advisor_bot/
├── app/
│   ├── __init__.py
│   ├── finance.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   │   ├── base.html
│   │   └── dashboard.html
│   └── static/
│       └── style.css
├── instance/
├── tests/
├── requirements.txt
├── run.py
└── README.md
```

## Note
The "AI recommendations" in this starter project are deterministic financial rules so the project works without an API key or paid AI service. For a more advanced version, an LLM API can be connected to `app/finance.py`.
