# from connection import get_db

# def init_db():
#     conn = get_db()
#     cur = conn.cursor()

#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS workshop (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT,
#         gst_no TEXT,
#         address TEXT
#     )
#     """)

#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS customer (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT,
#         gst_no TEXT,
#         phone TEXT
#     )
#     """)

#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS invoice (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         invoice_number TEXT,
#         customer_id INTEGER,
#         delivery_date TEXT,
#         subtotal REAL,
#         gst_amount REAL,
#         total_amount REAL
#     )
#     """)

#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS invoice_services (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         invoice_id INTEGER,
#         service_name TEXT,
#         price REAL,
#         gst_percent REAL
#     )
#     """)

#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS payments (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         invoice_id INTEGER,
#         amount REAL,
#         payment_mode TEXT,
#         payment_type TEXT,
#         payment_date TEXT
#     )
#     """)

#     conn.commit()
#     conn.close()


# if __name__ == "__main__":
#     init_db()
#     print("Database initialized successfully")
