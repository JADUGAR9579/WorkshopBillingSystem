from .connection import get_db

def fetch_invoice_full(invoice_id):
    conn = get_db()

    invoice = conn.execute("""
        SELECT i.*, c.name AS customer_name, c.phone
        FROM invoice i
        JOIN customer c ON i.customer_id = c.id
        WHERE i.id = ?
    """, (invoice_id,)).fetchone()

    services = conn.execute("""
        SELECT * FROM invoice_services
        WHERE invoice_id = ?
    """, (invoice_id,)).fetchall()

    payments = conn.execute("""
        SELECT * FROM payments
        WHERE invoice_id = ?
    """, (invoice_id,)).fetchall()

    workshop = conn.execute("""
        SELECT * FROM workshop LIMIT 1
    """).fetchone()

    conn.close()

    return workshop, invoice, services, payments
