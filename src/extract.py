import requests
import json
import pandas as pd

from pathlib import Path


API_URL = "http://127.0.0.1:8000"

RAW_DATA_PATH = Path("data/raw")


def extract_endpoint(endpoint: str):

    url = f"{API_URL}/{endpoint}"

    response = requests.get(url)

    response.raise_for_status()

    return response.json()


def save_raw_data(
    data,
    file_name: str
):

    RAW_DATA_PATH.mkdir(
        parents=True,
        exist_ok=True
    )

    file_path = (
        RAW_DATA_PATH / file_name
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=2,
            ensure_ascii=False
        )


def extract_all():

    customers = extract_endpoint(
        "customers"
    )

    products = extract_endpoint(
        "products"
    )

    orders = extract_endpoint(
        "orders"
    )

    order_items = extract_endpoint(
        "order_items"
    )

    payments = extract_endpoint(
        "payments"
    )

    save_raw_data(
        customers,
        "customers.json"
    )

    save_raw_data(
        products,
        "products.json"
    )

    save_raw_data(
        orders,
        "orders.json"
    )

    save_raw_data(
        order_items,
        "order_items.json"
    )

    save_raw_data(
        payments,
        "payments.json"
    )

    return {
        "customers": pd.DataFrame(customers),
        "products": pd.DataFrame(products),
        "orders": pd.DataFrame(orders),
        "order_items": pd.DataFrame(order_items),
        "payments": pd.DataFrame(payments)
    }