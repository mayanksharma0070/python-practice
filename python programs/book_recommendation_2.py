# -------------------------------------------------------
# BOOK RECOMMENDATION SYSTEM (Full Upgrade - No Files)
# -------------------------------------------------------

# Initial Book Database (Dictionary of genres -> list of dictionaries)
books_db = {
    "Fiction": [
        {"title": "1984", "author": "George Orwell"},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    ],
    "Non-Fiction": [
        {"title": "Sapiens", "author": "Yuval Noah Harari"},
        {"title": "The Power of Habit", "author": "Charles Duhigg"},
        {"title": "Educated", "author": "Tara Westover"},
    ],
    "Mystery": [
        {"title": "Sherlock Holmes", "author": "Arthur Conan Doyle"},
        {"title": "Gone Girl", "author": "Gillian Flynn"},
        {"title": "The Girl with the Dragon Tattoo", "author": "Stieg Larsson"},
    ],
    "Thriller": [
        {"title": "The Da Vinci Code", "author": "Dan Brown"},
        {"title": "Shutter Island", "author": "Dennis Lehane"},
        {"title": "The Silence of the Lambs", "author": "Thomas Harris"},
    ],
    "Fantasy": [
        {"title": "The Hobbit", "author": "J.R.R. Tolkien"},
        {"title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling"},
        {"title": "The Name of the Wind", "author": "Patrick Rothfuss"},
    ],
    "Science Fiction": [
        {"title": "Dune", "author": "Frank Herbert"},
        {"title": "Ender's Game", "author": "Orson Scott Card"},
        {"title": "The Martian", "author": "Andy Weir"},
    ],
    "Philosophy": [
        {"title": "The Alchemist", "author": "Paulo Coelho"},
        {"title": "Meditations", "author": "Marcus Aurelius"},
        {"title": "Man's Search for Meaning", "author": "Viktor Frankl"},
    ],
    "Horror": [
        {"title": "It", "author": "Stephen King"},
        {"title": "The Haunting of Hill House", "author": "Shirley Jackson"},
        {"title": "Bird Box", "author": "Josh Malerman"},
    ],
    "Drama": [
        {"title": "The Merchant of Venice", "author": "William Shakespeare"},
        {"title": "Death of a Salesman", "author": "Arthur Miller"},
        {"title": "A Doll's House", "author": "Henrik Ibsen"},
    ]
}

# Recently viewed stack (Last 5 books)
recent_stack = []

# Wishlist: Set (no duplicates)
wishlist = set()


# -------------------- SHOW ALL GENRES --------------------

def show_genres():
    print("\n--- Available Genres ---")
    for i, genre in enumerate(books_db.keys(), 1):
        print(f"{i}. {genre}")
    print()


# -------------------- SHOW ALL BOOKS ---------------------

def show_all_books():
    print("\n--- All Books ---")
    for genre, book_list in books_db.items():
        print(f"\n[{genre}]")
        for b in book_list:
            print(f"- {b['title']} by {b['author']}")
    print()


# -------------------- GENRE SELECTION MENU ---------------

def select_genre():
    genre_list = list(books_db.keys())
    print("\n--- Select Genre ---")
    for i, g in enumerate(genre_list, 1):
        print(f"{i}. {g}")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(genre_list):
                return genre_list[choice - 1]
        except:
            pass
        print("Invalid choice! Try again.")


# -------------------- RECOMMEND BOOKS --------------------

def recommend_by_genre():
    print("\n--- Recommend Books by Genre ---")
    genre = select_genre()

    print(f"\nRecommended books in {genre}:")
    for b in books_db[genre]:
        print(f"- {b['title']} by {b['author']}")
        recent_stack.append(b)

    if len(recent_stack) > 5:
        recent_stack[:] = recent_stack[-5:]

    print()


# -------------------- SEARCH BOOKS ------------------------

def search_books():
    print("\n--- Search Books by Title ---")
    query = input("Enter book title: ").strip().lower()
    found = False

    for genre, book_list in books_db.items():
        for b in book_list:
            if query in b["title"].lower():
                print(f"- {b['title']} by {b['author']} ({genre})")
                recent_stack.append(b)
                found = True

    if not found:
        print("No matching books found.")

    if len(recent_stack) > 5:
        recent_stack[:] = recent_stack[-5:]

    print()


# -------------------- ADD NEW BOOK ------------------------

def add_book():
    print("\n--- Add New Book ---")
    title = input("Book Title: ").strip()
    author = input("Author Name: ").strip()

    print("Select Genre for New Book:")
    genre = select_genre()

    new_book = {"title": title, "author": author}
    books_db[genre].append(new_book)

    print("Book added successfully!\n")


# -------------------- UPDATE BOOK DETAILS --------------------

def update_book():
    print("\n--- Update an Existing Book ---")
    print("Select the genre of the book:")
    genre = select_genre()

    print(f"\nBooks in {genre}:")
    for i, b in enumerate(books_db[genre], 1):
        print(f"{i}. {b['title']} by {b['author']}")

    try:
        choice = int(input("Select book number to update: "))
        selected = books_db[genre][choice - 1]
    except:
        print("Invalid selection.\n")
        return

    new_title = input(f"New Title (press enter to keep '{selected['title']}'): ").strip()
    new_author = input(f"New Author (press enter to keep '{selected['author']}'): ").strip()

    if new_title:
        selected["title"] = new_title
    if new_author:
        selected["author"] = new_author

    print("Book details updated successfully!\n")


# -------------------- RECENTLY VIEWED ---------------------

def view_recent():
    print("\n--- Recently Viewed Books (Last 5) ---")
    if not recent_stack:
        print("No recent books.\n")
        return

    for b in recent_stack[-5:]:
        print(f"- {b['title']} by {b['author']}")
    print()


# -------------------- WISHLIST FUNCTIONS ----------------------------

def add_to_wishlist():
    book = input("Enter book title to add to wishlist: ").strip()
    wishlist.add(book)
    print("Added to wishlist!\n")


def view_wishlist():
    print("\n--- Wishlist ---")
    if not wishlist:
        print("Wishlist is empty.\n")
        return
    for b in wishlist:
        print("- " + b)
    print()


def move_from_wishlist_to_recent():
    if not wishlist:
        print("\nWishlist is empty.\n")
        return

    print("\n--- Move a Wishlist Book to Recent ---")
    wishlist_list = list(wishlist)

    for i, item in enumerate(wishlist_list, 1):
        print(f"{i}. {item}")

    try:
        choice = int(input("Select the book number: "))
        book_title = wishlist_list[choice - 1]
    except:
        print("Invalid choice.\n")
        return

    # Find book in database
    found_book = None
    for genre, blist in books_db.items():
        for b in blist:
            if b["title"].lower() == book_title.lower():
                found_book = b
                break

    if found_book:
        recent_stack.append(found_book)
        print(f"Moved '{book_title}' to recently viewed!\n")
    else:
        print("Book not found in database, but moved as title only.\n")
        recent_stack.append({"title": book_title, "author": "Unknown"})

    wishlist.remove(book_title)

    if len(recent_stack) > 5:
        recent_stack[:] = recent_stack[-5:]


# -------------------- MAIN MENU ---------------------------

def main():
    while True:
        print("\n========== BOOK RECOMMENDATION SYSTEM ==========")
        print("1. Show All Genres")
        print("2. Show All Books")
        print("3. Recommend Books by Genre")
        print("4. Search Books by Title")
        print("5. Add New Book")
        print("6. Update Book Details")
        print("7. View Recently Viewed Books")
        print("8. Add to Wishlist")
        print("9. View Wishlist")
        print("10. Move from Wishlist to Recently Viewed")
        print("11. Exit")
        print("================================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_genres()
        elif choice == "2":
            show_all_books()
        elif choice == "3":
            recommend_by_genre()
        elif choice == "4":
            search_books()
        elif choice == "5":
            add_book()
        elif choice == "6":
            update_book()
        elif choice == "7":
            view_recent()
        elif choice == "8":
            add_to_wishlist()
        elif choice == "9":
            view_wishlist()
        elif choice == "10":
            move_from_wishlist_to_recent()
        elif choice == "11":
            print("Exiting Program...")
            break
        else:
            print("Invalid choice, try again.")


main()
