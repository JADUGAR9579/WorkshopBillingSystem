from .connection import get_db

def create_workshop_if_not_exists():
    conn = get_db()

    existing = conn.execute(
        "SELECT id FROM workshop LIMIT 1"
    ).fetchone()

    if not existing:
        conn.execute("""
            INSERT INTO workshop (name, gst_no, address)
            VALUES (?, ?, ?)
        """, (
            "Bhairavnath Enterprises",
            "27ABCDE1234F1Z5",
            "Pune, Maharashtra"
        ))
        conn.commit()

    conn.close()


def get_workshop():
    conn = get_db()
    row = conn.execute(
        "SELECT * FROM workshop LIMIT 1"
    ).fetchone()
    conn.close()
    return row
