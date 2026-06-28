from fastapi import FastAPI

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Python Basic",
        "author": "Le Minh Thu",
        "category": "programming",
        "year": 2022,
        "is_available": True
    },
    {
        "id": 2,
        "title": "Web API Design",
        "author": "Pham Lan Hong",
        "category": "web",
        "year": 2021,
        "is_available": False
    },
    {
        "id": 3,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "category": "software",
        "year": 2008,
        "is_available": True
    },
    {
        "id": 6,
        "title": "FastAPI Basic",
        "author": "Nguyen Van A",
        "category": "web",
        "year": 2023,
        "is_available": True
    }
]

@app.get("/books/statistics")
def total_book():
    total = 0
    available_books = 0
    borrowed_books = 0
    for i in books:
        if i["is_available"] == True:
            available_books += 1
        if i["is_available"] == False:
            borrowed_books += 1
    total = available_books + borrowed_books
    return {
        "total_books": total,
        "available_books": available_books,
        "borrowed_books": borrowed_books
        }
@app.get("/books/categories")
def get_categories():
    categories = []
    for book in books:
        if book["category"] not in categories:
            categories.append(book["category"])
    return {"categories": categories}
@app.get("/books/latest")
def get_latest_book():
    if not books:
        return {"message": "No books available"}
    last_book = books[0]
    for book in books:
        if book["year"] > last_book["year"]:
            last_book = book
    return last_book