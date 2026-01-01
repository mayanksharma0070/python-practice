# ---------------------------------------------------
# BOOK RECOMMENDATION SYSTEM (FULL MENU - FINAL)
# ---------------------------------------------------

books = {
    "Fiction": [
        ("To Kill a Mockingbird", "Harper Lee"),
        ("The Great Gatsby", "F. Scott Fitzgerald"),
        ("1984", "George Orwell"),
        ("Pride and Prejudice", "Jane Austen")
    ],
    "Non-Fiction": [
        ("Sapiens", "Yuval Noah Harari"),
        ("Educated", "Tara Westover"),
        ("Atomic Habits", "James Clear"),
        ("The Power of Habit", "Charles Duhigg")
    ],
    "Fantasy": [
        ("Harry Potter and the Sorcerer's Stone", "J.K. Rowling"),
        ("The Hobbit", "J.R.R. Tolkien"),
        ("A Game of Thrones", "George R.R. Martin"),
        ("The Name of the Wind", "Patrick Rothfuss")
    ],
    "Science Fiction": [
        ("Dune", "Frank Herbert"),
        ("Ender's Game", "Orson Scott Card"),
        ("The Martian", "Andy Weir"),
        ("Neuromancer", "William Gibson")
    ],
    "Mystery": [
        ("The Girl with the Dragon Tattoo", "Stieg Larsson"),
        ("Gone Girl", "Gillian Flynn"),
        ("Sherlock Holmes: The Hound of the Baskervilles", "Arthur Conan Doyle"),
        ("The Da Vinci Code", "Dan Brown")
    ],
    "Thriller": [
        ("The Silence of the Lambs", "Thomas Harris"),
        ("The Shining", "Stephen King"),
        ("The Girl on the Train", "Paula Hawkins"),
        ("Misery", "Stephen King")
    ],
    "Horror": [
        ("It", "Stephen King"),
        ("The Haunting of Hill House", "Shirley Jackson"),
        ("Bird Box", "Josh Malerman"),
        ("Dracula", "Bram Stoker")
    ],
    "Biography": [
        ("The Diary of a Young Girl", "Anne Frank"),
        ("Long Walk to Freedom", "Nelson Mandela"),
        ("Steve Jobs", "Walter Isaacson"),
        ("Becoming", "Michelle Obama")
    ],
    "Self Help": [
        ("The Subtle Art of Not Giving a F*ck", "Mark Manson"),
        ("How to Win Friends and Influence People", "Dale Carnegie"),
        ("Think and Grow Rich", "Napoleon Hill"),
        ("The 7 Habits of Highly Effective People", "Stephen Covey")
    ],
    "Historical": [
        ("The Book Thief", "Markus Zusak"),
        ("The Pillars of the Earth", "Ken Follett"),
        ("All the Light We Cannot See", "Anthony Doerr"),
        ("Wolf Hall", "Hilary Mantel")
    ],
    "Adventure": [
        ("Life of Pi", "Yann Martel"),
        ("Treasure Island", "Robert Louis Stevenson"),
        ("The Three Musketeers", "Alexandre Dumas"),
        ("Into the Wild", "Jon Krakauer")
    ],
    "Poetry": [
        ("Milk and Honey", "Rupi Kaur"),
        ("The Sun and Her Flowers", "Rupi Kaur"),
        ("Leaves of Grass", "Walt Whitman"),
        ("The Raven and Other Poems", "Edgar Allan Poe")
    ],
    "Philosophy": [
        ("Meditations", "Marcus Aurelius"),
        ("The Republic", "Plato"),
        ("Thus Spoke Zarathustra", "Friedrich Nietzsche"),
        ("Beyond Good and Evil", "Friedrich Nietzsche")
    ],
    "Drama": [
        ("The Merchant of Venice", "William Shakespeare"),
        ("Hamlet", "William Shakespeare"),
        ("A Doll's House", "Henrik Ibsen"),
        ("Death of a Salesman", "Arthur Miller"),
        ("The Crucible", "Arthur Miller")
    ]
}


# ---------------------------------------------------
# FUNCTIONS
# ---------------------------------------------------

def show_genres():
    print("\nAvailable Genres:")
    for i, genre in enumerate(books.keys(), 1):
        print(f"{i}. {genre}")


def show_all_books():
    print("\n--- ALL BOOKS AVAILABLE ---")
    for genre, book_list in books.items():
        print(f"\n{genre}:")
        for title, author in book_list:
            print(f"  - {title} by {author}")


def recommend_by_genre():
    show_genres()
    choice = int(input("\nEnter genre number: "))

    genres = list(books.keys())
    if 1 <= choice <= len(genres):
        selected_genre = genres[choice - 1]
        print(f"\n--- Books in {selected_genre} ---")
        for title, author in books[selected_genre]:
            print(f"• {title} — {author}")
    else:
        print("Invalid genre number!")


def add_book():
    print("\n--- Add a New Book ---")
    show_genres()
    genre_choice = int(input("Enter genre number to add book to: "))

    genres = list(books.keys())
    if 1 <= genre_choice <= len(genres):
        genre = genres[genre_choice - 1]
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        books[genre].append((title, author))
        print(f"Book '{title}' added to genre '{genre}'.")
    else:
        print("Invalid genre!")


def search_book():
    print("\n--- Search Book by Name ---")
    search = input("Enter book title to search: ").lower()

    found = False
    for genre, book_list in books.items():
        for title, author in book_list:
            if search in title.lower():
                print(f"\nFound: {title} by {author}  | Genre: {genre}")
                found = True

    if not found:
        print("Book not found!")


# ---------------------------------------------------
# MAIN PROGRAM LOOP
# ---------------------------------------------------

while True:
    print("\n========== BOOK RECOMMENDATION SYSTEM ==========")
    print("1. Recommend books by genre")
    print("2. Show all genres")
    print("3. Show all books")
    print("4. Add a new book")
    print("5. Search a book by name")
    print("6. Exit")

    user_choice = input("Enter your choice: ")

    if user_choice == "1":
        recommend_by_genre()
    elif user_choice == "2":
        show_genres()
    elif user_choice == "3":
        show_all_books()
    elif user_choice == "4":
        add_book()
    elif user_choice == "5":
        search_book()
    elif user_choice == "6":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid option. Try again.")
