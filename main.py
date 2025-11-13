import requests
import click


@click.command()
@click.option("--search", default="", help="Search anything about the book!")
# Command function search any query about the book.
def search_book(search):
    # Used context managers.
    with requests.Session() as session:
        base_URL = f"https://openlibrary.org/search.json?q={search}"
        response = requests.get(base_URL)

    if response.status_code == 200:
        data = response.json()
        docs = data.get("docs")

        for obj in docs:
            click.echo(f"Book Title: {obj["title"]}\n")

    else:
        click.echo(f"Something Went Wrong: {response.status_code}")


if __name__ == "__main__":
    data = search_book()
