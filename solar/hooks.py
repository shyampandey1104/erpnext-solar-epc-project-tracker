# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "solar"
app_title = "Erpnext Solar Epc Project Tracker"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Solar Epc Project Tracker for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/solar/css/solar.bundle.css"
app_include_js = "/assets/solar/js/solar.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "solar.engine.on_document_submit",
        "on_cancel": "solar.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "solar.engine.daily_scheduled_sync"
    ]
}
