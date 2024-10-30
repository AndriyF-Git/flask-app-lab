from flask import Blueprint
import click

cli_bp = Blueprint("cli", __name__)

# Додаємо команду за допомогою Click
@cli_bp.cli.command("hello")
@click.argument("name")
def hello(name):
    """Привітати користувача по імені"""
    click.echo(f"Hello, {name}!")
    print("Hello server")