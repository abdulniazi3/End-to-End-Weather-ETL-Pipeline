# Weather ETL Pipeline

An end-to-end ETL pipeline that extracts live weather data from OpenWeather API, transforms it using Python Pandas, and loads it into PostgreSQL. The database is containerized using Docker.

## Architecture

```
OpenWeather API
        |
        ↓
Python Extract
        |
        ↓
Pandas Transformation
        |
        ↓
SQLAlchemy Loader
        |
        ↓
PostgreSQL (Docker)
        |
        ↓
SQL Analytics
```

## Features

- Extracts live weather data from REST API
- Handles JSON data parsing
- Cleans and transforms data using Pandas
- Loads data into PostgreSQL
- Uses SQLAlchemy for database connection
- PostgreSQL containerized with Docker
- Environment variables for sensitive credentials
- SQL analytical queries
- Automated ETL structure

## Technologies Used

- Python
- Pandas
- Requests
- PostgreSQL
- SQLAlchemy
- Docker
- REST API
- SQL

## Project Structure

```
ETL-Pipeline/
│
├── src/
│   ├── extract.py       # API data extraction
│   ├── transform.py     # Data cleaning
│   ├── load.py          # Database loading
│   └── main.py          # ETL workflow
│
├── docker/
│   └── docker-compose.yml
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── tests/
│   └── test_etl.py
│
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Clone Repository

```bash
git clone <repository-url>
cd ETL-Pipeline
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```
API_KEY=your_openweather_api_key

DB_USER=postgres
DB_PASSWORD=postgres123
DB_HOST=localhost
DB_PORT=5432
DB_NAME=weather_db
```

### 5. Start PostgreSQL with Docker

```bash
cd docker
docker compose up -d
```

### 6. Run ETL Pipeline

From project root:

```bash
python src/main.py
```

## Database Schema

Table: `weather_data`

| Column | Type |
|---|---|
| id | SERIAL |
| city | VARCHAR |
| temperature | FLOAT |
| humidity | INT |
| condition | VARCHAR |
| created_at | TIMESTAMP |

## Example SQL Analytics

Average temperature:

```sql
SELECT AVG(temperature)
FROM weather_data;
```

Highest recorded temperature:

```sql
SELECT MAX(temperature)
FROM weather_data;
```

Weather history:

```sql
SELECT *
FROM weather_data
ORDER BY created_at;
```

## Future Improvements

- Add Airflow scheduling
- Add data quality checks
- Add logging system
- Containerize Python application
- Add CI/CD pipeline
- Add dashboard using Power BI

## Author

Abdul Rahman Khan