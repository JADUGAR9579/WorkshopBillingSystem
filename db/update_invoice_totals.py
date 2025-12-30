from .connection import get_db

def update_invoice_totals(invoice_id):
    conn = get_db()

    rows = conn.execute("""
        SELECT price, gst_percent
        FROM invoice_services
        WHERE invoice_id = ?
    """, (invoice_id,)).fetchall()

    subtotal = 0
    gst_total = 0

    for r in rows:
        subtotal += r["price"]
        gst_total += (r["price"] * r["gst_percent"]) / 100

    total = subtotal + gst_total

    conn.execute("""
        UPDATE invoice
        SET subtotal = ?, gst_amount = ?, total_amount = ?
        WHERE id = ?
    """, (subtotal, gst_total, total, invoice_id))

    conn.commit()
    conn.close()
