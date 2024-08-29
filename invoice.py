from datetime import datetime
import os

# Function to get input from the user
def get_invoice_details():
    print("Enter Company Details:")
    company_name = input("Company Name: ")
    company_address = input("Company Address: ")
    company_email = input("Company Email: ")
    company_phone = input("Company Phone: ")

    print("\nEnter Customer Details:")
    customer_name = input("Customer Name: ")
    customer_address = input("Customer Address: ")

    items = []
    print("\nEnter Item Details (type 'done' when finished):")
    while True:
        description = input("Item Description: ")
        if description.lower() == 'done':
            break
        quantity = int(input("Quantity: "))
        price = float(input("Price: "))
        items.append({"description": description, "quantity": quantity, "price": price})

    invoice_number = input("\nInvoice Number: ")
    invoice_date = datetime.now().strftime("%Y-%m-%d")

    return {
        "company_name": company_name,
        "company_address": company_address,
        "company_email": company_email,
        "company_phone": company_phone,
        "customer_name": customer_name,
        "customer_address": customer_address,
        "items": items,
        "invoice_number": invoice_number,
        "invoice_date": invoice_date
    }

# Calculate totals
def calculate_totals(items):
    subtotal = sum(item['quantity'] * item['price'] for item in items)
    tax_rate = 0.07  # 7% tax
    tax = subtotal * tax_rate
    total = subtotal + tax
    return subtotal, tax, total

# Generate Text-Based Invoice
def generate_invoice(details, subtotal, tax, total):
    invoice = []
    invoice.append(f"Invoice: {details['invoice_number']}")
    invoice.append(f"Date: {details['invoice_date']}")
    invoice.append("=" * 40)
    invoice.append(f"{details['company_name']}")
    invoice.append(f"{details['company_address']}")
    invoice.append(f"Email: {details['company_email']}")
    invoice.append(f"Phone: {details['company_phone']}")
    invoice.append("=" * 40)
    invoice.append(f"Bill To:")
    invoice.append(f"{details['customer_name']}")
    invoice.append(f"{details['customer_address']}")
    invoice.append("=" * 40)
    invoice.append(f"{'Description':<20} {'Qty':<5} {'Price':<10} {'Total':<10}")
    invoice.append("-" * 40)

    for item in details['items']:
        total_price = item['quantity'] * item['price']
        invoice.append(f"{item['description']:<20} {item['quantity']:<5} ${item['price']:<10.2f} ${total_price:<10.2f}")

    invoice.append("-" * 40)
    invoice.append(f"{'Subtotal':<20} ${subtotal:.2f}")
    invoice.append(f"{'Tax (7%)':<20} ${tax:.2f}")
    invoice.append(f"{'Total':<20} ${total:.2f}")
    invoice.append("=" * 40)

    # Save the invoice to a text file
    invoice_dir = "invoices"
    os.makedirs(invoice_dir, exist_ok=True)
    invoice_file = os.path.join(invoice_dir, f"invoice_{details['invoice_number']}.txt")
    with open(invoice_file, 'w') as file:
        file.write("\n".join(invoice))

    print(f"Invoice generated and saved as {invoice_file}")

# Main logic to run the invoice generator
def run_invoice_generator():
    details = get_invoice_details()
    subtotal, tax, total = calculate_totals(details['items'])
    generate_invoice(details, subtotal, tax, total)

# Run the invoice generator
run_invoice_generator()
