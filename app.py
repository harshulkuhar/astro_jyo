import streamlit as st
from src.gpt_commands import get_astrological_insight
from src.ui_components import (
    setup_page_config,
    display_header,
    get_birth_details,
    get_life_aspect,
    display_insights
)

def main():
    # Setup page configuration
    setup_page_config()
    
    # Display header
    display_header()
    
    # Get user inputs
    birth_date, birth_time = get_birth_details()
    selected_aspect = get_life_aspect()
    
    # Generate button
    if st.button("Get Astrological Insights", type="primary"):
        with st.spinner("Consulting the stars... 🌠"):
            # Get insights
            insights = get_astrological_insight(birth_date, birth_time, selected_aspect)
            
            # Display results
            display_insights(insights)

if __name__ == "__main__":
    main() 