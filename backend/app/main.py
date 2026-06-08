from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.db import Base, engine

# Models
from app.models.user import User
from app.models.dataset import Dataset
from app.models.dataset_version import DatasetVersion
from app.models.forecast_project import ForecastProject
from app.models.forecast_scenario import ForecastScenario
from app.models.forecast import Forecast
from app.models.forecast_comment import ForecastComment
from app.models.forecast_revision import ForecastRevision
from app.models.executive_report import ExecutiveReport
from app.models.model_accuracy import ModelAccuracy
from app.models.dashboard_widget import DashboardWidget
from app.models.notification import Notification
from app.models.report import Report
from app.models.integration import Integration
from app.models.alert import Alert
from app.models.automation import AutomationJob
from app.models.project_activity import ProjectActivity
from app.models.project_permission import ProjectPermission
from app.models.report_share import ReportShare
from app.models.report_schedule import ReportSchedule


# Routers
from app.routers.auth_router import router as auth_router
from app.routers.workspace_router import router as workspace_router
from app.routers.scenario_router import router as scenario_router
from app.routers.dataset_router import router as dataset_router
from app.routers.forecast_router import router as forecast_router
from app.routers.insights_router import router as insights_router
from app.routers.executive_router import router as executive_router
from app.routers.collaboration_router import router as collaboration_router
from app.routers.accuracy_router import router as accuracy_router
from app.routers.report_router import router as report_router
from app.routers.notification_router import router as notification_router
from app.routers.dashboard_router import router as dashboard_router
from app.routers.activity_router import router as activity_router
from app.routers.permission_router import router as permission_router
from app.routers.report_share_router import router as report_share_router
from app.routers.dataset_compare_router import router as dataset_compare_router
from app.routers.report_schedule_router import router as report_schedule_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Advanced AI Demand Forecasting SaaS",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(workspace_router)
app.include_router(scenario_router)
app.include_router(dataset_router)
app.include_router(forecast_router)
app.include_router(insights_router)
app.include_router(executive_router)
app.include_router(collaboration_router)
app.include_router(accuracy_router)
app.include_router(report_router)
app.include_router(notification_router)
app.include_router(dashboard_router)
app.include_router(activity_router)
app.include_router(permission_router)
app.include_router(report_share_router)
app.include_router(dataset_compare_router)
app.include_router(report_schedule_router)



@app.get("/")
def root():
    return {
        "status": "success",
        "message": "Advanced AI Demand Forecasting SaaS API running",
        "database": "demand_forecasting_phase5",
    }