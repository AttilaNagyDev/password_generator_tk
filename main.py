from tkinter import *

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
symbols = ['!', '?', '#', '$', '%', '&', '(', ')', '/', '*', '+', '-', '_']

# --------------------------------------------------- UI SETUP ------------------------------------------------------ #
main_window = Tk()
main_window.title("Password Generator")
main_window.config(padx=25, pady=35, bg=GREY, width=420, height=210)
main_window.resizable(width=False, height=False)

# Character Options
characters_label = Label(text="Character Options:", font=BOLD_FONT, bg=GREY, fg='white')
characters_label.place(x=10, y=10, anchor='w')

small_letters_checkbutton = Checkbutton(text="Small Letters", onvalue=True, offvalue=False,
                                        bg=GREY, fg='white', font=FONT)
small_letters_checkbutton.place(x=10, y=36, anchor='w')

capital_letters_checkbutton = Checkbutton(text="Capital Letters", onvalue=True, offvalue=False,
                                          bg=GREY, fg='white', font=FONT)
capital_letters_checkbutton.place(x=10, y=60, anchor='w')

numbers_checkbutton = Checkbutton(text="Numbers", onvalue=True, offvalue=False,
                                  bg=GREY, fg='white', font=FONT)
numbers_checkbutton.place(x=10, y=84, anchor='w')

symbols_checkbutton = Checkbutton(text="Symbols", onvalue=True, offvalue=False,
                                  bg=GREY, fg='white', font=FONT)
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
password_length = password_length_selector.get()

# Password Field
password_label = Label(text="Your New Password is:", font=BOLD_FONT, bg=GREY, fg='white')
password_label.place(x=180, y=50, anchor='w')
password_entry = Entry(main_window, bg="white", fg="black", font=FONT, width=21, highlightbackground=GREY)
password_entry.place(x=180, y=75, anchor='w')
password = password_entry.get()

# Generate Password Button
generate_password_button = Button(text="Generate New Password", highlightbackground=GREY, font=FONT)
generate_password_button.place(x=180, y=105, anchor='w', width=180)

# Message to the user if a password has been generated
message = Label(text="Your Password is already available on the clipboard", font=INFO_FONT, bg=GREY, fg='white')
if password != "":
    message.place(x=185, y=140, anchor='center')

main_window.mainloop()
