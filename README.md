# Get Book Info Through CLI

A simple Python command-line tool that fetches book information from the [Open Library API](https://openlibrary.org/dev/docs/api/books).

This project is built to get familiar with:

- Git & GitHub
- Python virtual environments
- Writing CLI tools using **Click**
- Making API calls using **requests**
- Working with external APIs (Open Library)

---

## 🚀 Features

- Search for books directly from the terminal
  - Fetch and display:
    - Book Title
    - Author Name
    - First Published Year
  - Graceful error handling with status code
  - Clean and user-friendly CLI using **Click**

> More features will be added as the project evolves.

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Click**
- **Requests**
- **venv**
- **VS Code**

---

## 📦 Installation

Follow these steps to set up the project locally:

```bash
# Clone the repository
git clone https://github.com/sarveshdevrukhkarftech/get-book-info-through-CLI.git
cd get-book-info-through-CLI

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt
```
