import streamlit as st
import pandas as pd
import plotly.express as px

# App Title
st.title("College Advisor Pro")
st.write("Welcome to the College Advisor App!")

# Sample Data
st.header("Sample Data Visualization")
data = {
    "Majors": ["Engineering", "Business", "Arts", "Sciences"],
    "Students": [120, 150, 90, 100]
}
df = pd.DataFrame(data)

# Display DataFrame
st.write("Here is a sample dataset:")
st.dataframe(df)

# Plotly Bar Chart
st.write("Here is a bar chart of students by major:")
fig = px.bar(df, x="Majors", y="Students", title="Students by Major")
st.plotly_chart(fig)
