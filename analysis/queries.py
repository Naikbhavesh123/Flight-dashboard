import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.db_connection import get_connection
import pandas as pd

conn = get_connection()

query = """
SELECT airline, COUNT(*) AS total_flights
FROM flights
GROUP BY airline
ORDER BY total_flights DESC;
"""

df = pd.read_sql(query, conn)

print(df.head())