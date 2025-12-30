from flask import Flask, render_template, request, redirect, url_for

# Mocking your imports for structure
from db.workshop import create_workshop_if_not_exists
from db.customer import add_customer
from db.invoice import create_invoice
from db.invoice_services import add_service
from db.payments import add_payment
from db.update_invoice_totals import update_invoice_totals
from db.fetch_invoice import fetch_invoice_full

app = Flask(__name__)

# Initialize DB structure on startup
create_workshop_if_not_exists()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create-invoice", methods=["POST"])
def create_invoice_route():
    try:
        # 1. Handle Customer
        customer_name = request.form.get("customer_name")
        phone = request.form.get("phone")
        
        # Assume add_customer returns the unique ID of the customer (new or existing)
        customer_id = add_customer(customer_name, "", phone)

        # 2. Create Base Invoice
        invoice_id = create_invoice(customer_id, None)

        # 3. Process Multiple Services
        service_names = request.form.getlist("service_name[]")
        prices = request.form.getlist("price[]")
        gst_percents = request.form.getlist("gst_percent[]")

        for name, price, gst in zip(service_names, prices, gst_percents):
            if name.strip() and price:
                add_service(
                    invoice_id,
                    name.strip(),
                    float(price),
                    float(gst) if gst else 18.0
                )

        # 4. Calculate Totals (Crucial before payment)
        update_invoice_totals(invoice_id)

        # 5. Handle Payment
        # Fetch the invoice again to get the final total_amount calculated in step 4
        _, invoice, _, _ = fetch_invoice_full(invoice_id)
        
        payment_mode = request.form.get("payment_mode")
        payment_type = request.form.get("payment_type")

        add_payment(
            invoice_id,
            invoice["total_amount"], # Paying full amount for this example
            payment_mode,
            payment_type
        )

        return redirect(url_for('view_invoice', invoice_id=invoice_id))
    
    except Exception as e:
        print(f"Error: {e}")
        return "Internal Server Error", 500

@app.route("/invoice/<int:invoice_id>")
def view_invoice(invoice_id):
    workshop, invoice, services, payments = fetch_invoice_full(invoice_id)
    if not invoice:
        return "Invoice not found", 404
        
    return render_template(
        "invoice.html",
        workshop=workshop,
        invoice=invoice,
        services=services,
        payments=payments
    )

if __name__ == "__main__":
    app.run(debug=True)