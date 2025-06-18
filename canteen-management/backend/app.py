from flask import Flask, request, jsonify
import bcrypt # For password hashing

app = Flask(__name__)

# In-memory storage for users (temporary, will be replaced by a database)
users_db = {} # Store user_id: {username, password_hash, role}
next_user_id = 1

@app.route('/auth/register', methods=['POST'])
def register():
    global next_user_id
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role', 'customer') # Default role is customer

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    if username in [u['username'] for u in users_db.values()]:
        return jsonify({'message': 'Username already exists'}), 409

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    users_db[next_user_id] = {
        'username': username,
        'password_hash': hashed_password,
        'role': role
    }
    user_id = next_user_id
    next_user_id += 1

    # In a real app, you wouldn't return the user_id like this without proper auth
    return jsonify({'message': 'User registered successfully', 'user_id': user_id, 'role': role}), 201

@app.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    user_record = None
    for uid, u_data in users_db.items():
        if u_data['username'] == username:
            user_record = u_data
            break

    if user_record and bcrypt.checkpw(password.encode('utf-8'), user_record['password_hash']):
        # In a real app, you would generate and return a JWT token here
        return jsonify({'message': 'Login successful', 'username': username, 'role': user_record['role']}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

if __name__ == '__main__':
    # For development only, in production use a proper WSGI server
    app.run(debug=True, port=5000)

# --- Placeholder Payment Integration Endpoints ---

@app.route('/api/create-payment-intent', methods=['POST'])
def create_payment_intent():
    # This endpoint would be called by the frontend after obtaining a payment method ID from Stripe/Gateway
    data = request.get_json()
    # payment_method_id = data.get('payment_method_id')
    # order_id = data.get('order_id')

    # 1. Retrieve order details from your database using order_id
    # 2. Calculate the amount
    # 3. Create a PaymentIntent with the payment gateway (e.g., Stripe)
    #    intent = stripe.PaymentIntent.create(
    //        amount=amount_in_cents,
    //        currency='usd',
    //        payment_method=payment_method_id,
    //        confirm=True, // or handle confirmation client-side
    //        metadata={'order_id': order_id}
    //    )
    # 4. Handle the intent status (e.g., requires_action, succeeded)
    # 5. If successful, update your database (order payment_status = 'paid')
    # 6. Return a response to the client

    # Placeholder response:
    return jsonify({'message': 'Placeholder for creating payment intent. Real integration needed.', 'success': True}), 200

@app.route('/api/stripe-webhook', methods=['POST'])
def stripe_webhook():
    # This endpoint would be configured in your Stripe dashboard to receive events
    # payload = request.data
    # sig_header = request.headers.get('Stripe-Signature')
    # event = None

    # try:
    #     event = stripe.Webhook.construct_event(
    #         payload, sig_header, YOUR_STRIPE_WEBHOOK_SECRET
    #     )
    # except ValueError as e:
    #     # Invalid payload
    #     return jsonify({'error': str(e)}), 400
    # except stripe.error.SignatureVerificationError as e:
    #     # Invalid signature
    #     return jsonify({'error': str(e)}), 400

    # # Handle the event
    # if event.type == 'payment_intent.succeeded':
    #     payment_intent = event.data.object
    #     order_id = payment_intent.metadata.get('order_id')
    #     # Update order status in your database to 'paid' for the given order_id
    #     print(f"PaymentIntent succeeded for order_id: {order_id}")
    # elif event.type == 'payment_intent.payment_failed':
    #     payment_intent = event.data.object
    #     order_id = payment_intent.metadata.get('order_id')
    #     # Update order status in your database to 'failed' or log the failure
    #     print(f"PaymentIntent failed for order_id: {order_id}")
    # # ... handle other event types

    return jsonify({'message': 'Placeholder for Stripe webhook. Real integration needed.', 'received': True}), 200

# --- Placeholder Order History Endpoint ---

# Mock database for orders and order items (replace with actual database interaction)
mock_orders_db = {
    1: {'order_id': 1, 'customer_id': 101, 'order_date': '2023-10-26T10:00:00Z', 'total_amount': 25.50, 'status': 'Delivered', 'payment_status': 'Paid',
        'items': [
            {'item_name': 'Pizza', 'quantity': 1, 'price_at_purchase': 15.00},
            {'item_name': 'Coke', 'quantity': 2, 'price_at_purchase': 2.75}
        ]},
    2: {'order_id': 2, 'customer_id': 101, 'order_date': '2023-10-28T12:30:00Z', 'total_amount': 12.00, 'status': 'Pending', 'payment_status': 'Pending',
        'items': [
            {'item_name': 'Sandwich', 'quantity': 1, 'price_at_purchase': 8.00},
            {'item_name': 'Water', 'quantity': 1, 'price_at_purchase': 4.00}
        ]}
}
mock_food_items_db = { # Simplified version for name lookup if needed
    1: {'name': 'Pizza', 'price': 15.00},
    2: {'name': 'Coke', 'price': 2.75},
    3: {'name': 'Sandwich', 'price': 8.00},
    4: {'name': 'Water', 'price': 4.00}
}


@app.route('/api/orders/history', methods=['GET'])
def get_order_history():
    # In a real application, you would:
    # 1. Authenticate the user (e.g., via JWT token) to get their customer_id.
    # 2. Query the database for orders belonging to that customer_id.
    # For now, we'll assume a mock customer_id and return mock data.

    assumed_customer_id = 101 # Mock customer ID
    customer_orders = [order for order in mock_orders_db.values() if order['customer_id'] == assumed_customer_id]

    if not customer_orders:
        return jsonify({'message': 'No order history found for this customer.'}), 404

    return jsonify(customer_orders), 200
