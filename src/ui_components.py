import streamlit as st
from datetime import datetime

def setup_page_config():
    """Configure the Streamlit page settings"""
    st.set_page_config(
        page_title="Apna Jyotish - Personal Astrology Guide",
        page_icon="🌟"
    )

def display_header():
    """Display the application header"""
    st.title("🌟 Apna Jyotish")
    st.subheader("Your Personal Astrology Guide")

def get_birth_details():
    """
    Get birth date and time from user input
    
    Returns:
        tuple: (formatted_date, formatted_time)
    """
    col1, col2 = st.columns(2)

    with col1:
        birth_date = st.date_input("Date of Birth", min_value=datetime(1900, 1, 1))

    with col2:
        birth_time = st.time_input("Time of Birth")
        
    return (
        birth_date.strftime("%B %d, %Y"),
        birth_time.strftime("%H:%M")
    )

def get_life_aspect():
    """
    Get selected life aspect from user input
    
    Returns:
        str: Selected life aspect
    """
    aspects = [
        "Career & Professional Life",
        "Love & Relationships",
        "Health & Well-being",
        "Wealth & Finance",
        "Personal Growth",
        "Family Life",
        "Education & Learning",
        "Travel & Adventure"
    ]
    return st.selectbox("Choose an aspect of life", aspects)

def display_insights(insights: str):
    """
    Display the astrological insights in a formatted box
    
    Args:
        insights (str): The astrological reading to display
    """
    st.success("Your Personalized Astrological Reading")
    st.write("---")
    st.write(insights)
    st.write("---")
    st.caption("Note: This is an AI-generated astrological reading for entertainment purposes.") 