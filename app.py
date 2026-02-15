import streamlit as st
import pandas as pd
import requests
import json
from datetime import datetime
import time
import random

st.set_page_config(page_title="EcoTrack API Portal", layout="wide", page_icon="🏗️")

st.markdown("""
    <style>
    .main { background-color: #f0f4f8; color: #2d3748; }
    .stMetric { background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

if 'api_calls' not in st.session_state:
    st.session_state.api_calls = pd.DataFrame(columns=['Timestamp', 'Endpoint', 'Status', 'CO2e_Calculated'])

st.title("🏗️ EcoTrack Enterprise API | Sustainability Dashboard")
st.write("Live API Analytics and Carbon Calculation Monitor")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Active Endpoints", "6")
m2.metric("Avg Latency", "42ms")
m3.metric("Total CO2e Processed", "1,240 Tons")
m4.metric("API Status", "🟢 Healthy")

placeholder = st.empty()

for i in range(100):
    endpoints = ["/v1/calculate/logistics", "/v1/calculate/utility", "/v1/report/summary"]
    endpoint = random.choice(endpoints)
    co2_val = round(random.uniform(5.5, 85.2), 2)
    
    new_call = {
        'Timestamp': datetime.now().strftime("%H:%M:%S.%f")[:-3],
        'Endpoint': endpoint,
        'Status': "200 OK",
        'CO2e_Calculated': f"{co2_val} kg"
    }
    
    st.session_state.api_calls = pd.concat([pd.DataFrame([new_call]), st.session_state.api_calls]).head(15)
    
    with placeholder.container():
        st.subheader("Recent API Transactions")
        st.table(st.session_state.api_calls)
        
        st.subheader("Emission Ingestion Profile")
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['Logistics', 'Energy', 'Waste'])
        st.area_chart(chart_data)

    time.sleep(1.8)
