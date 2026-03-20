# Qualc

Qualc is a full-stack web application for call quality control workflows.
It combines a FastAPI backend with a Next.js frontend and stores business data in PostgreSQL.

## Tech Stack

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![FastAPI](https://img.shields.io/badge/fastapi-009688?style=for-the-badge&logo=fastapi&logoColor=white) ![Pydantic](https://img.shields.io/badge/pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)

![SQLAlchemy](https://img.shields.io/badge/sqlalchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white) ![Alembic](https://img.shields.io/badge/alembic-4B5563?style=for-the-badge&logo=alembic&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/postgresql-316192?style=for-the-badge&logo=postgresql&logoColor=white)

![Next JS](https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=next.js&logoColor=white) ![React](https://img.shields.io/badge/react-20232A?style=for-the-badge&logo=react&logoColor=61DAFB) ![TailwindCSS](https://img.shields.io/badge/tailwind_css-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)

## Repository Structure

- `backend/` - FastAPI app, SQLAlchemy models, Alembic migrations
- `frontend/` - Next.js application (App Router)
- `.env.example` - environment configuration template

## Backend

Main components:

- API: FastAPI (`backend/main.py`)
- DB access: SQLAlchemy async engine (`backend/database.py`)
- Config: Pydantic settings (`backend/config.py`)
- Migrations: Alembic (`backend/alembic/`)

### Backend setup

```bash
cd backend
pip install -r requirements.txt
```

Create `.env` in the repository root based on `.env.example`, then run:

```bash
python main.py
```

The API is available at `http://127.0.0.1:8000`.

## Frontend

```bash
cd frontend
npm install
npm run dev
```

The app is available at `http://localhost:3000`.
