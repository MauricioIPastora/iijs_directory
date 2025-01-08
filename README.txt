# IIJS Directory
### Video Demo: <URL HERE>
### Description: This project is a Contact Management Database designed for managing and organizing contact information.
It features a user-friendly desktop interface built with Python's Tkinter library and a SQLite database for backend storage.
The application supports operations like adding, viewing, updating, searching, and deleting contacts.
It also includes dropdown menus for organization and organization type, which users can dynamically update.

The frontend code is responsible for providing the graphical user interface (GUI) using Python's Tkinter library.
It allows users to interact with the contact database through a series of input fields, buttons, and dropdown menus. Users can enter contact details such as full name, phone number,
LinkedIn, Instagram, email, organization, organization type, and Twitter. The interface includes buttons for key functionalities: viewing all contacts, searching for specific contacts,
adding new entries, updating selected contacts, deleting selected contacts, and closing the application. A dynamic dropdown menu system enables users to manage and customize organization
and organization type options. A listbox displays contact records and supports selection for update or deletion. The frontend's core functions include retrieving and displaying selected
contact details, managing CRUD operations, and dynamically updating dropdown menus.

The backend code manages the database operations using SQLite. It ensures data is stored, retrieved, updated, and deleted efficiently.
The database is initialized through the connect() function, which creates the contacts.db file and the contact table, aswell as the organization table, and organization type table so when
new organizations and organization types are added to the dropdown list, they are saved so they continue to populate the dropdown when the program is closed and opened again.
Key functions include insert() for adding new contacts, view() for retrieving all records, search() for querying contacts based on user-provided criteria,
delete() for removing contacts by their unique ID, and update() for modifying existing contact details. The database schema consists of a three tables,
contact, organizations, and organization_type, with columns for ID (primary key), full name, phone number, LinkedIn, Instagram, email, organization, organization type, and Twitter in the contact table,
and name columns for the organization and organization type tables.

Together, the frontend and backend work seamlessly to provide a user-friendly application for managing contact information, integrating a robust GUI with efficient database operations.
