import os
from google import genai
from dotenv import load_dotenv # type: ignore

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variable
API_KEY = os.getenv("GENAI_API_KEY")

client = genai.Client(api_key=API_KEY)

def ai_supplementary_data_generator(company_name, press_kit_topic, target_audience, tone):
    """
    Generates AI-based supplementary data for a press release using Gemini AI.
    
    Parameters:
        - company_name (str): Name of the company.
        - press_kit_topic (str): Focus topic for the press kit.
        - target_audience (str): Intended audience.
        - tone (str): Desired tone of the press release.

    Returns:
        - list: Two significant AI-generated supplementary data points.
    """
    prompt = (
        f"Generate two significant insights related to {company_name} and its industry. "
        f"The focus should be on '{press_kit_topic}', targeting {target_audience} with a {tone} tone. "
        f"Provide a concise bullet-point list. No need to include any additional information."
    )

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[prompt])        
        # Extract AI-generated text
        if response and response.candidates:
            content = response.candidates[0].content.parts[0].text  # Extract the content part
            insights = content.split("\n")  # Split text into separate lines

            # Clean and filter empty lines, return top 2 insights
            insights = [insight.strip() for insight in insights if insight.strip()]
            return insights[-2:]
        
        return ["No AI-generated data available.", "Please try again."]
    
    except Exception as e:
        return [f"⚠️ Error generating AI data: {str(e)}"]
