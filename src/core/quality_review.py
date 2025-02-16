import os
import typer  # type: ignore
from google import genai
from dotenv import load_dotenv # type: ignore
from rich.console import Console

# Load API Key
load_dotenv()
API_KEY = os.getenv("GENAI_API_KEY")

# Initialize Google Gemini AI Client
client = genai.Client(api_key=API_KEY)
console = Console()

def generate_ai_ratings(press_kit):
    """Uses AI to generate ratings for different parameters."""
    prompt = (
        f"Evaluate the following press kit on a scale of 1 to 10 for each parameter:\n"
        f"- Content Consistency\n"
        f"- Writing Style & Tone\n"
        f"- Layout & Structure\n"
        f"- SEO Optimization\n\n"
        f"Provide only the ratings in this format:\n"
        f"Content Consistency: X/10\n"
        f"Writing Style & Tone: X/10\n"
        f"Layout & Structure: X/10\n"
        f"SEO Optimization: X/10\n\n"
        f"Press Kit:\n{press_kit}"
    )

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[prompt]
    )

    return response.text if response else "❌ AI rating generation failed."

def generate_ai_feedback(press_kit):
    """Uses AI to analyze the press kit and generate concise feedback."""
    prompt = (
        f"Review the following press kit for:\n"
        f"- Content Consistency\n"
        f"- Writing Style & Tone\n"
        f"- Layout & Structure\n"
        f"- SEO Optimization\n\n"
        f"Provide ONLY 3 short, clear improvement suggestions as bullet points. "
        f"Keep it under 50 words total for each category.\n\n"
        f"Press Kit:\n{press_kit}"
    )

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[prompt]
    )

    return response.text if response else "❌ AI feedback generation failed."


def review_press_kit(press_kit: str):
    """AI-Powered Quality Review for the Press Kit."""
    console.print("\n🔍 [bold cyan]Step 4: Quality Review AI Agent[/bold cyan]\n")

    # Generate AI-based ratings
    ai_ratings = generate_ai_ratings(press_kit)

    # Generate AI-based review feedback
    ai_feedback = generate_ai_feedback(press_kit)

    # Review Report
    review_report = f"""
    [bold]📊 Quality Review Report[/bold]
    ------------------------------------
    {ai_ratings}

    [bold]📋 AI Feedback:[/bold]
    {ai_feedback}
    """
    
    console.print(review_report)

    # Ask User for Approval or Modification
    modify = typer.confirm("\n🔄 Do you want to make improvements based on the feedback?")
    if modify:
        console.print("\n✍️ [bold yellow]Please modify the press kit content as needed and rerun the review.[/bold yellow]")
        return None  # User will modify and re-run the review

    console.print("\n✅ [bold green]Press Kit Approved! Ready for Export.[/bold green]")
    return review_report  # Return final review report
