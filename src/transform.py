import pandas as pd
from pathlib import Path

#clean CUSTOMERS
def clean_customers(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["email"] = (
        df["email"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    df["first_name"] = (
        df["first_name"]
        .astype(str)
        .str.strip()
    )

    df["last_name"] = (
        df["last_name"]
        .astype(str)
        .str.strip()
    )

    df["created_at"] = pd.to_datetime(
        df["created_at"],
        errors = "coerce"
    )

    df = df.drop_duplicates(
        subset=["customer_id"]
    )

    df = df.dropna(
        subset=[
            "customer_id",
            "email"
        ]
    )

    return df

#clean PRODUCTS
def clean_products(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["product_name"]=(
        df["product_name"]
        .astype(str)
        .str.strip()
    )

    df["category"] = (
        df["category"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    df["price"] = pd.to_numeric(
        df["price"],
        errors = "coerce"
    )

    df["stock"] = pd.to_numeric(
        df["stock"],
        errors = "coerce"
    )

    df["created_at"] = pd.to_datetime(
        df["created_at"],
        errors = "coerce"
    )

    df = df[df["price"] >= 0 ]
    df = df[df["stock"] >= 0]

    df = df.drop_duplicates(
        subset = ["product_id"]
    )

    return df

#clean ORDERS

def clean_orders(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["order_date"] = pd.to_datetime(
        df["order_date"],
        errors = "coerce"
    )

    df["total_amount"] = pd.to_numeric(
        df["total_amount"],
        errors = "coerce"
    )

    df["status"] = (
        df["status"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    valid_statuses = (
        "pending",
        "completed",
        "canceld",
        "refunded"
    )

    df = df[
        df["status"].isin(valid_statuses)
    ]

    df =df[
        df["total_amount"] >=0
    ]

    df = df.drop_duplicates(
        subset=["order_id"]
    )

    df = df.dropna(
        subset = [
            "order_id",
            "customer_id",
            "order_date"
        ]
    )

    return df

#clean ORDER ITEMS
def clean_order_items (df : pd.DataFrame) -> pd.DataFrame :

    df = df.copy()

    df["quantity"] = pd.to_numeric(
        df["quantity"],
        errors = "coerce"
    )

    df["unit_price"] = pd.to_numeric(
        df["unit_price"],
        errors = "coerce"
    )

    df = df[
        (df["quantity"] > 0)&
        (df["unit_price"] > 0)
    ]

    df = df.drop_duplicates(
        subset=["order_item_id"]
    )

    return df

#clean PAYMENTS
def clean_payments(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df ["payment_date"] = pd.to_datetime(
        df["payment_date"],
        errors = "coerce"
    ) 

    df ["amount"] = pd.to_numeric(
        df["amount"],
        errors = "coerce"
    )

    df ["payment_method"] = (
        df["payment_method"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    df ["payment_status"] = (
        df["payment_status"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    df = df[df["amount"] >= 0 ]

    df = df.drop_duplicates(
        subset=["payment_id"]
    )

    return df

#all Data
def transform_all(data: dict[str, pd.DataFrame]) -> dict[str, pd.DataFrame]:
    transformed = {
        "customers" : clean_customers(data["customers"]),
        "products" : clean_products(data["products"]),
        "orders" : clean_orders(data["orders"]),
        "order_items" : clean_order_items(data["order_items"]),
        "payments" : clean_payments(data["payments"]),
    }

    return transformed

#processed data
PROCESSED_DATA_PATH = Path(
    "data/processed"
)

def save_processed (
        data: dict[str, pd.DataFrame]
):
    PROCESSED_DATA_PATH.mkdir(
        parents=True,
        exist_ok=True
    )

    for name, df in data.items():
        file_path = (
            PROCESSED_DATA_PATH
            / f"{name}.csv"
        )

        df.to_csv(
            file_path,
            index=False)


       