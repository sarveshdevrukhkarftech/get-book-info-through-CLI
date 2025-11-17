import requests
import click


@click.command()
@click.option("--search", default="", help="Search anything about the book!")
# Command function search any query about the book.
def search_book(search):
    # Used context managers.
    with requests.Session() as session:
        base_URL = f"https://openlibrary.org/search.json?"
        params = {"q": {search}}
        response = requests.get(base_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        docs = data.get(
            "docs"
        )  # This List contains the Dictionaries of Book information.

        click.echo("Here is your 10 search query result.\n\n")  # Heading

        for i in range(10):
            click.echo(f"\n=== BOOK INFORMATION {i+1} ===")
            click.echo(f"Book Title: {docs[i]["title"]}")
            click.echo(f"Author Name: {",".join(docs[i]["author_name"])}")
            click.echo(f"Published Year: {docs[i]["first_publish_year"]}")
            click.echo(f"========== | ==========\n")

    else:
        click.echo(f"Something Went Wrong: {response.status_code}")


if __name__ == "__main__":
    search_book()
