import requests
import click

@click.command()
@click.option('--search', help='Search anything about the book!')

def get_Book_Info_CLI(search):
    # click.echo(f"Hello {search}!")
    base_URL = f"https://openlibrary.org/search.json?q={search}"
    response = requests.get(base_URL)

    if response.status_code == 200:
        data = response.json()

        book = data.get("docs", [])

        for books in book:
            print(f"{books[0]["author_name"][0]}") # Destructured the response and print the name of the author.
        else:
            print("Error:", response.status_code)

        # print(f"{book_data["docs"][0]["author_name"][0]}") # Destructured the response and print the name of the author.
    else:
        print(f"Failed to retrieve data with  {response.status_code}")

if __name__ == '__main__':
    get_Book_Info_CLI()



### Teesha's Code ###

# import requests
# import click
# # Base URL for Open Library search API

# base_url = "https://openlibrary.org/search.json"


# def get_book_info(name):

# # Send request to Open Library API with book title
# response = requests.get(base_url, params={"title": name})

# # Check if the request was successful
# if response.status_code == 200:
# book_data = response.json()
# books = book_data.get("docs", [])

# if not books:
# print("No books found!")
# return

# # Print info for the first few books

# for book in books[:5]: # limit to first 5 results
# title = book.get("title", "N/A")
# authors = book.get("author_name", ["N/A"])
# year = book.get("first_publish_year", "N/A")

# print(f"\nTitle: {title}")
# print(f"Author: {authors[0]}")
# print(f"Published Year: {year}")

# else:
# print("Failed to get book info. Error code:", response.status_code)


# Get book name from user

# book_name = input("Enter book name: ")
# get_book_info(book_name)
# @click.command()
# @click.argument('nameby')
# @click.option('--count', default=1, help='Number of times to greet.')
# def success(count,nameby):
# for _ in range(count):
# click.echo(f"The book name has been fetched successfully by {nameby}.")
# success()






# params = {"q": sear} # Query search. Overall you can search anything related to books.


# def getBookInfo():
#     response = requests.get(base_URL, params=params)

#     if response.status_code == 200:
#         book_data = response.json()
#         return book_data
#     else:
#         print(f"Failed to retrieve data with  {response.status_code}")

# # Function Calling.
# book_Info = getBookInfo()

# # If response information is present then.
# if book_Info:
#     print(f"{book_Info["docs"][0]["author_name"][0]}") # Destructured the response and print the name of the author.


#### Gauri's Code ####

# import requests
# import click

# @click.command()
# @click.argument("title")
# @click.option('--count', default=1, help="number of books")

# def title_search(title, count):
# """search book by its title."""

# URL = f"https://openlibrary.org/search.json?title={title}"
# response = requests.get(URL)

# if response.status_code == 200:
# data = response.json()
# book = data.get("docs", [])
# if not book:
# print("No books found")
# return

# for books in book[:count]:
# print("📘Title:", books.get("title"))
# print("Author Name:", books["author_name"][0])
# print("Author Key:", books["author_key"][0])
# print("📅first publish year:", books["first_publish_year"],"\n")
# click.echo(f"The book name has been fetched successfully by {title}")
# else:
# print("Error:", response.status_code)

# if name == "main":
# title_search()