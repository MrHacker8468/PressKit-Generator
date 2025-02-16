from rich.console import Console
import typer  # type: ignore
from core.ai_generator import ai_supplementary_data_generator

console = Console()

def select_supplementary_data(user_data):
    """📂 Asks the user whether they want to provide supplementary data manually or generate it using AI."""
    
    console.print("\n📂 [bold cyan]Step 2: Supplementary Data Selection[/bold cyan] 🎯\n")
    choice = typer.prompt("🤖 Would you like to provide supplementary data manually or generate it using AI? (manual/ai)").strip().lower()

    if choice == "ai":
        console.print("\n🤖 [bold green]Generating AI-based supplementary data...[/bold green]")
        
        ai_generated_data = ai_supplementary_data_generator(
            user_data["company_name"],
            user_data["topic"],
            user_data["target_media"],
            user_data["tone"]
        )
        
        console.print("\n🔹 [bold blue]AI-Generated Supplementary Data:[/bold blue]")
        for idx, item in enumerate(ai_generated_data, start=1):
            console.print(f"   🎯 [bold yellow][{idx}][/bold yellow] {item}")
        
        # Ask if the AI-generated content is satisfactory
        satisfied = typer.prompt("✅ Are you satisfied with the AI-generated supplementary data? (yes/no)").strip().lower()
        
        if satisfied == "no":
            console.print("\n✍️ [bold magenta]Please enter additional supplementary data manually.[/bold magenta]")
            additional_data = []
            
            while True:
                entry = typer.prompt("➕ Enter an additional data point (or type 'exit' to finish)").strip()
                if entry == "exit":
                    break  # ✅ Breaks the loop when Enter is pressed
                additional_data.append(entry)

            ai_generated_data.extend(additional_data)  # ✅ Appends new data to AI-generated data
        
        # Print the final updated data
        console.print("\n✅ [bold green]Final Supplementary Data:[/bold green]")
        for idx, item in enumerate(ai_generated_data, start=1):
            console.print(f"   🎯 [bold yellow][{idx}][/bold yellow] {item}")
            
        # Ask for confirmation
        confirm = typer.prompt("✅ Are you satisfied with the AI + manually entered data? (yes/no)").strip().lower()
        if confirm == "no":
            return select_supplementary_data(user_data)  # ✅ Restart function if not satisfied
        
        return ai_generated_data  # ✅ Returns final list

    elif choice == "manual":
        console.print("\n✍️ [bold magenta]Please enter your supplementary data manually.[/bold magenta]")
        manual_data = []
        
        while True:
            entry = typer.prompt("📝 Enter a supplementary data point (or type 'exit' to finish)").strip()
            if entry == "exit":
                break  # ✅ Breaks the loop when Enter is pressed
            manual_data.append(entry)
        
        # Print the final manually entered data
        console.print("\n✅ [bold green]Final Manually Entered Supplementary Data:[/bold green]")
        for idx, item in enumerate(manual_data, start=1):
            console.print(f"   ✏️ [bold yellow][{idx}][/bold yellow] {item}")

        # Ask for confirmation
        confirm = typer.prompt("✅ Are you satisfied with the manually entered data? (yes/no)").strip().lower()
        if confirm == "no":
            return select_supplementary_data(user_data)  # ✅ Restart function if not satisfied
        
        return manual_data  # ✅ Returns final manual data

    else:
        console.print("\n❌ [bold red]Invalid choice! Please enter 'manual' or 'ai'.[/bold red]")
        return select_supplementary_data(user_data)  # ✅ Restart function if input is invalid
