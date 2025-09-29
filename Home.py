import streamlit as st

# Page configuration
st.set_page_config(
    page_title="World Cities Explorer",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main title
st.title("🌍 World Cities Explorer")

# Welcome text
st.write("""
Welcome to the World Cities Explorer application! 

This interactive app allows you to explore and analyze data about cities around the world. 
You can filter cities by population, capital status, and country to discover interesting 
patterns and insights about global urban centers.

## Features:
- 🗺️ Interactive world map visualization
- 📊 Population filtering and analysis
- 🏛️ Capital city exploration
- 🌐 Country-specific data filtering
- 📈 Population distribution charts

Get started by clicking the button below to access the main application!
""")

# Add some spacing
st.write("")
st.write("")

# Navigation section
st.subheader("🚀 Get Started")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("🗺️ Explore World Cities", type="primary", use_container_width=True):
        st.switch_page("pages/app.py")

# Additional information
st.write("")
st.write("")

with st.expander("ℹ️ About the Data"):
    st.write("""
    This application uses a comprehensive dataset of world cities including:
    - City names and geographic coordinates
    - Population data (in millions)
    - Capital city indicators
    - Country classifications
    - Geographic regions
    
    The data allows for dynamic filtering and visualization to help you discover 
    patterns in global urbanization and city distribution.
    """)

# Footer
st.write("")
st.write("")
st.markdown("---")
st.markdown("*Built with Streamlit* 🎈")