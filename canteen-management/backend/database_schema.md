# Database Schema for Canteen Management System

## Users Table (`users`)

-   `user_id` (Primary Key, Auto-incrementing Integer)
-   `username` (Unique, String)
-   `password_hash` (String - store hashed passwords)
-   `role` (String - e.g., 'customer', 'admin')
-   `created_at` (Timestamp)

## Food Items Table (`food_items`)

-   `item_id` (Primary Key, Auto-incrementing Integer)
-   `name` (String)
-   `description` (Text)
-   `price` (Decimal)
-   `image_url` (String - optional)
-   `stock_quantity` (Integer)
-   `created_at` (Timestamp)
-   `updated_at` (Timestamp)

## Orders Table (`orders`)

-   `order_id` (Primary Key, Auto-incrementing Integer)
-   `customer_id` (Foreign Key referencing `users.user_id`)
-   `order_date` (Timestamp)
-   `total_amount` (Decimal)
-   `status` (String - e.g., 'pending', 'confirmed', 'delivered', 'cancelled')
-   `payment_status` (String - e.g., 'pending', 'paid', 'failed')
-   `created_at` (Timestamp)

## Order Items Table (`order_items`)

-   `order_item_id` (Primary Key, Auto-incrementing Integer)
-   `order_id` (Foreign Key referencing `orders.order_id`)
-   `item_id` (Foreign Key referencing `food_items.item_id`)
-   `quantity` (Integer)
-   `price_at_purchase` (Decimal - to store the price of the item at the time of purchase)
