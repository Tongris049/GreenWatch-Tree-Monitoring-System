  	PIPELIN-DESIGN

1. Pipeline Flow Structure (Visual Overview)

	GREENWATCH DATA FLOW PIPELINE
   ─────────────────────────────────────────────
KoBoToolbox Form (Inventory / Monitoring)
        │
        ▼
KoBoToolbox Cloud (server storage)
        │
        ▼
REST Service (KoBo → Endpoint connection)
        │  (JSON data automatically sent)
        ▼
Python Endpoint (hosted free on Render)
        │  (Receives data and saves to SQL)
        ▼
MySQL Database (WorkBench / Online)
        │  (Data stored & ready for use)
        ▼
Power BI Dashboard (auto-refresh)
        │  (Visuals for Central GreenWatch HQ)
        ▼
Future Expansion
       • NGO Servers (decentralized)
       • State Forestry Databases
       • Synchronization to Central GreenWatch DB


2. Pipeline Description (Text Explanation)

I. KoboCollect App (Field Submission)

Data will be collected in the field using the KoboCollect mobile app. Submissions will include tree details, GPS coordinates, photos, and monitoring updates.

II. KoboToolbox Cloud Server

All submitted data will sync to the KoboToolbox cloud platform. This will serve as the central location for receiving raw field entries.

III. REST API Service (Data Extraction)

A REST API endpoint will be used to pull new submissions from KoboToolbox.
The endpoint will receive JSON data and prepare it for the next processing stage.

IV. Python Processing Script (Upcoming Development)

A lightweight Python script will be developed to run on a small server.
Its responsibilities will include:

fetching form data

cleaning and validating records

mapping each field to the correct database table

managing unique Tree IDs

supporting monitoring relationships

V. MySQL Database (Already Created)

The SQL database and key tables have already been set up.
Tables include:

baseline inventory

monitoring and evaluation

planting entity

GPS/location details

This provides the foundation for structured storage.

VI. Visualization Layer (Planned)

Power BI will later be connected to the SQL database to provide real-time dashboards displaying:

trees planted

local government distribution

monitoring progress

survival rates

planting agent verification

mapped GPS points

VII. Future Expansion:
The GreenWatch system is designed with scalability in mind. Planned expansions include:

NGO Servers (Decentralized): Allowing partner NGOs to manage and upload data independently while maintaining central oversight.

State Forestry Databases: Integrating state-level forestry data to enrich the centralized database and support broader analysis.

Synchronization to Central GreenWatch DB: Ensuring all decentralized and state-level data is automatically synchronized to the central system for real-time reporting and visualization.