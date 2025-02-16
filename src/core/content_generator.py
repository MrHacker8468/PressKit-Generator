import os
import typer  # type: ignore
from google import genai
from dotenv import load_dotenv # type: ignore
from rich.console import Console
from datetime import datetime
from typing import Optional, List

# Load API Key
load_dotenv()
API_KEY = os.getenv("GENAI_API_KEY")

# Initialize Google Gemini AI Client
client = genai.Client(api_key=API_KEY)
console = Console()

def generate_ai_content(prompt):
    """Generates AI-powered content using Gemini API."""
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[prompt]
    )
    return response.text if response else "❌ AI generation failed."

def confirm_or_regenerate(section_name, content, prompt):
    """Displays a section, asks for confirmation, and allows regeneration."""
    while True:
        console.print(f"\n[bold cyan]🔹 {section_name}:[/bold cyan]\n{content}\n")
        keep = typer.confirm(f"✅ Do you want to keep this {section_name}?")
        if keep:
            return content  # User confirmed, keep the content
        console.print(f"\n🔄 Regenerating {section_name}...\n")
        content = generate_ai_content(prompt)  # Regenerate AI content

def generate_press_kit(user_data: dict, supplementary_data: Optional[List[str]] = None):
    """Generates a complete AI-powered press kit with interactive confirmation."""
    
    console.print("\n📝 [bold cyan]Step 3: Generating Press Kit Content Using AI[/bold cyan]\n")

    company_name = user_data['company_name']
    press_kit_topic = user_data['topic']
    target_audience = user_data['target_media']
    tone = user_data['tone']

    # 🎯 AI-Powered Insights
    insights_prompt = (
        f"Generate two key insights about {company_name} and its industry. "
        f"Focus on '{press_kit_topic}', targeting {target_audience} with a {tone} tone. "
        f"Provide a bullet-point list."
    )
    insights = confirm_or_regenerate("Key Insights", generate_ai_content(insights_prompt), insights_prompt)

    # 📰 AI-Powered Press Release
    press_release_prompt = (
        f"Write a compelling press release for {company_name} announcing its latest innovation in {press_kit_topic}. "
        f"Ensure it's engaging and tailored to {target_audience}. Maintain a {tone} tone."
    )
    press_release = confirm_or_regenerate("Press Release", generate_ai_content(press_release_prompt), press_release_prompt)

    # 🗣️ AI-Powered PR Message
    pr_message_prompt = (
        f"Create a short, impactful PR message for {company_name} regarding {press_kit_topic}. "
        f"Keep it inspiring and relevant to {target_audience}."
    )
    pr_message = confirm_or_regenerate("PR Message", generate_ai_content(pr_message_prompt), pr_message_prompt)

    # 📩 AI-Powered Email Draft
    email_prompt = (
        f"Draft a professional outreach email for {company_name}, introducing its latest breakthrough in {press_kit_topic}. "
        f"Make it engaging, short, and persuasive for {target_audience}."
    )
    email_draft = confirm_or_regenerate("Email Draft", generate_ai_content(email_prompt), email_prompt)

    # 📊 Supplementary Data Handling
    supplementary_section = ""
    if supplementary_data:
        supplementary_section = "\n[bold]📎 Supplementary Information:[/bold]\n"
        for item in supplementary_data:
            supplementary_section += f"   - {item}\n"

    # 📅 Timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    closing_statement = f"\n[italic]Generated on {timestamp} using Google Gemini AI.[/italic]"

    # ✨ Final Press Kit Compilation
    press_kit = f"""
    [bold]📌 Key Insights:[/bold]
    {insights}

    [bold]📰 Press Release:[/bold]
    {press_release}

    [bold]🗣️ PR Message:[/bold]
    {pr_message}

    [bold]📩 Email Draft:[/bold]
    {email_draft}

    {supplementary_section}

    {closing_statement}
    """

    return press_kit
