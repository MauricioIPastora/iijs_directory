import sqlite3

#connect to database
def connect():
    conn=sqlite3.connect("contacts.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS contact (id INTEGER PRIMARY KEY, full_name text, phone_number varchar, linkedin varchar, instagram varchar, email varchar, organization text, org_type text, twitter varchar)")
    cur.execute("""CREATE TABLE IF NOT EXISTS organization (id INTEGER PRIMARY KEY,name TEXT UNIQUE)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS organization_type (id INTEGER PRIMARY KEY,name TEXT UNIQUE)""")
        # Insert default values if not already present
    cur.execute("INSERT OR IGNORE INTO organization (name) VALUES ('Select Organization')")
    cur.execute("INSERT OR IGNORE INTO organization_type (name) VALUES ('Select Type')")
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

def get_organizations():
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("SELECT name FROM organization")
    rows = [row[0] for row in cur.fetchall()]
    conn.close()
    return rows

def add_organization(name):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO organization (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def delete_organization(name):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM organization WHERE name = ? AND name != 'Select Organization'", (name,))
    conn.commit()
    conn.close()

def get_organization_types():
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("SELECT name FROM organization_type")
    rows = [row[0] for row in cur.fetchall()]
    conn.close()
    return rows

def add_organization_type(name):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO organization_type (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def delete_organization_type(name):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM organization_type WHERE name = ? AND name != 'Select Type'", (name,))
    conn.commit()
    conn.close()

# Create table and test insertion
connect()
print("Application Launched")

