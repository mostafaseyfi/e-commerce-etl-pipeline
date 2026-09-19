from fastapi import FastAPI

app = FastAPI(
    title="E-commerce Fake API",
    version="1.0.0"
)


customers = [
    {
        "customer_id": 1,
        "first_name": "Ali",
        "last_name": "Ahmadi",
        "email": "ALI@example.com",
        "country": "Iran",
        "created_at": "2026-08-01"
    },
    {
        "customer_id": 2,
        "first_name": "Sara",
        "last_name": "Mohammadi",
        "email": "sara@example.com",
        "country": "Iran",
        "created_at": "2026-08-02"
    }
]


products = [
    {
        "product_id": 1,
        "product_name": "Laptop",
        "category": "Electronics",
        "price": 1200.50,
        "stock": 20,
        "created_at": "2026-08-01"
    },
    {
        "product_id": 2,
        "product_name": "Mouse",
        "category": "Electronics",
        "price": 25.99,
        "stock": 100,
        "created_at": "2026-08-01"
    }
]


orders = [
    {
        "order_id": 1001,
        "customer_id": 1,
        "order_date": "2026-08-10",
        "status": "completed",
        "total_amount": 1226.49
    }
]


order_items = [
    {
        "order_item_id": 1,
        "order_id": 1001,
        "product_id": 1,
        "quantity": 1,
        "unit_price": 1200.50
    },
    {
        "order_item_id": 2,
        "order_id": 1001,
        "product_id": 2,
        "quantity": 1,
        "unit_price": 25.99
    }
]


payments = [
    {
        "payment_id": 1,
        "order_id": 1001,
        "payment_date": "2026-08-10",
        "amount": 1226.49,
        "payment_method": "credit_card",
        "payment_status": "paid"
    }
]


@app.get("/")
def root():
    return {
        "message": "E-commerce Fake API is running"
    }


@app.get("/customers")
def get_customers():
    return customers


@app.get("/products")
def get_products():
    return products


@app.get("/orders")
def get_orders():
    return orders


@app.get("/order_items")
def get_order_items():
    return order_items


@app.get("/payments")
def get_payments():
    return payments