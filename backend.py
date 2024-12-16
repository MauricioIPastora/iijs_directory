import sqlite3

#connect to database
def connect():
    conn=sqlite3.connect("contacts.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS contact (id INTEGER PRIMARY KEY, full_name text, phone_number varchar, linkedin varchar, instagram varchar, email varchar, organization text, org_type text, twitter varchar)")
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
    conn=sqlite3.connect("contacts.db")
    cur=conn.cursor()
    cur.execute("""
        SELECT * FROM contact
        WHERE full_name=?
          OR phone_number=?
          OR linkedin=?
          OR instagram=?
          OR email=?
          OR organization=?
          OR org_type=?
          OR twitter=?
          """, (full_name, phone_number, linkedin, instagram, email, organization, org_type, twitter))
    rows=cur.fetchall()
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

# Create table and test insertion
connect()
print(view())

