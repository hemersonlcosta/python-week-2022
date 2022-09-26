from typing import List
import typer
from beerlog.core import add_beer_to_database, get_beers_from_database
from typing import Optional
from rich.table import Table
from rich.console import Console


main = typer.Typer(help="Beer Management")
console = Console()

@main.command("add")
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    if add_beer_to_database(name, style, flavor, image, cost):
        print("Beer added to database")


@main.command("list")
def list_beer(style: Optional[str] = None):
    beers = get_beers_from_database()
    table = Table(title="Beerlog")
    headers = ["id", "name", "style", "rate", "date"]
    for header in headers:
        table.add_column(header, style="magenta")
    for beer in beers:
        values = [str(getattr(beer, header)) for header in headers]
        table.add_row(*values)
    console.print(table)
