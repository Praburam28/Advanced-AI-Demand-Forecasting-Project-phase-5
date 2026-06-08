# 🚀 Advanced AI Demand Forecasting SaaS

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-UI-38B2AC?style=for-the-badge&logo=tailwindcss&logoColor=white)

A professional **AI-powered Demand Forecasting SaaS platform** built with **FastAPI, React, MySQL, Machine Learning, Business Intelligence Dashboards, Reports, Role-Based Access, and Modern SaaS UI**.

---

## 📌 Project Overview

**Advanced AI Demand Forecasting SaaS** helps businesses forecast demand, revenue, cost, profit, and model accuracy using uploaded datasets and machine learning models.

The system provides:

- 📊 Forecast generation
- 📁 Dataset management
- 🧠 AI insights
- 📈 Executive dashboards
- 📑 PDF / Excel reports
- 👥 Collaboration
- 🔐 Authentication and role-based access
- 🌗 Dark / light UI
- ⚡ Modern SaaS interface

---

## ✨ Key Features

### 🔐 Authentication Module
- Login
- Register
- Forgot password
- Reset password
- JWT authentication
- Protected routes
- Admin / Manager / User roles

### 📁 Dataset Management
- Upload CSV / Excel datasets
- Dataset versioning
- Upload history
- Dataset archive
- Dataset comparison
- Row and column tracking

### 🤖 Forecasting Engine
- Generate demand forecasts
- Multiple ML models:
  - Linear Regression
  - Random Forest
  - Gradient Boosting
- Revenue forecasting
- Profit forecasting
- Cost forecasting
- Accuracy metrics:
  - MAE
  - MSE
  - RMSE
  - MAPE
  - R² Score

### 🧠 AI Insights
- Automated forecasting summaries
- Business recommendations
- High-growth product detection
- Declining product detection
- Demand opportunity identification

### 📊 Business Intelligence
- Executive dashboard
- Revenue forecast
- Profit forecast
- Cost analysis
- Business KPIs
- Regional and category analytics

### 🧪 Scenario Planning
- What-if analysis
- Sales growth adjustment
- Seasonality adjustment
- Demand factor adjustment
- Scenario comparison
- Save and reuse scenarios

### 👥 Collaboration
- Forecast comments
- Revision history
- Report sharing
- Project activity timeline
- Team collaboration support

### 📑 Reports
- Forecast reports
- Executive reports
- PDF download
- Excel download
- Report scheduling
- Professional report templates

### 🎨 Modern SaaS Frontend
- Responsive dashboard
- Colorful UI
- Dark / light theme
- Sidebar navigation
- Top navbar
- Command palette
- Profile and settings pages

---

## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React, Vite, Tailwind CSS |
| Icons | Lucide React |
| Charts | Recharts |
| Backend | FastAPI |
| Database | MySQL |
| ORM | SQLAlchemy |
| Authentication | JWT |
| ML | scikit-learn, pandas, numpy |
| Reports | ReportLab, OpenPyXL |

---

## 📂 Project Structure

```bash
advanced-ai-demand-forecasting-saas/
│
├── backend/
│   ├── app/
│   │   ├── database/
│   │   ├── models/
│   │   ├── routers/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── uploads/
│   │   ├── generated_reports/
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   ├── layouts/
│   │   ├── pages/
│   │   ├── utils/
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── index.html
│
└── README.md
```

---

## ⚙️ Backend Setup

### 1️⃣ Navigate to backend

```bash
cd backend
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
```

### 3️⃣ Activate virtual environment

#### Windows PowerShell

```bash
venv\Scripts\Activate.ps1
```

If activation is blocked:

```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
venv\Scripts\Activate.ps1
```

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Run backend server

```bash
python -m uvicorn app.main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

Swagger API Docs:

```text
http://127.0.0.1:8000/docs
```

---

## 🎨 Frontend Setup

### 1️⃣ Navigate to frontend

```bash
cd frontend
```

### 2️⃣ Install dependencies

```bash
npm install
```

### 3️⃣ Run frontend

```bash
npm run dev
```

Frontend runs at:

```text
http://localhost:5173
```

---

## 🗄️ Database Setup

Create a MySQL database:

```sql
CREATE DATABASE demand_forecasting_phase5;
```

Example `.env`:

```env
DATABASE_URL=mysql+pymysql://root:your_password@localhost:3306/demand_forecasting_phase5
SECRET_KEY=forecast_ai_secret_key
ALGORITHM=HS256
```

---

## 🔑 Default Test Admin

Use this request in Swagger:

```json
{
  "name": "Praburam",
  "email": "prabu@gmail.com",
  "password": "prabu123",
  "role": "admin"
}
```

Login:

```json
{
  "email": "prabu@gmail.com",
  "password": "prabu123"
}
```

Copy `access_token` and authorize Swagger.

---

## 📊 Dataset Format

Upload CSV dataset with these columns:

```csv
Date,Product,Category,Region,Units_Sold,Unit_Price,Revenue,Cost,Profit
```

Example:

```csv
01-01-2024,Laptop,Electronics,North,120,50000,6000000,4800000,1200000
```

Required columns:

| Column | Description |
|---|---|
| Date | Sales date |
| Product | Product name |
| Category | Product category |
| Region | Sales region |
| Units_Sold | Units sold |
| Unit_Price | Price per unit |
| Revenue | Total revenue |
| Cost | Total cost |
| Profit | Revenue minus cost |

---

## 🔄 Recommended Workflow

```text
1. Register / Login
2. Create Forecast Workspace
3. Upload Dataset
4. Generate Forecast
5. View Accuracy Center
6. Check AI Insights
7. Generate Report
8. Download PDF / Excel
9. Analyze Dashboard Analytics
```

---

## 📡 Main API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/auth/register` | Register user |
| POST | `/api/auth/login` | Login user |
| POST | `/api/auth/forgot-password` | Forgot password |
| POST | `/api/auth/reset-password` | Reset password |
| GET | `/api/workspaces/` | List workspaces |
| POST | `/api/workspaces/` | Create workspace |
| POST | `/api/datasets/upload` | Upload dataset |
| GET | `/api/datasets/` | List datasets |
| POST | `/api/forecasts/generate` | Generate forecast |
| GET | `/api/forecasts/` | Forecast history |
| GET | `/api/accuracy/dashboard` | Accuracy dashboard |
| GET | `/api/insights/` | AI insights |
| POST | `/api/reports/` | Generate report |
| GET | `/api/reports/{id}/download/pdf` | Download PDF |
| GET | `/api/reports/{id}/download/excel` | Download Excel |

---

## 📸 Screenshots Template

Add your screenshots inside:

```bash
assets/screenshots/
```

Then update this section:

### 🖥️ Dashboard

![Dashboard](assets/screenshots/dashboard.png)

### 📊 Forecast

![Forecast](assets/screenshots/forecast.png)

### 📑 Reports

![Reports](assets/screenshots/reports.png)

### 🧠 AI Insights

![AI Insights](assets/screenshots/ai-insights.png)

---

## 🧪 Testing Checklist

- [ ] Backend runs without error
- [ ] Frontend runs without white screen
- [ ] Register works
- [ ] Login returns JWT token
- [ ] Protected routes work
- [ ] Dataset upload works
- [ ] Forecast generation works
- [ ] Accuracy center displays values
- [ ] Reports generate successfully
- [ ] PDF download works
- [ ] Excel download works
- [ ] Dark mode works
- [ ] Sidebar routes work

---

## 🚀 Future Enhancements

- Real email delivery for forgot password
- Email delivery for scheduled reports
- Drag-and-drop dashboard widgets
- WebSocket-based real-time collaboration
- Admin audit logs
- Docker deployment
- Cloud deployment
- CI/CD pipeline
- Payment integration
- Multi-tenant SaaS support

---

## 🤝 Contributing

Contributions are welcome.

```bash
fork repository
create feature branch
commit changes
push branch
open pull request
```

---

## 👨‍💻 Author

**Praburam R**

- 💼 Project: Advanced AI Demand Forecasting SaaS
- 🧠 Domain: Machine Learning + Business Intelligence
- 🛠️ Stack: FastAPI + React + MySQL

---

## ⭐ GitHub Repository Tips

Use this GitHub description:

```text
AI-powered Demand Forecasting SaaS built with FastAPI, React, MySQL, ML models, BI dashboards, reports, JWT auth, and modern SaaS UI.
```

Use these GitHub topics:

```text
fastapi
react
machine-learning
demand-forecasting
saas
mysql
jwt-authentication
business-intelligence
tailwindcss
forecasting
```

---

## 📄 License

This project is for educational and portfolio purposes.

You may add an MIT License if publishing publicly.

👨‍💻 Author

PrabuRam R
