import streamlit as st
import pandas as pd

st.set_page_config(page_title="Budget Dashboard", page_icon="📊", layout="wide")

st.title("📊 Indian Budget Dashboard (2014–2025)")
st.write("Dataset is automatically loaded from the repository.")

# Load CSV directly from GitHub repo folder
df = pd.read_csv("Department_Budget_2014_to_2025.csv")

# Show dataset
st.subheader("📄 Dataset Preview")
st.dataframe(df)

# Select department
department_list = df["Department"].unique()
department = st.selectbox("Select Department", department_list)

# Extract data
row = df[df["Department"] == department].iloc[0]
years = df.columns[1:]
values = row[1:].astype(float)

# Data for charts
chart_df = pd.DataFrame({"Year": years, "Budget": values})

st.write("---")
st.subheader(f"📈 Budget Trend for {department}")
st.line_chart(chart_df, x="Year", y="Budget")

st.write("---")
st.subheader(f"📊 Budget Bar Chart for {department}")
st.bar_chart(chart_df, x="Year", y="Budget")
