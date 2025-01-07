import sqlite3

#connect to database
def connect():
    conn=sqlite3.connect("contacts.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS contact (id INTEGER PRIMARY KEY, full_name text, phone_number varchar, linkedin varchar, instagram varchar, email varchar, organization text, org_type text, twitter varchar)")
    cur.execute("CREATE TABLE IF NOT EXISTS organizations (name TEXT PRIMARY KEY)")
    cur.execute("CREATE TABLE IF NOT EXISTS organization_type (name TEXT PRIMARY KEY)")
    conn.commit()
    conn.close()

#insert values
def insert(full_name, phone_number, linkedin, instagram, email, organization, org_type, twitter):
    conn=sqlite3.connect("contacts.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO contact VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)",(full_name, phone_number, linkedin, instagram, email, organization, org_type, twitter))
    conn.commit()
    conn.close()

#viewall contacts
def view():
    conn=sqlite3.connect("contacts.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM contact")
    rows=cur.fetchall()
    conn.close()
    return rows

#search contacts
def search(full_name="", phone_number="", linkedin="", instagram="", email="", organization="", org_type="", twitter=""):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()

    # Build the query dynamically
    query = "SELECT * FROM contact WHERE 1=1"
    parameters = []

    if full_name:
        query += " AND LOWER(full_name) LIKE ?"
        parameters.append(f"%{full_name.lower()}%")
    if phone_number:
        query += " AND phone_number LIKE ?"
        parameters.append(f"%{phone_number}%")
    if linkedin:
        query += " AND LOWER(linkedin) LIKE ?"
        parameters.append(f"%{linkedin.lower()}%")
    if instagram:
        query += " AND LOWER(instagram) LIKE ?"
        parameters.append(f"%{instagram.lower()}%")
    if email:
        query += " AND LOWER(email) LIKE ?"
        parameters.append(f"%{email.lower()}%")
    if organization:
        query += " AND LOWER(organization) LIKE ?"
        parameters.append(f"%{organization.lower()}%")
    if org_type:
        query += " AND LOWER(org_type) LIKE ?"
        parameters.append(f"%{org_type.lower()}%")
    if twitter:
        query += " AND LOWER(twitter) LIKE ?"
        parameters.append(f"%{twitter.lower()}%")

    cur.execute(query, parameters)
    rows = cur.fetchall()
    conn.close()
    return rows


#delete contacts
def delete(id):
    conn=sqlite3.connect("contacts.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM contact WHERE id=?",(id,))
    conn.commit()
    conn.close()

#update contacts
def update(full_name, phone_number, linkedin, instagram, email, organization, org_type, twitter, id):
    conn=sqlite3.connect("contacts.db")
    cur=conn.cursor()
    cur.execute("""
                UPDATE contact
                SET full_name=?,
                  phone_number=?,
                  linkedin=?,
                  instagram=?,
                  email=?,
                  organization=?,
                  org_type=?,
                  twitter=?
                WHERE id=?
                """,
                (full_name, phone_number, linkedin, instagram, email, organization, org_type, twitter, id)
                )
    conn.commit()
    conn.close()

def load_options(option_type):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    table_name = "organization" if option_type == "organization" else "organization_type"
    cur.execute(f"SELECT name FROM {table_name}")
    rows = cur.fetchall()
    conn.close()
    return [row[0] for row in rows]

def save_new_option(option_name, option_type):
    if option_name or option_type in ["Select Organization", "Select Type"]:
        return "Default Option already exists."
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    table_name = "organization" if option_type == "organization" else "organization_type"
    cur.execute(f"INSERT OR IGNORE INTO {table_name} (name) VALUES (?)", (option_name,))
    conn.commit()
    conn.close()

def delete_option(option_name, option_type):
    if option_name or option_type in ["Select Organization", "Select Type"]:
        return "Cannot delete default option."
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    table_name = "organization" if option_type == "organization" else "organization_type"
    cur.execute(f"DELETE FROM {table_name} WHERE name=?", (option_name,))
    conn.commit()
    conn.close()

# Fetch all organizations
def fetch_organizations():
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("SELECT name FROM organization")
    rows = cur.fetchall()
    conn.close()
    return rows

# Fetch all organization types
def fetch_organization_types():
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("SELECT name FROM organization_type")
    rows = cur.fetchall()
    conn.close()
    return rows

# Create table
connect()
print("Application Launched")
