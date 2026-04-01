import sys
import os

# FIX PATH ISSUE
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from database.db_connection import get_connection

st.title("✈️ Flight Analysis Dashboard")

conn = get_connection()

# -----------------------------
# KPI 1: Total Bookings
# -----------------------------
total_query = "SELECT COUNT(*) FROM flights;"
total = pd.read_sql(total_query, conn).iloc[0,0]

# -----------------------------
# KPI 2: Avg Price
# -----------------------------
avg_query = "SELECT AVG(price) FROM flights;"
avg_price = pd.read_sql(avg_query, conn).iloc[0,0]

# -----------------------------
# Show KPIs
# -----------------------------
col1, col2 = st.columns(2)

col1.metric("Total Bookings", total)
col2.metric("Average Price", round(avg_price,2))

# -----------------------------
# Airline Analysis
# -----------------------------
query = """
SELECT airline, COUNT(*) AS total_flights
FROM flights
GROUP BY airline
ORDER BY total_flights DESC;
"""

df = pd.read_sql(query, conn)

st.subheader("Airline Performance")
st.bar_chart(df.set_index("airline"))