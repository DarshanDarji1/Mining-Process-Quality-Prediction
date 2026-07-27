# ⛏️ Mining Process Quality Prediction

## 📌 Project Overview

Mining Process Quality Prediction is a Machine Learning project developed to predict the percentage of silica concentrate produced during the flotation process in a mining plant.

The project analyzes operational parameters such as iron feed, silica feed, air flow, flotation column levels, ore pulp properties, and chemical flow to estimate the final silica concentration. A Random Forest Regression model is used to provide accurate predictions, while Streamlit offers an interactive web application for users and Power BI provides business-oriented dashboard visualizations.

---

## 🎯 Project Objectives

- Predict the percentage of silica concentrate.
- Improve mining process quality using Machine Learning.
- Reduce manual analysis of flotation parameters.
- Provide an easy-to-use prediction interface.
- Visualize operational insights using Power BI dashboards.

---

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Machine Learning:** Scikit-learn
- **Data Processing:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Plotly
- **Web Application:** Streamlit
- **Business Intelligence:** Power BI
- **Model Serialization:** Joblib

---

## 📂 Dataset

**Dataset Name:** Mining Process Flotation Plant Database

The dataset contains operational data collected from a mining flotation plant, including:

- % Iron Feed
- % Silica Feed
- Starch Flow
- Amina Flow
- Ore Pulp Flow
- Ore Pulp pH
- Ore Pulp Density
- Flotation Column Air Flow
- Flotation Column Levels
- Date & Time Features

**Target Variable:**

- **% Silica Concentrate**

---

## 📁 Project Structure

```text
Mining_Process_Quality_Prediction/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
├── dashboard/
├── images/
├── models/
├── outputs/
├── reports/
└── src/
```

---

## 🔄 Machine Learning Workflow

The project follows a complete Machine Learning pipeline:

1. **Data Collection**
   - Imported the Mining Process Flotation Plant dataset.

2. **Data Preprocessing**
   - Cleaned missing and invalid values.
   - Converted the date column into Year, Month, Day, and Hour.
   - Prepared the dataset for model training.

3. **Exploratory Data Analysis (EDA)**
   - Analyzed feature distributions.
   - Generated correlation heatmaps.
   - Identified relationships between process parameters and silica concentrate.

4. **Model Training**
   - Trained multiple regression models.
   - Compared their performance.
   - Selected the Random Forest Regressor as the final model.

5. **Model Evaluation**
   - Evaluated the model using standard regression metrics.
   - Saved the trained model using Joblib.

6. **Deployment**
   - Built an interactive Streamlit web application.
   - Designed a Power BI dashboard for business insights.

---

## 🤖 Machine Learning Model

**Selected Algorithm**

- Random Forest Regressor

### Model Performance

| Metric | Value |
|---------|-------|
| R² Score | 0.9953 |
| Mean Absolute Error (MAE) | 0.15 |

The Random Forest model achieved excellent prediction accuracy on the processed mining dataset and was selected as the final model for deployment.

---

## 🚀 Streamlit Application Features

The Streamlit application provides:

- Interactive input form
- Prediction of silica concentrate percentage
- Quality status indicator
- Organized parameter sections
- Project information sidebar
- Responsive dashboard layout

---

## 📊 Power BI Dashboard

The Power BI dashboard includes:

- KPI Cards
- Interactive Filters
- Process Monitoring Visualizations
- Trend Analysis
- Operational Dashboard for Mining Process

---

## 📸 Project Screenshots

### Streamlit Application

> Add a screenshot of the Streamlit prediction dashboard here.

### Power BI Dashboard

> Add a screenshot of the Power BI dashboard here.

---

## 🔮 Future Enhancements

Possible improvements for this project include:

- Integrating real-time sensor data from the mining process.
- Deploying the application on a cloud platform.
- Adding support for multiple machine learning models.
- Implementing automatic model retraining with new data.
- Enhancing the dashboard with advanced analytics and reporting.

---

## 👨‍💻 Author

**Developer:** DD

**Project:** Mining Process Quality Prediction

**Internship Project – 2026**

---

## 📜 License

This project was developed for educational and internship purposes.

---

## 🙏 Acknowledgements

Special thanks to:

- Internship Organization
- Scikit-learn Documentation
- Streamlit Documentation
- Microsoft Power BI
- Open-source Python Community