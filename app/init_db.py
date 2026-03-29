from pathlib import Path
import duckdb

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "parkshare.duckdb"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

# First version of the database to test

conn = duckdb.connect(str(DB_PATH))

# Raw Table 
conn.execute(""" 
CREATE TABLE IF NOT EXISTS raw_data (
    city VARCHAR,
    population VARCHAR,
    density VARCHAR,
    car_ownership_rate VARCHAR,
    collective_housing_rate VARCHAR,
    latitude VARCHAR,
    longitude VARCHAR,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);         
""")

# Clean Table
conn.execute(""" 
CREATE TABLE IF NOT EXISTS clean_data (
    city VARCHAR,
    latitude FLOAT,
    longitude FLOAT,
    population INTEGER,
    density FLOAT,
    car_ownership_rate FLOAT,
    collective_housing_rate FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);         
""")

# KPI table
conn.execute(""" 
CREATE TABLE IF NOT EXISTS kpi_scores (
    city VARCHAR,
    latitude FLOAT,
    longitude FLOAT,
    score FLOAT,
    population_score FLOAT,
    transport_score FLOAT,
    housing_score FLOAT,
    rank INTEGER,
    zone_type VARCHAR,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);         
""")