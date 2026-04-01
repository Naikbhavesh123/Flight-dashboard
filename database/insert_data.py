import pandas as pd
from db_connection import get_connection

# Load cleaned data
df = pd.read_csv("C:/Bhavesh/ALL Projects 2026/flight_project/data/cleaned_data.csv")

conn = get_connection()
cursor = conn.cursor()

for i, row in df.iterrows():
    cursor.execute("""
        INSERT INTO flights (
            airline, ch_code, num_code, source, destination,
            price, stop, journey_day, journey_month,
            dep_hour, arr_hour, duration_mins
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row['airline'],
        row['ch_code'],
        row['num_code'],
        row['source'],
        row['destination'],
        row['price'],
        row['stop'],
        row['journey_day'],
        row['journey_month'],
        row['dep_hour'],
        row['arr_hour'],
        row['duration_mins']
    ))

conn.commit()
cursor.close()
conn.close()

print("Data inserted successfully!")