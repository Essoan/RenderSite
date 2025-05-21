import streamlit as st

st.set_page_config(page_title="Data Science Portfolio", layout="wide")

# Apply global style
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Hero/Intro
st.markdown("""
<div style='background: var(--primary); border-radius:18px; padding:2.5rem 2rem 2rem 2rem; margin-bottom:2rem; 
color:var(--box); box-shadow:0 4px 20px rgba(49,151,149,0.08);'>
    <h1 style='font-size:2.4rem; margin-bottom:0.6rem; font-family: var(--font-main);'>Espen Andresen</h1>
    <div style='font-size:1.15rem; font-family: var(--font-main);'>Data Science & Programming Portfolio</div>
    <div style='font-size:1rem; margin-top:0.7rem;'>Analytics · Machine Learning · Python · Visualization</div>
</div>
""", unsafe_allow_html=True)

# About section
st.markdown("### About Me")
st.markdown("""
I am passionate about **data-driven solutions** and modern software development.  
With a strong background in **data science, analytics, and programming**, I build tools and visualizations that make 
complex problems simple.

- 💡 **Skills:** Python, Pandas, scikit-learn, Streamlit, Data Visualization, SQL  
- 🛠️ **Technologies:** Jupyter, Git, REST APIs  
- 🗂️ **Interests:** Machine Learning, Automation, Dashboards, Open Source
""")

# Projects preview (replace/add as you go)
st.markdown("---")
st.markdown("### Featured Projects")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**Project 1:** Exploratory Data Analysis App *(Coming Soon)*")
    st.markdown("Interactive dashboard for rapid EDA on CSV datasets.")
with col2:
    st.markdown("**Project 2:** ML Model Playground *(Coming Soon)*")
    st.markdown("Play with machine learning models on your data.")

# Navigation buttons (add pages as you build)
st.markdown("---")
col3, col4 = st.columns(2)
with col3:
    st.button("Projects", use_container_width=True)
with col4:
    st.button("Contact", use_container_width=True)

st.markdown("""
<div style='text-align:center; color:var(--primary); font-size:1rem; margin-top:1.6rem;'>
    &copy; 2025 Espen Andresen — Built with Streamlit
</div>
""", unsafe_allow_html=True)
