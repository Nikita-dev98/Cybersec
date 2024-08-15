from cli import run_cli
from database import initialize_database

def main():
    initialize_database()
    run_cli()

if __name__ == "__main__":
    main()