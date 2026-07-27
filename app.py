from datetime import datetime
import os
from pathlib import Path

import joblib
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Mining Process Quality Prediction",
    page_icon="⛏️",
    layout="wide"
)

# ---------------------------------------------------
# Paths
# ---------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "models" / "mining_model.pkl"

# ---------------------------------------------------
# Load Model
# ---------------------------------------------------

model = joblib.load(MODEL_PATH)

MODEL_R2 = 0.8981
MODEL_MAE = 0.0834
MODEL_NAME = "Decision Tree Regressor"

# ---------------------------------------------------
# Title
# ---------------------------------------------------

st.markdown("""
# ⛏️ Mining Process Quality Prediction

### AI-Based Flotation Process Monitoring Dashboard
""")

st.caption("Predict the percentage of Silica Concentrate using Machine Learning")

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------


IMAGE_PATH = BASE_DIR / "images" / "mining.png"

if IMAGE_PATH.exists():
    st.sidebar.image(str(IMAGE_PATH), width=80)

st.sidebar.title("Project Information")

st.sidebar.success("✅ Model Loaded")

st.sidebar.markdown("""
### 🤖 Algorithm
Decision Tree Regressor

### 🎯 Target
% Silica Concentrate

### 📊 Dataset
Mining Process Flotation Plant

### 👨‍💻 Developer
DD
""")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🤖 Model", MODEL_NAME)

with col2:
    st.metric("📊 R² Score", f"{MODEL_R2:.4f}")

with col3:
    st.metric("📉 MAE", f"{MODEL_MAE:.2f}")

with col4:
    st.metric("✅ Status", "Ready")

st.markdown("---")
st.header("⚙️ Enter Mining Process Parameters")

# ---------------- Feed Parameters ----------------
with st.expander("⛏️ Feed Parameters", expanded=True):

    col1, col2 = st.columns(2)

    with col1:
        iron_feed = st.number_input("% Iron Feed", value=60.0)
        silica_feed = st.number_input("% Silica Feed", value=15.0)

    with col2:
        ore_pulp_flow = st.number_input("Ore Pulp Flow", value=400.0)
        ore_pulp_density = st.number_input("Ore Pulp Density", value=1.7)

# ---------------- Chemical Parameters ----------------
with st.expander("🧪 Chemical Parameters"):

    col1, col2 = st.columns(2)

    with col1:
        starch_flow = st.number_input("Starch Flow", value=3000.0)

    with col2:
        amina_flow = st.number_input("Amina Flow", value=10.0)
        ore_pulp_ph = st.number_input("Ore Pulp pH", value=10.0)

# ---------------- Air Flow ----------------
with st.expander("💨 Air Flow Parameters"):

    col1, col2 = st.columns(2)

    with col1:
        air1 = st.number_input("Column 01 Air Flow", value=250.0)
        air2 = st.number_input("Column 02 Air Flow", value=250.0)
        air3 = st.number_input("Column 03 Air Flow", value=250.0)
        air4 = st.number_input("Column 04 Air Flow", value=250.0)

    with col2:
        air5 = st.number_input("Column 05 Air Flow", value=250.0)
        air6 = st.number_input("Column 06 Air Flow", value=250.0)
        air7 = st.number_input("Column 07 Air Flow", value=250.0)

# ---------------- Column Levels ----------------
with st.expander("📏 Flotation Column Levels"):

    col1, col2 = st.columns(2)

    with col1:
        level1 = st.number_input("Column 01 Level", value=500.0)
        level2 = st.number_input("Column 02 Level", value=500.0)
        level3 = st.number_input("Column 03 Level", value=500.0)
        level4 = st.number_input("Column 04 Level", value=500.0)

    with col2:
        level5 = st.number_input("Column 05 Level", value=500.0)
        level6 = st.number_input("Column 06 Level", value=500.0)
        level7 = st.number_input("Column 07 Level", value=500.0)

# ---------------- Time ----------------
with st.expander("📅 Date & Time"):

    col1, col2 = st.columns(2)

    with col1:
        year = st.number_input("Year", value=2017)
        month = st.number_input("Month", value=3)

    with col2:
        day = st.number_input("Day", value=1)
        hour = st.number_input("Hour", value=0)

# ---------------- Predict Button ----------------
c1, c2, c3 = st.columns([1, 2, 1])

with c2:
    predict = st.button(
        "🚀 Predict Quality",
        use_container_width=True
    )

if predict:

    input_data = pd.DataFrame([{
        "% Iron Feed": iron_feed,
        "% Silica Feed": silica_feed,
        "Starch Flow": starch_flow,
        "Amina Flow": amina_flow,
        "Ore Pulp Flow": ore_pulp_flow,
        "Ore Pulp pH": ore_pulp_ph,
        "Ore Pulp Density": ore_pulp_density,

        "Flotation Column 01 Air Flow": air1,
        "Flotation Column 02 Air Flow": air2,
        "Flotation Column 03 Air Flow": air3,
        "Flotation Column 04 Air Flow": air4,
        "Flotation Column 05 Air Flow": air5,
        "Flotation Column 06 Air Flow": air6,
        "Flotation Column 07 Air Flow": air7,

        "Flotation Column 01 Level": level1,
        "Flotation Column 02 Level": level2,
        "Flotation Column 03 Level": level3,
        "Flotation Column 04 Level": level4,
        "Flotation Column 05 Level": level5,
        "Flotation Column 06 Level": level6,
        "Flotation Column 07 Level": level7,

        "Year": year,
        "Month": month,
        "Day": day,
        "Hour": hour
    }])

    with st.expander("📋 View Input Parameters"):
            st.dataframe(input_data, use_container_width=True)

    st.write("Columns sent to model:")
    st.write(input_data.columns.tolist())
    prediction = model.predict(input_data)[0]
    st.write("Input sent to model:")
    st.dataframe(input_data)

    st.write("Prediction:")
    st.write(prediction)

    st.markdown("---")

    st.markdown("## 📊 Prediction Result")

    st.metric(
    "Predicted Silica Concentrate",
    f"{prediction:.2f} %",
    delta=None
    )

    fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=prediction,
    number={"suffix": "%"},
    title={"text": "Silica Concentrate"},
    gauge={
        "axis": {"range": [0, 10]},
        "bar": {"color": "#1f77b4"},
        "steps": [
            {"range": [0, 2], "color": "#2ECC71"},
            {"range": [2, 4], "color": "#F1C40F"},
            {"range": [4, 10], "color": "#E74C3C"},
        ],
        "threshold": {
            "line": {"color": "red", "width": 4},
            "thickness": 0.75,
            "value": prediction
        }
    }
    ))

    st.plotly_chart(fig, use_container_width=True)

    if prediction < 2:
        st.success("🟢 Excellent Quality Concentrate")
        st.write("The predicted silica percentage is within the ideal operating range.")

    elif prediction < 4:
        st.info("🟡 Good Quality Concentrate")
        st.write("The process is performing well, but continuous monitoring is recommended.")

    else:
        st.warning("🔴 High Silica Concentrate")
        st.write("The silica percentage is above the desired level. Process adjustment is recommended.")

    st.caption(
    f"Prediction generated on: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
    )
    
st.markdown("---")

with st.expander("ℹ️ About This Project"):

    st.write("""
This application predicts the percentage of silica concentrate in a mining flotation process using a Decision Tree Regression model.

### Technologies Used
- Python
- Streamlit
- Scikit-learn
- Pandas
- Plotly
- Power BI

### Objective
Improve mining process quality through AI-based prediction.
""")

st.markdown("---")

st.caption(
    "⛏️ Mining Process Quality Prediction | Internship Machine Learning Project | Developed by DD | 2026"
)