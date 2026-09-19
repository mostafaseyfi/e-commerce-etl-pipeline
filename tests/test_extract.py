from src.extract import extract_endpoint

def test_extract_customers():
    data = extract_endpoint("customers")

    assert isinstance(data, list)
    assert len(data) > 0
    assert "customer_id" in data[0]
    assert "email" in data[0]