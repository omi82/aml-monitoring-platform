````markdown
# 🏦 Enterprise AML Monitoring & Investigation Platform

An end-to-end **Anti-Money Laundering (AML) Monitoring & Investigation Platform** built to simulate how financial institutions detect suspicious transactions, generate alerts, create investigation cases, and analyze customer activity.

The project combines **data engineering, PostgreSQL, FastAPI, SQLAlchemy, rule-based AML detection, case management, JWT authentication, and a React/TypeScript analytics dashboard** into one enterprise-style application.

> **Data:** Synthetic financial data | **Status:** Core platform completed

---

## 🚀 Key Features

- 🔍 **AML Transaction Monitoring** with 5 detection rules
- 🚨 **Automated Alert Generation** with severity, risk score, and reason
- 📁 **Case Management** for investigation workflows
- 👤 **Customer 360** with customer, account, transaction, alert, and case context
- 📊 **AML Dashboard** with operational KPIs and visual analytics
- 🔐 **JWT Authentication** and protected APIs
- 🔄 **ETL Pipeline** for synthetic financial data
- 🗄️ **PostgreSQL Data Warehouse**
- 📡 **REST APIs** using FastAPI
- ⚡ **Pagination, Filtering & Sorting**
- 🗃️ **Alembic Database Migrations**
- 🐳 **Docker-ready architecture**
- 🧪 **Testing and code-quality tooling**

---

## 🔍 AML Detection Rules

The AML engine uses a modular rule-based architecture.

### Implemented Rules

| Rule | Description |
|---|---|
| Large Value Transaction | Detects transactions above configured thresholds |
| High Risk Country | Identifies transactions involving high-risk countries |
| Transaction Velocity | Detects unusually frequent transaction activity |
| Structuring | Identifies potentially structured transaction patterns |
| Dormant Account | Detects suspicious activity from previously inactive accounts |

Each triggered rule generates an alert containing:

```text
Transaction
Rule
Severity
Risk Score
Status
Reason
````

---

## 🔄 AML Investigation Lifecycle

```text
Transaction
     ↓
AML Rule Engine
     ↓
Suspicious Activity Detection
     ↓
Alert Generation
     ↓
Case Creation
     ↓
Investigation
     ↓
Customer 360
     ↓
Case Management
```

The platform separates **alert detection** from **case investigation**, providing a foundation for an enterprise AML workflow.

---

## 🏗️ System Architecture

```text
                  ┌──────────────────────┐
                  │   React Frontend     │
                  │ TypeScript + MUI     │
                  └──────────┬───────────┘
                             │
                          REST API
                             ↓
                  ┌──────────────────────┐
                  │       FastAPI        │
                  │      API Layer       │
                  └──────────┬───────────┘
                             ↓
              ┌──────────────────────────────┐
              │      Service Layer           │
              │      Repository Layer        │
              │      Authentication          │
              └──────────────┬───────────────┘
                             ↓
                  ┌──────────────────────┐
                  │    SQLAlchemy ORM    │
                  └──────────┬───────────┘
                             ↓
                  ┌──────────────────────┐
                  │     PostgreSQL       │
                  └──────────┬───────────┘
                             ↑
                  ┌──────────────────────┐
                  │    AML Rule Engine   │
                  └──────────┬───────────┘
                             ↑
                  ┌──────────────────────┐
                  │    ETL / Data Gen    │
                  └──────────────────────┘
```

---

## 📊 Showcase Dataset

The current showcase environment contains:

| Dataset      | Records |
| ------------ | ------: |
| Customers    |  20,000 |
| Accounts     |  59,901 |
| Transactions | 100,836 |
| AML Alerts   |  11,570 |
| Cases        |   1,035 |

All data is **synthetically generated** for demonstration purposes.

---

## 📈 Dashboard

The dashboard provides an operational view of AML activity, including:

* Total Transactions
* Total Alerts
* Open Alerts
* Total Cases
* Open Cases
* Critical Cases
* Total Customers
* Average Risk
* Alerts by Severity
* Risk Distribution
* Recent Alerts
* Recent Cases

---

## 👤 Customer 360

The Customer 360 investigation view brings together:

* Customer Profile
* KYC Status
* Risk Category
* Accounts
* Transactions
* AML Alerts
* Investigation Cases
* Investigation Timeline
* AI Investigation Interface

This provides investigators with a consolidated view of customer activity and risk.

---

## 📡 REST API

The backend provides REST APIs for:

```text
Authentication
Customers
Customer 360
Transactions
Alerts
Cases
Dashboard Analytics
Health Monitoring
```

FastAPI also provides interactive API documentation through Swagger/OpenAPI.

---

## 🛠️ Technology Stack

### Backend

* Python
* FastAPI
* Pydantic
* SQLAlchemy
* PostgreSQL
* Alembic
* JWT Authentication

### Frontend

* React
* TypeScript
* Material UI
* React Query
* Recharts

### Data Engineering

* Python
* Pandas
* Synthetic Data Generation
* ETL Pipelines
* Batch Processing

### Development & Infrastructure

* Docker
* Git
* GitHub
* Pytest
* Ruff
* Mypy

---

## 📁 Project Structure

```text
aml-monitoring-platform/
│
├── app/
│   ├── aml_engine/
│   ├── api/
│   ├── core/
│   ├── data_generator/
│   ├── etl/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── frontend/
│   └── src/
│       ├── components/
│       ├── layouts/
│       ├── pages/
│       ├── routes/
│       └── services/
│
├── migrations/
│   └── versions/
│
├── scripts/
├── tests/
├── data/
├── .env.example
├── .gitignore
├── alembic.ini
└── README.md
```

---

## ⚙️ Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/omi82/aml-monitoring-platform.git
cd aml-monitoring-platform
```

### 2. Create Virtual Environment

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure Environment

Create `.env` from the provided example:

```powershell
Copy-Item .env.example .env
```

Configure your PostgreSQL connection and application secrets in `.env`.

> **Never commit `.env` to GitHub.**

### 5. Run Database Migrations

```powershell
alembic upgrade head
```

Verify schema consistency:

```powershell
alembic check
```

### 6. Generate Synthetic Data

```powershell
python -m scripts.generate_data
```

### 7. Load Data

```powershell
python -m scripts.load_data
```

### 8. Start Backend

```powershell
uvicorn app.main:app --reload
```

API:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

### 9. Start Frontend

```powershell
cd frontend
npm install
npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

## 🧪 Testing

Run the test suite with:

```powershell
pytest
```

The project also uses:

```text
Ruff
Mypy
Pytest
```

for code quality and testing.

---

## 🧠 Future Roadmap

The current implementation establishes the core AML monitoring and investigation foundation.

Planned enhancements include:

* Customer ML Risk Scoring
* Sanctions & Watchlist Screening
* SAR/STR Workflow
* False-Positive Feedback Loop
* Configurable AML Rules
* Network & Link Analysis
* Behavioral Anomaly Detection
* Real-Time Transaction Monitoring
* SLA & Case Aging Analytics
* RAG-powered AML Investigation Copilot
* AI Evaluation & Observability

The planned AI layer will be designed as an **investigator decision-support system**, keeping final compliance decisions human-controlled.

---

## 🔒 Disclaimer

This project is an **educational and portfolio implementation** using synthetic financial data.

The AML rules are simplified simulations and should not be considered a production-ready regulatory compliance solution.

A real-world AML platform would require additional security, governance, model validation, regulatory controls, monitoring, auditability, and compliance processes.

---

## 👨‍💻 Author

**Omendra Puri**

**Data Analytics | Data Engineering | AI Engineering**

Built as an end-to-end portfolio project demonstrating how data engineering, backend systems, AML monitoring, investigation workflows, and interactive analytics can be combined into an enterprise financial crime platform.

```
```
