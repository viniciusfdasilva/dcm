import typer, sys
from cli import Cli, Interface

app = typer.Typer()

@app.command()
def new():
    
    is_ok = Cli.new_connection()

    if is_ok:

        new()

    else:
        pass
        #typer.


@app.command()
def connect(name: str):
    #if formal:
     #   print(f"Goodbye Ms. {name}. Have a good day.")
    #else:
    #        print(f"Bye {name}!")
    pass

if __name__ == "__main__":
    
    if len(sys.argv) > 1:

        app()
    else:
        Interface.banner()
        Interface.menu()