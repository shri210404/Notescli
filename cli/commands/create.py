
import click
import requests
from cli.commands.login import get_token

@click.command("create")
def create_note():
    """Create a new note."""
    click.echo("📓 Let's create a new note!")
    title = click.prompt("Enter the note title")
    content = click.prompt("Enter the note content")
    
    token = get_token()
    if not token:
        click.echo("❌ You are not logged in.")
        return
    
    response = requests.post(
        "http://13.71.28.224:5000/notes", 
        json={"title": title, "content": content},
        headers={"Authorization": f"Bearer {token}"},
    )
    
    if response.status_code == 201:
        click.echo(f"✅ Successfully created note with ID: {response.json()['id']}")
    else:
        click.echo("❌ Failed to create the note.")

import click
import requests
from cli.commands.login import get_token

@click.command("create")
def create_note():
    """Create a new note."""
    click.echo("📓 Let's create a new note!")
    title = click.prompt("Enter the note title")
    content = click.prompt("Enter the note content")
    
    token = get_token()
    if not token:
        click.echo("❌ You are not logged in.")
        return
    
    # Replace with your Azure VM's public IP
    response = requests.post(
        "http://13.71.28.224:5000/notes",  # Use your Azure VM's public IP here
        json={"title": title, "content": content},
        headers={"Authorization": f"Bearer {token}"},
    )
    
    if response.status_code == 201:
        click.echo(f"✅ Successfully created note with ID: {response.json()['id']}")
    else:
        click.echo("❌ Failed to create the note.")

