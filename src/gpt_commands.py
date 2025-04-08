import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_astrological_insight(birth_date: str, birth_time: str, place_of_birth: str, aspect: str) -> str:
    """
    Get astrological insights using OpenAI's API
    
    Args:
        birth_date (str): Formatted birth date (e.g., "April 15, 1990")
        birth_time (str): Formatted birth time (e.g., "14:30")
        place_of_birth (str): Place of birth (e.g., "Mumbai, India")
        aspect (str): Life aspect to analyze
        
    Returns:
        str: AI-generated astrological insight
    """
    prompt = f"""As an expert astrologer, provide insights about {aspect} for someone born on {birth_date} at {birth_time} in {place_of_birth}.
    Consider planetary positions, zodiac influences, and cosmic energies in your analysis.
    Take into account the geographical location and its astrological significance.
    Focus specifically on their {aspect} and provide meaningful, constructive guidance.
    Keep the response concise but insightful (100-150 words)."""
    
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert astrologer with deep knowledge of vedic and western astrology."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating insights: {str(e)}" 