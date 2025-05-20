import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate some generic data
np.random.seed(42)
dates = pd.date_range("2024-01-01", periods=30)
data = pd.DataFrame({
    "Date": dates,
    "Sales": np.random.randint(100, 500, size=30),
    "Customers": np.random.randint(20, 80, size=30),
    "Conversion Rate (%)": np.round(np.random.uniform(5, 20, size=30), 2)
})

# Dashboard title
st.title("📊 Quick Data Science Dashboard Demo")
st.subheader("Generic business data – sales, customers, and conversion rate")

# Show data table
if st.checkbox("Show raw data"):
    st.write(data)

# Metrics row
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"{data['Sales'].sum():,}")
col2.metric("Avg Customers/Day", f"{data['Customers'].mean():.1f}")
col3.metric("Avg Conversion Rate", f"{data['Conversion Rate (%)'].mean():.2f}%")

st.markdown("---")

# Sales chart
st.header("Sales Over Time")
fig, ax = plt.subplots()
ax.plot(data["Date"], data["Sales"], marker="o")
ax.set_xlabel("Date")
ax.set_ylabel("Sales")
ax.set_title("Daily Sales")
st.pyplot(fig)

# Customers bar chart
st.header("Customers Per Day")
fig2, ax2 = plt.subplots()
ax2.bar(data["Date"], data["Customers"], color="tab:orange")
ax2.set_xlabel("Date")
ax2.set_ylabel("Customers")
st.pyplot(fig2)

# Conversion Rate
st.header("Conversion Rate (%) Over Time")
fig3, ax3 = plt.subplots()
ax3.plot(data["Date"], data["Conversion Rate (%)"], color="tab:green")
ax3.set_xlabel("Date")
ax3.set_ylabel("Conversion Rate (%)")
st.pyplot(fig3)

st.markdown("---")
st.info("This dashboard is fully interactive. Add your own data or features!")