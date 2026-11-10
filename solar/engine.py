"""Solar EPC Plant Sizing & Project Tracker for ERPNext."""

from typing import Dict, Any, List, Optional
from pydantic import BaseModel


class SolarSiteSurvey(BaseModel):
    project_id: str
    client_name: str
    sanctioned_load_kw: float
    rooftop_area_sqft: float
    monthly_bill_avg: float
    discom_name: str  # e.g. MSEDCL, Tata Power, Adani Electricity


class SolarPVDesign(BaseModel):
    recommended_capacity_kwp: float
    num_panels: int
    panel_wattage: int = 540  # Mono PERC 540W
    inverter_capacity_kw: float
    est_annual_generation_kwh: float
    est_annual_savings: float
    payback_period_years: float


class SolarEPCEngine:
    """Calculates PV rooftop capacity, generation yield, and subsidy milestones."""

    SQFT_PER_KWP = 100.0  # Approx 100 sq.ft required per 1 kWp
    ANNUAL_KWH_PER_KWP = 1450.0  # Average solar irradiance in India (~4.0 peak sun hours/day)
    TARIFF_PER_KWH = 8.50  # Average commercial/residential power tariff

    def design_system(self, survey: SolarSiteSurvey) -> SolarPVDesign:
        # Max capacity constrained by rooftop area and sanctioned load
        area_capacity = survey.rooftop_area_sqft / self.SQFT_PER_KWP
        load_capacity = survey.sanctioned_load_kw * 1.0  # Max 100% of sanctioned load under net metering rules

        optimal_capacity = round(min(area_capacity, load_capacity), 1)
        num_panels = int((optimal_capacity * 1000) / 540)
        inverter_kw = round(optimal_capacity * 0.95, 1)

        annual_generation = round(optimal_capacity * self.ANNUAL_KWH_PER_KWP, 0)
        annual_savings = round(annual_generation * self.TARIFF_PER_KWH, 0)

        # Approx ₹45,000 per kWp turnkey installation cost
        project_cost = optimal_capacity * 45000.0
        payback = round(project_cost / max(annual_savings, 1.0), 1)

        return SolarPVDesign(
            recommended_capacity_kwp=optimal_capacity,
            num_panels=num_panels,
            inverter_capacity_kw=inverter_kw,
            est_annual_generation_kwh=annual_generation,
            est_annual_savings=annual_savings,
            payback_period_years=payback,
        )
