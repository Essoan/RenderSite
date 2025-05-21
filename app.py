import streamlit as st

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.set_page_config(page_title="Programming and Data Science Portfolio", layout="wide")

# Hero Section
st.markdown("""
<style>
.hero {
    background-color: #1e8346;
    color: white;
    border-radius: 16px;
    padding: 3rem 2rem;
    margin-bottom: 2rem;
}
h1.hero-title {
    font-size: 3rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1 class="hero-title">👋 Welcome to Espen Andresen’s Portfolio</h1>
    <p>Data Science • AI • IoT • Electronics</p>
    <p><b>Clarity, Control, and Calm in One Space.</b></p>
</div>
""", unsafe_allow_html=True)

# Feature Columns
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("### 🧠 Data Science")
    st.write("EDA, dashboards, and analytics.")
    st.button("View Projects", key="ds")
with col2:
    st.markdown("### 🤖 AI Demos")
    st.write("Machine learning and AI applications.")
    st.button("View AI", key="ai")
with col3:
    st.markdown("### 🌡️ Sensor Data")
    st.write("Real-time and simulated IoT data.")
    st.button("View Sensor", key="sensor")

st.markdown("---")
st.write("👇 Scroll for project highlights, testimonials, and more!")

# Add images/logos using st.image if needed
