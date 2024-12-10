from tkinter import *
from tkinter import simpledialog

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
window.title("Data Entry Form")

# Labels
Label(window, text="Full Name").grid(row=0,column=0)
Label(window, text="Phone Number").grid(row=0,column=2)
Label(window, text="Linkedin").grid(row=0,column=4)
Label(window, text="Instagram").grid(row=0,column=6)
Label(window, text="Email").grid(row=1,column=0)
Label(window, text="Organization").grid(row=1,column=2)
Label(window, text="Organization Type").grid(row=1,column=4)
Label(window, text="Twitter").grid(row=1,column=6)

# Entry fields
fullname_text = StringVar()
Entry(window, textvariable=fullname_text).grid(row=0,column=1)

phonenumber_text = StringVar()
Entry(window, textvariable=phonenumber_text).grid(row=0,column=3)

linkedin_text = StringVar()
Entry(window, textvariable=linkedin_text).grid(row=0,column=5)

instagram_text = StringVar()
Entry(window, textvariable=instagram_text).grid(row=0,column=7)

email_text = StringVar()
Entry(window, textvariable=email_text).grid(row=1,column=1)

twitter_text = StringVar()
Entry(window, textvariable=twitter_text).grid(row=1,column=7)

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

# View all contacts button
b1=Button(window,text="View All", width=12)
b1.grid(row=2,column=6,columnspan=2)
#Search Button
b2=Button(window,text="Search", width=12)
b2.grid(row=3,column=6,columnspan=2)
#Add entry Button
b3=Button(window,text="Add Entry", width=12)
b3.grid(row=4,column=6,columnspan=2)
#Update Entry Button
b4=Button(window,text="Update Selected", width=12)
b4.grid(row=5,column=6,columnspan=2)
#Delete Entry Button
b5=Button(window,text="Delete Selected", width=12)
b5.grid(row=6,column=6,columnspan=2)
#Close Button
b6=Button(window,text="Close", width=12)
b6.grid(row=7,column=6,columnspan=2)



# Main loop
window.mainloop()

