from tkinter import *
from tkinter import simpledialog
import backend
import ctypes
from PIL import Image, ImageTk

def get_selected_row(event):
    global selected_tuple
    try:
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
        e5.delete(0, END)
        e5.insert(END, selected_tuple[5])
        e6.delete(0, END)
        e6.insert(END, selected_tuple[8])
        organization_var.set(selected_tuple[6])
        organization_type_var.set(selected_tuple[7])
    except IndexError:
        # No item selected
        selected_tuple = None

backspace_active = False

#Create ability to hold backspace to delete characters
def on_backspace_press(event):
    """Start deleting characters when backspace is pressed."""
    global backspace_active
    backspace_active = True
    delete_character()

#When backspace is released stop deleting characters
def on_backspace_release(event):
    """Stop deleting characters on backspace release."""
    global backspace_active
    backspace_active = False

def delete_character(event):
    """Delete the last character from the focused Entry widget."""
    if backspace_active:
        widget = window.focus_get()  # Get the currently focused widget
        if isinstance(widget, Entry):  # Check if it's an Entry widget
            current_text = widget.get()
            if current_text:  # Only delete if there's text
                widget.delete(len(current_text) - 1, END)
        # Call this function again after a short delay
        window.after(60, delete_character)


#define view command
def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

#define search command
def search_command():
    list1.delete(0, END)
    rows = backend.search(
        full_name=fullname_text.get(),
        phone_number=phonenumber_text.get(),
        linkedin=linkedin_text.get(),
        instagram=instagram_text.get(),
        email=email_text.get(),
        organization=organization_var.get() if organization_var.get() != "Select Organization" else "",
        org_type=organization_type_var.get() if organization_type_var.get() != "Select Type" else "",
        twitter=twitter_text.get()
    )
    for row in rows:
        list1.insert(END, row)

#define add commmand
def add_command():
    backend.insert(
        fullname_text.get(),
        phonenumber_text.get(),
        linkedin_text.get(),
        instagram_text.get(),
        email_text.get(),
        organization_var.get(),
        organization_type_var.get(),
        twitter_text.get()
        )
    list1.delete(0,END)
    list1.insert(END,
        fullname_text.get(),
        phonenumber_text.get(),
        linkedin_text.get(),
        instagram_text.get(),
        email_text.get(),
        organization_var.get(),
        organization_type_var.get(),
        twitter_text.get())

#define delete command
def delete_command():
    global selected_tuple
    if selected_tuple:
        backend.delete(selected_tuple[0])
        view_command()
        selected_tuple = None  # Reset after deletion
    else:
        print("No item selected for deletion.")

#define update command
def update_command():
    global selected_tuple
    if selected_tuple:
        backend.update(
            fullname_text.get(),
            phonenumber_text.get(),
            linkedin_text.get(),
            instagram_text.get(),
            email_text.get(),
            organization_var.get(),
            organization_type_var.get(),
            twitter_text.get(),
            selected_tuple[0] #id
        )
        view_command()  # Refresh the list to show updated data
        selected_tuple = None  # Reset after deletion
    else:
        print("No item selected for update.")

def add_new_option(option_list, dropdown_var, type_):
    new_option = simpledialog.askstring("Add New Option", "Enter new option:")
    if new_option and new_option not in option_list:
        option_list.append(new_option)
        dropdown_var.set(new_option)
        backend.save_new_option(new_option, type_)
        update_dropdowns()

def delete_selected_option(option_list, dropdown_var, type_):
    selected_option = dropdown_var.get()
    if selected_option and selected_option != f"Select {type_}":
        if selected_option in option_list:
            option_list.remove(selected_option)
            dropdown_var.set(f"Select {type_}")
            backend.delete_option(selected_option, type_)
            update_dropdowns()
        else:
            print(f"{type_} not found in list")
    else:
        print(f"No valid {type_} selected to delete")

def update_dropdowns():
    global organization_options, organization_type_options
    organization_options = backend.load_options("organization")
    organization_type_options = backend.load_options("organization_type")

    org_menu = organization_dropdown.children['menu']
    org_menu.delete(0, 'end')
    for org in organization_options:
        org_menu.add_command(label=org, command=lambda value=org: organization_var.set(value))

    org_type_menu = organization_type_dropdown.children['menu']
    org_type_menu.delete(0, 'end')
    for org_type in organization_type_options:
        org_type_menu.add_command(label=org_type, command=lambda value=org_type: organization_type_var.set(value))

# Create the window
window = Tk()
window.wm_title("IIJS Directory")

# Create a frame for the logo and apply padding
logo_frame = Frame(window, bg="#00609C")
logo_frame.grid(row=0, column=0, columnspan=8, pady=20)

# Add the logo to the frame
logo_image = Image.open("/workspaces/131306115/iijs_directory/logocircleenglish.jpg")
logo_image = logo_image.resize((200, 200))
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = Label(logo_frame, image=logo_photo, bg="#00609C")
logo_label.grid(row=0, column=0)

# Create a frame for the form inputs
form_frame = Frame(window, bg="#00609C")
form_frame.grid(row=1, column=0, columnspan=8, pady=20)

# Label style
label_style = {"bg": "#00609C", "fg": "#fcfcfc", "font": ("Calibri", 12, "bold")}

# Define StringVar objects for input fields
fullname_text = StringVar()
phonenumber_text = StringVar()
linkedin_text = StringVar()
instagram_text = StringVar()
email_text = StringVar()
organization_var = StringVar()
organization_type_var = StringVar()
twitter_text = StringVar()

# Labels and Entry fields
Label(form_frame, text="Full Name", **label_style).grid(row=0, column=0, padx=10, pady=10)
e1 = Entry(form_frame, textvariable=fullname_text)
e1.grid(row=0, column=1, padx=10, pady=10)

Label(form_frame, text="Phone Number", **label_style).grid(row=0, column=2, padx=10, pady=10)
e2 = Entry(form_frame, textvariable=phonenumber_text)
e2.grid(row=0, column=3, padx=10, pady=10)

Label(form_frame, text="LinkedIn", **label_style).grid(row=0, column=4, padx=10, pady=10)
e3 = Entry(form_frame, textvariable=linkedin_text)
e3.grid(row=0, column=5, padx=10, pady=10)

Label(form_frame, text="Instagram", **label_style).grid(row=0, column=6, padx=10, pady=10)
e4 = Entry(form_frame, textvariable=instagram_text)
e4.grid(row=0, column=7, padx=10, pady=10)

Label(form_frame, text="Email", **label_style).grid(row=1, column=0, padx=10, pady=10)
e5 = Entry(form_frame, textvariable=email_text)
e5.grid(row=1, column=1, padx=10, pady=10)

Label(form_frame, text="Twitter", **label_style).grid(row=1, column=6, padx=10, pady=10)
e6 = Entry(form_frame, textvariable=twitter_text)
e6.grid(row=1, column=7, padx=10, pady=10)

# Fetch initial options from the database
organization_options = [row[0] for row in backend.fetch_organizations()]
organization_type_options = [row[0] for row in backend.fetch_organization_types()]

organization_var.set(organization_options[0])
organization_type_var.set(organization_type_options[0])

# Organization Dropdown
organization_dropdown = OptionMenu(form_frame, organization_var, *organization_options)
organization_dropdown.grid(row=1, column=3, padx=10, pady=10)

# Organization Type Dropdown
organization_type_dropdown = OptionMenu(form_frame, organization_type_var, *organization_type_options)
organization_type_dropdown.grid(row=1, column=5, padx=10, pady=10)

# Create a frame for buttons
button_frame = Frame(window, bg="#00609C")
button_frame.grid(row=2, column=0, columnspan=8, pady=20)

# Button style
button_style = {"bg": "#80BC00", "fg": "white", "font": ("Calibri", 10, "bold"), "activebackground": "#636569"}

Button(form_frame, text="+", **button_style, command=lambda: add_new_option(organization_options, organization_var, "organization")).grid(row=1, column=2, padx=5, pady=10)
Button(form_frame, text="+", **button_style, command=lambda: add_new_option(organization_type_options, organization_type_var, "organization_type")).grid(row=1, column=4, padx=5, pady=10, sticky="w")

Button(form_frame, text="-", **button_style, command=lambda: delete_selected_option(organization_options, organization_var, "organization")).grid(row=1, column=2, padx=5, pady=10, sticky="e")
Button(form_frame, text="-", **button_style, command=lambda: delete_selected_option(organization_type_options, organization_type_var, "organization_type")).grid(row=1, column=4, padx=5, pady=10, sticky="e")

# Buttons
b1 = Button(button_frame, text="View All", **button_style, command=view_command)
b1.grid(row=0, column=0, padx=10, pady=10)

b2 = Button(button_frame, text="Search", **button_style, command=search_command)
b2.grid(row=0, column=1, padx=10, pady=10)

b3 = Button(button_frame, text="Add Entry", **button_style, command=add_command)
b3.grid(row=0, column=2, padx=10, pady=10)

b4 = Button(button_frame, text="Update Selected", **button_style, command=update_command)
b4.grid(row=0, column=3, padx=10, pady=10)

b5 = Button(button_frame, text="Delete Selected", **button_style, command=delete_command)
b5.grid(row=0, column=4, padx=10, pady=10)

b6 = Button(button_frame, text="Close", **button_style, command=window.destroy)
b6.grid(row=0, column=5, padx=10, pady=10)

# Create a frame for the listbox
listbox_frame = Frame(window, bg="#00609C")
listbox_frame.grid(row=3, column=0, columnspan=8, pady=20)

# Listbox and Scrollbar
list1 = Listbox(listbox_frame, height=8, width=70)
list1.grid(row=0, column=0, padx=10, pady=10)

sb1 = Scrollbar(listbox_frame)
sb1.grid(row=0, column=1, sticky="ns", pady=10)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

# Main loop
window.mainloop()
