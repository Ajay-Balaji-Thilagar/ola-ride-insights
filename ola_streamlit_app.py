import streamlit as st
import sqlite3
import pandas as pd

# Set page configuration with OLA theme
st.set_page_config(
    page_title="OLA Ride Insights",
    layout="wide",
    page_icon="🚗",
    menu_items={
        'Get Help': None,
        'Report a Bug': None,
        'About': "OLA Ride Insights Dashboard by Ajay"
    }
)

# Apply OLA-themed CSS
st.markdown("""
    <style>
    /* Main page background */
    .stApp {
        background-color: #FFFFFF;
    }
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #008040;
        opacity: 0.85;
    }
    /* Fix sidebar title */
    .css-1d391kg h1, [data-testid="stSidebar"] h1 {
        color: #FFFFFF !important;
        font-family: Arial, sans-serif;
    }
    /* Fix selectbox label and options */
    .stSelectbox label {
        color: #FFFFFF !important;
        font-family: Arial, sans-serif;
    }
    .stSelectbox div[data-baseweb="select"] > div {
        color: #000000 !important;
        background-color: #FFFFFF;
        border: 1px solid #D3D3D3;
        border-radius: 5px;
        font-family: Arial, sans-serif;
    }
    .stSelectbox div[role="option"] {
        color: #000000 !important;
        background-color: #FFFFFF;
    }
    /* Title and text */
    h1 {
        color: #000000 !important;
        font-family: Arial Black, sans-serif;
        font-size: 28px;
    }
    .stMarkdown, .stDataFrame {
        font-family: Arial, sans-serif;
        color: #000000;
    }
    /* Button styling */
    .stButton>button {
        background-color: #00CC66;
        color: #FFFFFF;
        border: 1px solid #D3D3D3;
        border-radius: 5px;
    }
    /* Table borders */
    .stDataFrame {
        border: 1px solid #D3D3D3;
    }
    </style>
""", unsafe_allow_html=True)

# Title and header
st.title("🚗 OLA Ride Insights Dashboard")
st.markdown("**Interactive analytics for OLA ride-sharing data**", unsafe_allow_html=True)

# Connect to SQLite database
try:
    conn = sqlite3.connect('ola_database.db')
except Exception as e:
    st.error(f"Database connection failed: {e}")
    st.stop()

# Read SQL queries from file
try:
    with open('ola_queries.sql', 'r') as file:
        queries = file.read().split(';')
        queries = [q.strip() for q in queries if q.strip()]  # Remove empty queries
except Exception as e:
    st.error(f"Failed to read queries: {e}")
    st.stop()

# Sidebar for navigation
st.sidebar.markdown("<h1 style='color: #FFFFFF;'>Select Insight</h1>", unsafe_allow_html=True)
insight = st.sidebar.selectbox(
    "Choose an insight:",
    [
        "1. Successful Bookings",
        "2. Avg Ride Distance by Vehicle",
        "3. Cancelled Rides by Customers",
        "4. Top 5 Customers by Rides",
        "5. Cancelled Rides Reasons",
        "6. Prime Sedan Driver Ratings",
        "7. UPI Payment Rides",
        "8. Avg Customer Rating by Vehicle",
        "9. Total Booking Value (Success)",
        "10. Incomplete Rides with Reasons"
    ],
    key="insight_select"
)

# Display selected query result
query_index = int(insight.split('.')[0]) - 1
if query_index < len(queries):
    query = queries[query_index]
    try:
        df = pd.read_sql_query(query, conn)
        st.markdown(f"**Query {query_index + 1}: {insight}**", unsafe_allow_html=True)
        st.dataframe(df, use_container_width=True)
        st.markdown("### OLA Power BI Dashboard", unsafe_allow_html=True)
        st.image('d1.png', caption='Dashboard Image 1', use_column_width=True)
        st.image('d2.png', caption='Dashboard Image 2', use_column_width=True)
        st.image('d3.png', caption='Dashboard Image 3', use_column_width=True)
    except Exception as e:
        st.error(f"Query execution failed: {e}")
else:
    st.error("Invalid query selection.")

# Close database connection
conn.close()