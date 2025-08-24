# Profile and Stats API  

A Django + Django REST Framework (DRF) project that manages Formula 1–inspired data, including Teams, Drivers, Circuits, Races, and Results.  
The project uses MySQL as the database backend and supports token-based authentication.  

---

## 📌 What’s Been Done So Far  

### ✅ Aug 4, 2025  
- Initialized project: **`profile_and_stats_api`**.  
- Created apps: **`core`** and **`analytics`**.  
- Built initial models in `core/models.py` (Teams, Drivers, Circuits, Races, Results).  
- Configured **MySQL** as the default database.  
- Added **Django REST Framework** settings.  

### ✅ Aug 5, 2025  
- Applied migrations for all models.  

### ✅ Aug 6, 2025  
- Created **serializers** for all models.  
- Built **viewsets** for Teams, Drivers, Circuits, Races, Results.  
- Registered API routes for the viewsets in `core/urls.py`.  

### ✅ Aug 12, 2025  
- Updated `core/models.py`:  
  - Changed `stats` field in **Drivers** model from `CharField` → `JSONField`.  
- Fixed serializer configuration in `core/serializers.py`.  
- Cleaned up routes in `core/urls.py` by removing duplicate `DriverViewSet`.  
- Updated `profile_and_stats_api/urls.py` to include `api-auth-token/` for token authentication.  
- Added **`MYSQLServer.py`** script to seed initial data into the database.  

---

## 🚀 Features Implemented  
- **Core models**: Teams, Drivers, Circuits, Races, Results.  
- **Driver stats as JSON** for structured data (DNFs, wins, podiums, championships, etc.).  
- **REST API** using DRF viewsets and serializers.  
- **MySQL integration** as the primary database.  
- **Token authentication** available via `/api-auth-token/`.  
- **Data seeding script** (`MYSQLServer.py`).  

---

## API Endpoints (So Far)
- **Endpoint**	    **Method**	**Description**
- /api/teams/	    GET/POST	List or create teams
- /api/drivers/	    GET/POST	List or create drivers
- /api/circuits/	GET/POST	List or create circuits
- /api/races/	    GET/POST	List or create races
- /api/results/	    GET/POST	List or create results
- /api-auth-token/	POST	    Obtain auth token

### ✅ Aug 24, 2025  
- Updated `analytics/views.py`:
  - Created `DriverStatsView` and `DriverComparisonsView` 
- Updated `README.md`
