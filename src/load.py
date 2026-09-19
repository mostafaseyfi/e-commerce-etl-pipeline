import os

import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()


def get_database_url():
    host = os.getenv("POSTGRES_HOST", "localhost")
    port = os.getenv("POSTGRES_PORT", "5433")
    database = os.getenv("POSTGRES_DB", "ecommerce")
    user = os.getenv("POSTGRES_USER", "ecommerce_user")
    password = os.getenv("POSTGRES_PASSWORD", "ecommerce_password")

    return (
        f"postgresql+psycopg2://{user}:{password}@"
        f"{host}:{port}/{database}"
    )


def get_engine():
    return create_engine(get_database_url())


def clear_tables(engine):
    with engine.begin() as connection:
        connection.execute(
            text(
                """
                TRUNCATE TABLE
                    order_items,
                    payments,
                    orders,
                    products,
                    customers
                RESTART IDENTITY CASCADE;
                """
            )
        )


def load_dataframe(
    df: pd.DataFrame,
    table_name: str,
    engine
):
    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False,
        method="multi"
    )


def load_all(data: dict[str, pd.DataFrame]):
    engine = get_engine()

    print("Clearing existing data...")
    clear_tables(engine)

    print("Loading customers...")
    load_dataframe(
        data["customers"],
        "customers",
        engine
    )

    print("Loading products...")
    load_dataframe(
        data["products"],
        "products",
        engine
    )

    print("Loading orders...")
    load_dataframe(
        data["orders"],
        "orders",
        engine
    )

    print("Loading order_items...")
    load_dataframe(
        data["order_items"],
        "order_items",
        engine
    )

    print("Loading payments...")
    load_dataframe(
        data["payments"],
        "payments",
        engine
    )

    print("All data loaded successfully.")