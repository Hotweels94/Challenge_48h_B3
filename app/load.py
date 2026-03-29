from pathlib import Path
import duckdb
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "parkshare.duckdb"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

conn = duckdb.connect(str(DB_PATH))

df = pd.read_csv("data.csv")

conn.register("df_view", df)

conn.execute("""
INSERT INTO kpi_scores
SELECT 
    city,
    lat,
    lon,
    score,
    population / MAX(population) OVER (),
    car_ownership_rate / MAX(car_ownership_rate) OVER (),
    collective_housing_rate / MAX(collective_housing_rate) OVER (),
    ROW_NUMBER() OVER (ORDER BY score DESC),
    CASE 
        WHEN score > 0.75 THEN 'HIGH'
        WHEN score > 0.6 THEN 'MEDIUM'
        ELSE 'LOW'
    END,
    CURRENT_TIMESTAMP
FROM df_view
""")