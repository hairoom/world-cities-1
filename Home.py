import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="World Cities Dashboard",
    page_icon="🌍",
    layout="wide"
)

# Main title
st.title("🌍 World Cities Dashboard")

# Welcome text
st.markdown("""
## Welcome to the World Cities Explorer!

This interactive dashboard allows you to explore world cities data with various filters and visualizations.

### Features:
- 🗺️ Interactive map visualization
- 📊 Population analysis
- 🏛️ Capital city filtering
- 🌐 Country-specific views
- 📈 Statistical charts

Get started by clicking the button below to explore the world cities data!
""")

# Add some spacing
st.markdown("---")

# Navigation section
st.markdown("### 🚀 Ready to explore?")

# Button to navigate to the app
if st.button("🌟 Launch World Cities Explorer", type="primary", use_container_width=True):
    st.switch_page("pages/app.py")

# Additional information
st.markdown("---")
st.markdown("""
### About this app
This Streamlit multipage application provides an interactive way to explore world cities data, 
including population statistics, geographical distribution, and capital city information.
""")