import pytest

from src.pipeline import transform_orders


def test_transform_orders_calculates_total_amount():
    orders = [
        {
            "order_id": "1",
            "customer_id": "101",
            "quantity": "2",
            "unit_price": "10.50",
        }
    ]

    result = transform_orders(orders)

    assert result == [
        {
            "order_id": 1,
            "customer_id": 101,
            "quantity": 2,
            "unit_price": 10.5,
            "total_amount": 21.0,
        }
    ]


def test_transform_orders_handles_multiple_orders():
    orders = [
        {
            "order_id": "1",
            "customer_id": "101",
            "quantity": "2",
            "unit_price": "10.50",
        },
        {
            "order_id": "2",
            "customer_id": "102",
            "quantity": "1",
            "unit_price": "25.00",
        },
    ]

    result = transform_orders(orders)

    assert len(result) == 2
    assert result[0]["total_amount"] == 21.0
    assert result[1]["total_amount"] == 25.0
    

def test_transform_orders_rejects_non_positive_quantity():
    orders = [
        {
            "order_id": "1",
            "customer_id": "101",
            "quantity": "0",
            "unit_price": "10.50",
        }
    ]

    with pytest.raises(ValueError, match="quantity must be greater than 0"):
        transform_orders(orders)