"""/get   /post /put /delete /patch"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.report_service import ReportService

report_router = APIRouter()


@report_router.get("/report")
async def get_report():
    """Get health report"""
    return {"message": "Health report retrieved successfully"}