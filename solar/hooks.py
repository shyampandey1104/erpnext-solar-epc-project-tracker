# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "solar"
app_title = "Erpnext Solar Epc Project Tracker"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Solar Epc Project Tracker - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/solar/css/solar.bundle.css"
app_include_js = "/assets/solar/js/solar.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Erpnext Solar Epc Project Tracker Entry": {
        "validate": "solar.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "solar.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "solar.tasks.hourly_sync"
    ],
    "daily": [
        "solar.tasks.daily_reconciliation"
    ],
    "weekly": [
        "solar.tasks.weekly_digest"
    ]
}
