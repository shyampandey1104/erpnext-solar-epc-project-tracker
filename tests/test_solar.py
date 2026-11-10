"""Unit tests for SolarEPCEngine."""

from solar.engine import SolarEPCEngine, SolarSiteSurvey


def test_solar_pv_design_sizing():
    survey = SolarSiteSurvey(
        project_id="SOL-001",
        client_name="Sharma Manufacturing Ltd",
        sanctioned_load_kw=50.0,
        rooftop_area_sqft=6000.0,  # Can hold 60 kWp
        monthly_bill_avg=45000.0,
        discom_name="MSEDCL",
    )
    engine = SolarEPCEngine()
    design = engine.design_system(survey)

    # Capped at sanctioned load 50 kWp
    assert design.recommended_capacity_kwp == 50.0
    assert design.est_annual_generation_kwh > 50000.0
    assert design.est_annual_savings > 400000.0
    assert design.payback_period_years > 0
