import streamlit as st

st.set_page_config(page_title="Data Science Portfolio", layout="wide")

# Apply global style
with open("styles.css") as f:
    css = f.read()

# Hero/Intro

st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# About section
st.html("<h1> About Me</h1>")
st.html("I am passionate about <b>data-driven solutions</b> and modern software development. With a strong background "
        "in <b>data science, analytics, and programming</b>, I build tools and visualizations that make complex "
        "problems simple."
        "<br/>"
        "- 💡 <b>Skills:</b> Python, Pandas, scikit-learn, Streamlit, Data Visualization, SQL "
        "- 🛠️ <b>Technologies:</b> Jupyter, Git, REST APIs "
        "- 🗂️ </b>Interests:</b> Machine Learning, Automation, Dashboards, Open Source")

# Projects preview (replace/add as you go)
st.markdown("---")
st.markdown("### Featured Projects")
col1, col2 = st.columns(2)
with col1:
    st.html("<b>Project 1:</b> Exploratory Data Analysis App <i>(Coming Soon)</i>")
    st.html("Interactive dashboard for rapid EDA on CSV datasets.")
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
