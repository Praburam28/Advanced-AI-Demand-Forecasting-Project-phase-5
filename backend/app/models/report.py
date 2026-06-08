from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from app.database.db import Base

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    report_type = Column(String(100), default="forecast")
    file_path = Column(String(500), nullable=True)
    status = Column(String(50), default="generated")

    forecast_id = Column(Integer, ForeignKey("forecasts.id"), nullable=True)
    project_id = Column(Integer, ForeignKey("forecast_projects.id"), nullable=True)
    created_by = Column(Integer, ForeignKey("users.id"))

    created_at = Column(DateTime, default=datetime.utcnow)