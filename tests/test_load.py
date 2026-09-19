from src.load import get_engine

def test_database_connection():
    engine = get_engine()

    with engine.connect() as connection:
        result = connection.exec_driver_sql("SELECT 1")
        assert result.scalar() == 1