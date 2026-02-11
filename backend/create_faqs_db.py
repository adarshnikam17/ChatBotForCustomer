import sqlite3

conn = sqlite3.connect('faqs.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS faqs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
)
''')

cursor.executemany('''
INSERT INTO faqs (question, answer)
VALUES (?, ?)
''', [
    ('Can I cancel my order?', 'Yes, orders can be canceled within 2 hours of placement or before shipment.'),
    ('How do I update my account information?', 'Log in to your account and go to the “Profile” section to update your info.'),
    ('Do you offer gift wrapping?', 'Yes, we offer gift wrapping at checkout for an additional fee.'),
    ('Are your products eco-friendly?', 'Yes, we strive to use sustainable and eco-friendly materials.'),
    ('Can I get a GST invoice?', 'Yes, please provide your GST details at the time of purchase to receive a GST invoice.'),
    ('What if I receive a damaged item?', 'Please contact support within 48 hours with pictures for a replacement or refund.'),
    ('How do I use a promo code?', 'Apply the promo code at checkout to avail the discount.'),
    ('Where can I see my order history?', 'Log in to your account and go to “My Orders” to view your order history.'),
    ('Is COD (Cash on Delivery) available?', 'Yes, COD is available for select locations.'),
    ('How can I unsubscribe from promotional emails?', 'Click the unsubscribe link at the bottom of any promotional email.'),
    ('Do you have physical stores?', 'Currently, we are an online-only store.'),
    ('How do I delete my account?', 'Please contact support to request account deletion.'),
    ('Do you offer bulk discounts?', 'Yes, for bulk purchases, please contact our sales team.'),
    ('What if I entered the wrong email or phone number?', 'Contact support as soon as possible to update your contact details.'),
    ('Can I schedule a delivery date?', 'Yes, you can choose a preferred delivery date at checkout if available.'),
])


conn.commit()
conn.close()

print("Database setup complete.")
