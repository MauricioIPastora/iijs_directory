from tkinter import *
from tkinter import simpledialog
import backend

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
    except IndexError:
        # No item selected
        selected_tuple = None


def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(
        fullname_text.get(),
        phonenumber_text.get(),
        linkedin_text.get(),
        instagram_text.get(),
        email_text.get(),
        organization_var.get(),
        organization_type_var.get(),
        twitter_text.get()
        ):
            list1.insert(END,row)

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

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
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
            selected_tuple[0]  # Pass the ID as the last argument
        )
        view_command()  # Refresh the list to show updated data
    else:
        print("No item selected for update.")

# Functions to add new organization or organization type
def add_new_option(option_list, dropdown_var):
    new_option = simpledialog.askstring("Add New Option", "Enter new option:")
    if new_option and new_option not in option_list:
        option_list.append(new_option)
        dropdown_var.set(new_option)
        update_dropdowns()

def update_dropdowns():
    # Update organization dropdown
    org_menu = organization_dropdown.children['menu']
    org_menu.delete(0, 'end')
    for org in organization_options:
        org_menu.add_command(label=org, command=lambda value=org: organization_var.set(value))

    # Update organization type dropdown
    org_type_menu = organization_type_dropdown.children['menu']
    org_type_menu.delete(0, 'end')
    for org_type in organization_type_options:
        org_type_menu.add_command(label=org_type, command=lambda value=org_type: organization_type_var.set(value))

window = Tk()
window.wm_title("IIJS Directory")

# Labels
Label(window, text="Full Name").grid(row=0,column=0)
Label(window, text="Phone Number").grid(row=0,column=2)
Label(window, text="Linkedin").grid(row=0,column=4)
Label(window, text="Instagram").grid(row=0,column=6)
Label(window, text="Email").grid(row=1,column=0)
Label(window, text="Organization").grid(row=1,column=2)
Label(window, text="Organization Type").grid(row=1,column=4)
Label(window, text="Twitter").grid(row=1,column=6)

# Define StringVar variables before Entry widgets
fullname_text = StringVar()
phonenumber_text = StringVar()
linkedin_text = StringVar()
instagram_text = StringVar()
email_text = StringVar()
twitter_text = StringVar()

# Entry fields
e1 = Entry(window, textvariable=fullname_text)
e1.grid(row=0, column=1)

e2 = Entry(window, textvariable=phonenumber_text)
e2.grid(row=0, column=3)

e3 = Entry(window, textvariable=linkedin_text)
e3.grid(row=0, column=5)

e4 = Entry(window, textvariable=instagram_text)
e4.grid(row=0, column=7)

e5 = Entry(window, textvariable=email_text)
e5.grid(row=1, column=1)

e6 = Entry(window, textvariable=twitter_text)
e6.grid(row=1, column=7)

# Dropdown options
organization_options = ["OAS", "Inter-American Development Bank", "World Bank", ]
organization_type_options = ["OAS", "Academia", "Private", "World Bank", "IADB", "Embassy"]

# Organization dropdown
organization_var = StringVar(window)
organization_var.set(organization_options[0])  # Default value
organization_dropdown = OptionMenu(window, organization_var, *organization_options)
organization_dropdown.grid(row=1,column=3)

Button(window, text="Add Org", command=lambda: add_new_option(organization_options, organization_var)).grid(row=1,column=3,sticky=E)

# Organization Type dropdown
organization_type_var = StringVar(window)
organization_type_var.set(organization_type_options[0])  # Default value
organization_type_dropdown = OptionMenu(window, organization_type_var, *organization_type_options)
organization_type_dropdown.grid(row=1,column=5)

Button(window, text="Add Type", command=lambda: add_new_option(organization_type_options, organization_type_var)).grid(row=1,column=5,sticky=E)

# Contacts List box
list1=Listbox(window,height=8,width=70)
list1.grid(row=2,column=0,rowspan=7,columnspan=5,)

# scroll bar for list box
sb1=Scrollbar(window)
sb1.grid(row=2,column=5,rowspan=7)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

# View all contacts button
b1=Button(window,text="View All", width=12,command=view_command)
b1.grid(row=2,column=6,columnspan=2)
#Search Button
b2=Button(window,text="Search", width=12,command=search_command)
b2.grid(row=3,column=6,columnspan=2)
#Add entry Button
b3=Button(window,text="Add Entry", width=12,command=add_command)
b3.grid(row=4,column=6,columnspan=2)
#Update Entry Button
b4=Button(window,text="Update Selected", width=12,command=update_command)
b4.grid(row=5,column=6,columnspan=2)
#Delete Entry Button
b5=Button(window,text="Delete Selected", width=12,command=delete_command)
b5.grid(row=6,column=6,columnspan=2)
#Close Button
b6=Button(window,text="Close", width=12,command=window.destroy)
b6.grid(row=7,column=6,columnspan=2)


# Main loop
window.mainloop()

