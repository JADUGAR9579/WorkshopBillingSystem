from .connection import get_db
from datetime import datetime

def create_invoice(customer_id, delivery_date):
    conn = get_db()
    cur = conn.cursor()

    invoice_number = f"INV-{int(datetime.now().timestamp())}"
    invoice_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cur.execute("""
        INSERT INTO invoice 
        (invoice_number, customer_id, delivery_date, subtotal, gst_amount, total_amount)
        VALUES (?, ?, ?, 0, 0, 0)
    """, (invoice_number, customer_id, delivery_date))

    invoice_id = cur.lastrowid
    conn.commit()
    conn.close()
    return invoice_id

def get_invoice(invoice_id):
    conn = get_db()
    row = conn.execute(
        "SELECT * FROM invoice WHERE id = ?", (invoice_id,)
    ).fetchone()
    conn.close()
    return row
