import pandas as pd

from src.transform import (
    clean_customers,
    clean_products,
    clean_orders,
    clean_order_items,
    clean_payments,
)


def test_clean_customers():
    df = pd.DataFrame([
        {
            "customer_id": 1,
            "first_name": " Ali ",
            "last_name": " Ahmadi ",
            "email": " ALI@EXAMPLE.COM ",
            "country": "Iran",
            "created_at": "2026-08-01",
        }
    ])

    result = clean_customers(df)

    assert result.iloc[0]["first_name"] == "Ali"
    assert result.iloc[0]["last_name"] == "Ahmadi"
    assert result.iloc[0]["email"] == "ali@example.com"


def test_clean_products():
    df = pd.DataFrame([
        {
            "product_id": 1,
            "product_name": " Laptop ",
            "category": " Electronics ",
            "price": "1200.50",
            "stock": "20",
            "created_at": "2026-08-01",
        }
    ])

    result = clean_products(df)

    assert result.iloc[0]["product_name"] == "Laptop"
    assert result.iloc[0]["category"] == "electronics"
    assert result.iloc[0]["price"] == 1200.50
    assert result.iloc[0]["stock"] == 20


def test_clean_orders():
    df = pd.DataFrame([
        {
            "order_id": 1001,
            "customer_id": 1,
            "order_date": "2026-08-10",
            "status": " COMPLETED ",
            "total_amount": "1226.49",
        }
    ])

    result = clean_orders(df)

    assert len(result) == 1
    assert result.iloc[0]["status"] == "completed"
    assert result.iloc[0]["total_amount"] == 1226.49


def test_clean_order_items():
    df = pd.DataFrame([
        {
            "order_item_id": 1,
            "order_id": 1001,
            "product_id": 1,
            "quantity": "2",
            "unit_price": "100.50",
        }
    ])

    result = clean_order_items(df)

    assert len(result) == 1
    assert result.iloc[0]["quantity"] == 2
    assert result.iloc[0]["unit_price"] == 100.50


def test_clean_payments():
    df = pd.DataFrame([
        {
            "payment_id": 1,
            "order_id": 1001,
            "payment_date": "2026-08-10",
            "amount": "1226.49",
            "payment_method": " CREDIT_CARD ",
            "payment_status": " PAID ",
        }
    ])

    result = clean_payments(df)

    assert len(result) == 1
    assert result.iloc[0]["amount"] == 1226.49
    assert result.iloc[0]["payment_method"] == "credit_card"
    assert result.iloc[0]["payment_status"] == "paid"