import sys
import typer  # type: ignore
from rich.console import Console
from core.data_selection import select_supplementary_data
from core.content_generator import generate_press_kit
from core.quality_review import review_press_kit
from core.export import export_press_kit
from core.user_input import get_user_input  # Import user input function

console = Console()

def main():
    # Step 1: User Input
    user_data = get_user_input()

    # Step 2: Data Selection (AI or Manual)
    supplementary_data = select_supplementary_data(user_data)

    # Step 3: Generate Press Kit Content
    press_kit = generate_press_kit(user_data, supplementary_data)
    
    # Step 4: Review Press Kit Quality
    review_report = review_press_kit(press_kit)

    # Step 5: Ask for export format choice
    console.print("\n📤 [bold cyan]Step 5: Choose Export Format[/bold cyan]")
    format_choice = console.input("[bold green]Please select the export format (pdf/docx):[/bold green] ").strip().lower()

    if format_choice not in ["pdf", "docx"]:
        console.print("\n❌ [bold red]Invalid format choice! Please select either 'pdf' or 'docx'.[/bold red]")
        sys.exit(1)

    # Step 6: Export Press Kit to selected format
    export_press_kit(press_kit, format_choice)

if __name__ == "__main__":
    main()
