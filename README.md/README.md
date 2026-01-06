# 🌳 GreenWatch — Tree Inventory/Monitoring & Transparency System

GreenWatch is a real-time tree monitoring project designed to improve transparency, accountability, and data-driven decision-making within Nigeria’s green ecosystem.  
The project combines field data collection, geolocation validation, automated backend processing, and dynamic reporting dashboards to ensure credible monitoring of tree planting efforts.

---

## 📌 Project Objectives

- Create a centralize database taking inventory of planted trees across different locations.
- Improve transparency and monitoring of planted trees across different locations.
- Validate field activity using GPS, timestamp, images, and standardized forms.
- Build an automated backend pipeline linking KoBoToolbox data to a SQL database.
- Generate real-time insights using Power BI dashboards.
- Provide long-term documentation and version tracking of every improvement made in the project.

---

## 🗂️ Repository Structure

GreenWatch Project/
│
├── docs/
│ ├── progress-log/
│ ├── pipeline-design/
│ ├── tools-log/
│ └── project-overview/
│
├── sql/
│ └── (SQL scripts for database design, transformations, and validation)
│
├── python/
│ └── (ETL scripts for automation, GPS validation logic, API connections)
│
├── kobo/
│ └── (Form A & Form B templates, XLSForms, skip logic notes)
│
├── powerbi/
│ └── (Dashboard files, model documentation, M scripts)
│
├── images/
│ └── (Screenshots, workflow diagrams, field examples)
│
└── README.md


---

## 🛠️ Tools & Technologies

- **KoBoToolbox** — Data collection for planting and monitoring  
- **Python** — Automation scripts, validations, ETL pipeline  
- **SQL (MySQL)** — Backend database for structured storage  
- **Power BI** — Interactive dashboards and real-time insights  
- **GitHub** — Documentation, tracking, and version control  

---

## 📍 GPS Validation Logic (Overview)

GreenWatch uses a tolerance-based GPS matching system that ensures:
- A field agent cannot submit a monitoring report (Form B) if the GPS does not closely match the original planting location (Form A).  
- This helps reduce fraud and ensures field authenticity.  

More technical details will appear under `docs/pipeline-design/`.

---

## 📈 Project Status  
This repository is being actively structured, documented, and expanded.  
More files and components will be added as each module is completed.

---

## 👩‍💻 Author  
**Simon Tongriyang Mwantok**  
Data Analyst | Mentor | Field Monitoring Specialist | Power BI | SQL | Python  

---




### Data Validation & Error Handling (Casualty Management)

GreenWatch is designed to handle real-world data imperfections without data loss.

1. **Inventory as Source of Truth**
   - All valid Tree_IDs originate from Form A (Tree Inventory).
   - Extracted Tree_IDs are stored in a validated registry.
   - Monitoring records (Form B) must reference an existing Tree_ID.

2. **Separation of Raw and Validated Data**
   - Raw field submissions are preserved in their original form.
   - Validation occurs after collection, not during submission.
   - This ensures transparency, traceability, and auditability.

3. **Graceful Handling of Invalid Records**
   - Records that fail validation are flagged as invalid or unlinked.
   - Invalid records are not deleted or overwritten.
   - This allows investigation, correction, and accountability.

4. **Audit-First Architecture**
   - Every submission remains traceable to its source.
   - The system supports error analysis and institutional review.
   - This approach aligns with real-world monitoring and evaluation standards.



### Location-Based Validation for Transparency

GreenWatch incorporates GPS-based validation to ensure field presence and accountability.

1. **Baseline Location**
   - Each Tree_ID is assigned a reference GPS coordinate at inventory (Form A).
   - This location represents the official planting position.

2. **Monitoring Location Capture**
   - All monitoring records (Form B) capture GPS coordinates at the time of submission.

3. **Proximity-Based Validation**
   - Monitoring GPS points are compared against the reference tree location.
   - Validation is based on distance thresholds rather than exact matches to allow GPS drift.

4. **Confidence Classification**
   - Records are classified as Valid, Review Required, or Invalid.
   - No data is deleted; all submissions remain auditable.

5. **Transparency Outcome**
   - This approach discourages false reporting while preserving flexibility.
   - Decision-makers can assess monitoring credibility spatially and temporally.


