# AyushEquity-AI
An AI system for financial inclusion assessment and fraud detection in rural India.

## Project Structure

- `data/` — Raw and processed datasets
- `database/` — SQLite database and schema setup
- `models/` — Trained ML model artifacts (.pkl files)
- `scripts/` — Data generation and model training scripts
- `backend/` — FastAPI server for model serving
- `frontend/` — Streamlit dashboards (officer + citizen portals)
- `notebooks/` — Exploratory data analysis
- `tests/` — Automated tests

## Setup Instructions

1. Create virtual environment: `python -m venv venv`
2. Activate it: `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Initialize database: `python database/db_setup.py` (Day 3)
5. Generate synthetic data: `python scripts/generate_data.py` (Day 2)
6. Train models: `python scripts/train_*.py` (Later days)
7. Run API: `uvicorn backend.api:app --reload` (Later days)
8. Run dashboards: `streamlit run frontend/officer_dashboard.py` (Later days)

## Day-by-Day Guide

- **Day 1** — Project structure, virtual environment, Git initialization
- **Day 2** — Synthetic data generation with Faker
- **Day 3+** — Database, ML models, API, frontends

---
