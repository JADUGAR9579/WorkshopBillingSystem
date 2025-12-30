from .connection import get_db
from datetime import datetime

def add_payment(invoice_id, amount, payment_mode, payment_type):
    payment_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = get_db()
    conn.execute("""
        INSERT INTO payments
        (invoice_id, amount, payment_mode, payment_type, payment_date)
        VALUES (?, ?, ?, ?, ?)
    """, (invoice_id, amount, payment_mode, payment_type, payment_date))
    conn.commit()
    conn.close()

def get_payments(invoice_id):
    conn = get_db()
    rows = conn.execute(
        "SELECT * FROM payments WHERE invoice_id = ?",
        (invoice_id,)
    ).fetchall()
    conn.close()
    return rows
