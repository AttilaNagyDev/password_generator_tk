from tkinter import *
import random
import pyperclip

GREY = "#5C6672"
FONT = ("Arial", 14)
BOLD_FONT = ("Arial", 14, "bold")
INFO_FONT = ("Arial", 14, "italic")

# Password characters:
small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['.', '!', '?', '€', '$', '£', '&', '@', '#', '+', '-', '*', '/', '_', '(', ')']


# ---------------------------------------------- PASSWORD GENERATOR ------------------------------------------------- #
def generate_password():

    # Start with an empty list of characters to choose from
    password_characters = []

    # Check the desired Password Length
    password_length = int(password_length_selector.get())

    # Check which Character Options are selected
    if include_small_letters.get():
        for n in range(password_length):
            small_letter = random.choice(small_letters)
            password_characters.append(small_letter)

    if include_capital_letters.get():
        for n in range(password_length):
            capital_letter = random.choice(capital_letters)
            password_characters.append(capital_letter)

    if include_numbers.get():
        password_characters += numbers

    if include_symbols.get():
        for n in range(password_length):
            symbol = random.choice(symbols)
            password_characters.append(symbol)

    # Generate a random password from all the chosen character types
    password_list = [random.choice(password_characters) for _ in range(password_length)]
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    # Copy the generated password to clipboard
    pyperclip.copy(password)

    # Display the info message to the user
    message.place(x=185, y=140, anchor='center')


# --------------------------------------------------- UI SETUP ------------------------------------------------------ #
main_window = Tk()
main_window.title("Password Generator")
main_window.config(padx=25, pady=35, bg=GREY, width=420, height=210)
main_window.resizable(width=False, height=False)

# Character Options
characters_label = Label(text="Character Options:", font=BOLD_FONT, bg=GREY, fg='white')
characters_label.place(x=10, y=10, anchor='w')

include_small_letters = BooleanVar()
small_letters_checkbutton = Checkbutton(text="Small Letters", variable=include_small_letters, bg=GREY, font=FONT)
small_letters_checkbutton.place(x=10, y=36, anchor='w')

include_capital_letters = BooleanVar()
capital_letters_checkbutton = Checkbutton(text="Capital Letters", variable=include_capital_letters, bg=GREY, font=FONT)
capital_letters_checkbutton.place(x=10, y=60, anchor='w')

include_numbers = BooleanVar()
numbers_checkbutton = Checkbutton(text="Numbers", variable=include_numbers, bg=GREY, font=FONT)
numbers_checkbutton.place(x=10, y=84, anchor='w')

include_symbols = BooleanVar()
symbols_checkbutton = Checkbutton(text="Symbols", variable=include_symbols, bg=GREY, font=FONT)
symbols_checkbutton.place(x=10, y=108, anchor='w')

# Set default states
small_letters_checkbutton.select()
capital_letters_checkbutton.select()
numbers_checkbutton.select()
symbols_checkbutton.select()

# Password Length
password_length_label = Label(text="Password Length:", font=BOLD_FONT, bg=GREY, fg='white')
password_length_label.place(x=180, y=10, anchor='w')
password_length_selector = Spinbox(from_=8, to=24, width=3, bg='white', fg='black', highlightbackground=GREY)
password_length_selector.place(x=305, y=10, anchor='w')

# Generate Password Button
generate_password_button = Button(text="Generate New Password", command=generate_password,
                                  highlightbackground=GREY, font=FONT, )
generate_password_button.place(x=180, y=45, anchor='w', width=180)

# Password Field
password_label = Label(text="Your New Password is:", font=BOLD_FONT, bg=GREY, fg='white')
password_label.place(x=360, y=84, anchor='e')
password_entry = Entry(bg="white", fg="black", font=FONT, width=31, highlightbackground=GREY)
password_entry.place(x=360, y=108, anchor='e')

# Message to the user if a password has been generated
message = Label(text="Your Password is available on the clipboard", font=INFO_FONT, bg=GREY, fg='yellow')

main_window.mainloop()
