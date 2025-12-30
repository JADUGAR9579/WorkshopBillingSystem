from .connection import get_db

def add_service(invoice_id, service_name, price, gst_percent):
    conn = get_db()
    conn.execute("""
        INSERT INTO invoice_services
        (invoice_id, service_name, price, gst_percent)
        VALUES (?, ?, ?, ?)
    """, (invoice_id, service_name, price, gst_percent))
    conn.commit()
    conn.close()

def get_services(invoice_id):
    conn = get_db()
    rows = conn.execute(
        "SELECT * FROM invoice_services WHERE invoice_id = ?",
        (invoice_id,)
    ).fetchall()
    conn.close()
    return rows
