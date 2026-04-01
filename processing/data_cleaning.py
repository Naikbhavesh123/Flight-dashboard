import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("C:/Bhavesh/ALL Projects 2026/flight_project/data/raw_data.csv", sep="\t")

# Clean column names
df.columns = df.columns.str.strip().str.replace(" ", "_").str.lower()

df['price'] = df['price'].str.replace(',', '').astype(float)

# PRINT COLUMNS FIRST
print("Columns in dataset:")
print(df.columns) 



print("Initial Shape:", df.shape)
print(df.head())

# -----------------------------
# 1. Convert Date
# -----------------------------
df['date'] = pd.to_datetime(df['date'], dayfirst=True, errors='coerce')

df['journey_day'] = df['date'].dt.day
df['journey_month'] = df['date'].dt.month

# -----------------------------
# 2. Convert Time Columns
# -----------------------------
df['dep_time'] = pd.to_datetime(df['dep_time'], format='%H:%M', errors='coerce')
df['arr_time'] = pd.to_datetime(df['arr_time'], format='%H:%M', errors='coerce')

df['dep_hour'] = df['dep_time'].dt.hour
df['arr_hour'] = df['arr_time'].dt.hour

# -----------------------------
# 3. Duration Handling
# -----------------------------
def convert_duration(x):
    try:
        hours = 0
        minutes = 0
        
        if 'h' in x:
            hours = int(x.split('h')[0])
        if 'm' in x:
            minutes = int(x.split('h')[-1].replace('m', '').strip())
            
        return hours * 60 + minutes
    except:
        return None

df['duration_mins'] = df['time_taken'].apply(convert_duration)

# -----------------------------
# 4. Stops Handling
# -----------------------------
df['stop'] = df['stop'].replace('non-stop', '0')
df['stop'] = df['stop'].str.extract('(\d+)')
df['stop'] = pd.to_numeric(df['stop'], errors='coerce')
df['stop'] = df['stop'].fillna(0)

# -----------------------------
# 5. Rename Columns (IMPORTANT)
# -----------------------------
df.rename(columns={
    'from': 'source',
    'to': 'destination'
}, inplace=True)

# -----------------------------
# 6. Drop unnecessary columns
# -----------------------------
df.drop(columns=['date', 'dep_time', 'arr_time'], inplace=True)

# -----------------------------
# 7. Save Cleaned Data
# -----------------------------
df.to_csv("C:/Bhavesh/ALL Projects 2026/flight_project/data/cleaned_data.csv", index=False)

print(" Data cleaned and saved!")
print(df.head())

exit()