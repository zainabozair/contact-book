# Python Contact Book

A simple console-based Contact Book application created as my final project for Python Essentials 1.

## Features

- Add new contacts
- Prevent duplicate contact names
- View all contacts
- Search by full or partial name
- Delete contacts
- Validate names and phone numbers
- Handle invalid menu input
- Exit the program through the menu

## How It Works

The program uses a Python dictionary to store contacts. The contact name is used as the key and the phone number is stored as the value.

The program is divided into separate functions:

- `add_contact()` adds a new contact and checks for duplicates and invalid input.
- `view_contacts()` displays all saved contacts.
- `search_contact()` searches for a full or partial name.
- `delete_contact()` removes an existing contact.

A `while` loop keeps the menu running until the user selects Exit. The program also uses `try/except` to handle invalid menu input without crashing.

## Python Concepts Used

- Variables and data types
- Input and output
- Dictionaries
- Conditionals
- `while` and `for` loops
- Functions
- String methods
- Exception handling with `try/except`

## Challenges and What I Learned

One challenge was making sure duplicate contacts were not added. I used the contact name as the dictionary key and checked whether the name already existed before adding it.

I also learned how to use a loop to search through the dictionary for partial name matches and how `try/except` can prevent the program from crashing when the user enters invalid menu input.

## Files

- `contact_book.py` - Main Contact Book program
- `sample_output.txt` - Example test run demonstrating the program features

## Running the Program

Run the program from the terminal:

```bash
python contact_book.py