from models import *
from rich.console import Console
from rich.table import Table

class Connection():

    @staticmethod
    def new():
        pass

    @staticmethod
    def connect(host: str):
        pass

    @staticmethod
    def list():

        table = Table(title="Connections")

        table.add_column("Active"      , justify="center", style="green", no_wrap=True)
        table.add_column("Name"        , justify="center", style="green", no_wrap=True)
        table.add_column("Host"        , justify="center", style="green", no_wrap=True)
        table.add_column("Descriptions", justify="right" , style="green", no_wrap=True)
        table.add_column("Created"     , justify="center", style="green", no_wrap=True)

        contexts = Context().get_all()

        for context in contexts:
            table.add_row("🟢", context.name, context.host, context.description, context.created_on)
        
        console = Console()
        console.print(table)

    @staticmethod
    def remove():
        pass