# F1 Driver & Stats API Documentation

## Overview

This API provides access to Formula 1 data, including driver profiles, team information, race results, and analytical statistics. It is built with Django and Django REST Framework, featuring both a core data API and an analytics module.

**Base URL:** `https://itsaiight.pythonanywhere.com`

---

## 1. Core API Endpoints

The core API manages the fundamental F1 data entities. All endpoints support `GET` (public) and `POST/PUT/PATCH/DELETE` (admin-only).

**Base Path:** `/core/`

### 1.1. Teams

- **Endpoint:** `GET/POST /core/teams/`
- **Endpoint (Single):** `GET/PUT/DELETE /core/teams/{id}/`
- **Description:** Retrieve or manage F1 teams.
- **Authentication:** Read (Public), Write (Admin Token/Session)
- **Response:** Array of team objects.
  ```json
  [
    {
      "team_id": 5,
      "name": "Mercedes-AMG Petronas",
      "country": "Germany"
    }
  ]
  ```

### 1.2. Drivers

- **Endpoint:** `GET/POST /core/drivers/`
- **Endpoint (Single):** `GET/PUT/DELETE /core/drivers/{id}/`
- **Description:** Retrieve or manage F1 drivers, including their stats and team info.
- **Authentication:** Read (Public), Write (Admin Token/Session)
- **Response:** Array of driver objects.
  ```json
  [
    {
      "driver_id": 1,
      "full_name": "Lewis Hamilton",
      "number": 44,
      "nationality": "British",
      "debut_year": 2007,
      "current_team": { ...team object... },
      "stats": JSONFIELD,
      "image_url": "http://en.wikipedia.org/wiki/Lewis_Hamilton" #opted for wikipedia urls
    }
  ]
  ```

### 1.3. Circuits

- **Endpoint:** `GET/POST /core/circuits/`
- **Endpoint (Single):** `GET/PUT/DELETE /core/circuits/{id}/`
- **Description:** Retrieve or manage F1 circuits.
- **Authentication:** Read (Public), Write (Admin Token/Session)
- **Response:** Array of circuit objects.
  ```json
  [
    {
      "circuit_id": 9,
      "name": "Silverstone Circuit",
      "location": "Northamptonshire, UK",
      "length_km": 5.891
    }
  ]
  ```

### 1.4. Races

- **Endpoint:** `GET/POST /core/races/`
- **Endpoint (Single):** `GET/PUT/DELETE /core/races/{id}/`
- **Description:** Retrieve or manage F1 race events.
- **Authentication:** Read (Public), Write (Admin Token/Session)
- **Response:** Array of race objects with nested circuit data.
  ```json
  [
    {
      "race_id": 12,
      "name": "British Grand Prix",
      "round_number": 10,
      "year": 2025,
      "circuit": { ...circuit object... },
      "date": "2025-07-06"
    }
  ]
  ```

### 1.5. Results

- **Endpoint:** `GET/POST /core/results/`
- **Endpoint (Single):** `GET/PUT/DELETE /core/results/{id}/`
- **Description:** Retrieve or manage race results.
- **Authentication:** Read (Public), Write (Admin Token/Session)
- **Response:** Array of result objects with nested driver and race data.
  ```json
  [
    {
      "result_id": 1,
      "driver": { ...driver object... },
      "race": { ...race object... },
      "position": 1,
      "points": 25.0
    }
  ]
  ```

---

## 2. Analytics API Endpoints

The analytics API provides calculated statistics and head-to-head comparisons. All endpoints are public.

**Base Path:** `/analytics/`

### 2.1. Driver Statistics

- **Endpoint:** `GET /analytics/drivers/{full_name}/stats/`
- **Description:** Get career summary statistics for a specific driver (total starts, wins, points) for this current season.
- **Parameters:** `full_name` (URL path parameter)
- **Authentication:** Public
- **Example Request:** `GET /analytics/drivers/Lewis Hamilton/stats/`
- **Response:**
  ```json
  {
    "driver": "Lewis Hamilton",
    "starts": 14,
    "wins": 0,
    "points": 95
  }
  ```

### 2.2. Driver Comparison

- **Endpoint:** `GET /analytics/comparison/`
- **Description:** Get a head-to-head comparison between two drivers, including stats and direct race outcomes from this season.
- **Parameters:**
  - `a` (query): Full name of the first driver (e.g., `Lewis Hamilton`)
  - `b` (query): Full name of the second driver (e.g., `Fernando Alonso`)
- **Authentication:** Public
- **Example Request:** `GET /analytics/comparison/?a=Lewis%20Hamilton&b=Fernando%20Alonso`
- **Response:**
  ```json
  {
    "Lewis Hamilton": {
      "wins": 0,
      "podiums": 0,
      "points": 95
    },
    "Fernando Alonso": {
      "wins": 0,
      "podiums": 0,
      "points": 26
    },
    "head_to_head": {
      "races": 14,
      "a_wins": 13,
      "b_wins": 1
    }
  }
  ```

---

## 3. Authentication

The API uses a dual authentication system:

1.  **Public Access:** All `GET` requests are available without authentication.
2.  **Admin Access:** `POST`, `PUT`, `PATCH`, and `DELETE` requests require administrator privileges.

### How to Authenticate for Admin Actions

**Method 1: Token Authentication (Recommended for programmatic access)**

1.  Obtain a token via the endpoint: `POST /api-auth-token/`
    - **Body (form-data):** `username` & `password`
    - **Response:** `{ "token": "{{token}}" }`
2.  Use the token in the `Authorization` header for subsequent requests:
    `Authorization: Token {{token}}`

**Method 2: Session Authentication (Recommended for browsers)**

1.  Log in via the web interface: `GET /login/`
2.  Your browser will maintain a session cookie, granting you access to admin functions on the site and in the browsable API.

---

## 4. Web Interface & Navigation

The API includes user-friendly HTML pages for easy navigation.

- **Homepage (`/`)**: The main hub with links to the Admin Panel, Core API, and Analytics.
- **Analytics Home (`/analytics/`)**: A dedicated page with forms to quickly access driver stats and comparisons by entering driver names.
- **Browsable API:** Navigate to any API endpoint (e.g., `/core/drivers/`) in a web browser to use the interactive DRF browsable API, which allows you to explore and test endpoints easily.

---

## 5. Error Handling

Standard HTTP status codes are used.

- `200 OK`: Request was successful.
- `400 Bad Request`: The request was malformed (e.g., missing query parameters `a` or `b` for comparison).
- `404 Not Found`: The requested resource was not found (e.g., a driver with the provided name does not exist).
- `401 Unauthorized` / `403 Forbidden`: Trying to perform an admin action without valid credentials.

Errors typically return a JSON response with a descriptive message:

```json
{
  "error": "Please provide 'a' and 'b' query params"
}
```

---

## 6. Example Usage Scenarios

**1. Building a Driver Profile Page:**

1.  Fetch driver details: `GET /core/drivers/?full_name=Lewis Hamilton`
2.  Fetch their career stats: `GET /analytics/drivers/Lewis Hamilton/stats/`

**2. Creating a Head-to-Head Comparison Tool:**

1.  Use the comparison endpoint: `GET /analytics/comparison/?a=verstappen&b=leclerc`
2.  Display the returned wins, podiums, points, and head-to-head record.

**3. Populating a Database (Admin):**

1.  Obtain an auth token.
2.  Create a new team: `POST /core/teams/` with `{"name": "Aston Martin", "country": "UK"}`
3.  Create a new driver for that team: `POST /core/drivers/` with the driver's details and the team's ID.

---

## 7. Data Models (For Reference)

| Model   | Key Fields                                                                                                 |
| :------ | :--------------------------------------------------------------------------------------------------------- |
| Team    | `team_id`, `name` `country`                                                                                |
| Driver  | `driver_id`, `full_name`, `number`, `nationality`, `debut_year`, `current_team` (FK), `stats`, `image_url` |
| Circuit | `circuit_id`, `name`, `location`, `length_km`                                                              |
| Race    | `race_id`, `name`, `round_number`, `year`, `circuit` (FK), `date`                                          |
| Result  | `result_id`, `driver` (FK), `race` (FK), `position`, `points`                                              |

---

## Development Timeline

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

- **Endpoint** **Method** **Description**
- /api/teams/ GET/POST List or create teams
- /api/drivers/ GET/POST List or create drivers
- /api/circuits/ GET/POST List or create circuits
- /api/races/ GET/POST List or create races
- /api/results/ GET/POST List or create results
- /api-auth-token/ POST Obtain auth token

### ✅ Aug 24, 2025

- Updated `analytics/views.py`:
  - Created `DriverStatsView` and `DriverComparisonsView`
- Updated `README.md`

## ✅ Aug 26, 2025

- Created urls.py for the analytics app
- Fixed syntax issues in analytics/urls.py and analytics/views.py
- Updated core/views.py:
  - Removed all ListAPIViews
- Updated urls.py accordingly

## ✅ Aug 27, 2025

- In a newly create branch "core-views-update" I created a permissions viewset to reduce redundant code
- Generated templates for function-based views in analytics and core apps
- Added function-based views for both apps:
  - Landing page view in core
  - Analytics in home page view in analytics
- Changed logout redirect URL
- Updated home.html:
  - Removed extra buttons
- Created requirements.txt
- Collected static files
- Updated settings.py for deployment
- Updated `README.md`
