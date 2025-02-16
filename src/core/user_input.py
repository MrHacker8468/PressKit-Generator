import typer # type: ignore
from rich.console import Console

console = Console()

def get_user_input():
    """Collects user input for the press kit generation."""
    console.print("\n📝 [bold cyan]Step 1: Enter Press Kit Details[/bold cyan]\n")

    company_name = console.input("🏢 [bold yellow]Company Name:[/bold yellow] ")
    topic = console.input("📰 [bold yellow]Press Kit Topic:[/bold yellow] ")
    target_media = console.input("🎯 [bold yellow]Target Media (e.g., Tech News, Business Magazines):[/bold yellow] ")
    tone = console.input("🎭 [bold yellow]Tone (e.g., Professional, Engaging, Neutral):[/bold yellow] ")


    # Confirm details
    console.print(f"\n🔍 [bold yellow]Review Your Inputs:[/bold yellow]")
    console.print(f"   📌 Company Name: [green]{company_name}[/green]")
    console.print(f"   📌 Press Kit Topic: [green]{topic}[/green]")
    console.print(f"   📌 Target Media: [green]{target_media}[/green]")
    console.print(f"   📌 Tone: [green]{tone}[/green]")

    confirm = typer.confirm("\n✅ Confirm these details?")
    if not confirm:
        return get_user_input()  # Restart if user wants to change inputs

    return {
        "company_name": company_name,
        "topic": topic,
        "target_media": target_media,
        "tone": tone
    }
