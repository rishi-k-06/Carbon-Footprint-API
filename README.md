# Carbon Footprint API 🏗️

A RESTful API that calculates enterprise-level carbon emissions based on logistical data, utility consumption metrics, and global emission factors.

## Description
A RESTful API that calculates enterprise-level carbon emissions based on logistical data, utility consumption metrics, and global emission factors.

## Key Features
- **Multi-Scope Tracking:** Categorizes emissions into Scope 1 (Direct), Scope 2 (Utilities), and Scope 3 (Supply Chain).
- **Standardized Conversions:** Utilizes IPCC-aligned emission factors for accurate CO2e calculations.
- **Reporting Analytics:** Generates monthly and quarterly sustainability reports via JSON endpoints.

## Tech Stack
- **Language:** Python
- **Libraries:** Flask, PostgreSQL, Pandas, Marshmallow
- **Model:** GHG Protocol-based emission calculation engine.

## Engineering Logic
- **Backend:** The API is built using Flask with a focus on high-concurrency data ingestion. It validates incoming logistical payloads and maps them to localized emission factors.
- **Software Engine:** A mathematical core engine processes activity data (kWh, liters, km) to output normalized mass values in metric tons of CO2e.
