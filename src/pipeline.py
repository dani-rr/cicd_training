import csv
from pathlib import Path


def load_orders(path: str | Path) -> list[dict]:
    with open(path, newline="") as file:
        return list(csv.DictReader(file))


def transform_orders(orders: list[dict]) -> list[dict]:
    transformed = []

    for order in orders:
        quantity = int(order["quantity"])
        unit_price = float(order["unit_price"])

        if quantity <= 0:
            raise ValueError("quantity must be greater than 0")

        transformed.append(
            {
                "order_id": int(order["order_id"]),
                "customer_id": int(order["customer_id"]),
                "quantity": quantity,
                "unit_price": unit_price,
                "total_amount": quantity * unit_price,
            }
        )

    return transformed


def main() -> None:
    orders = load_orders("data/orders.csv")
    transformed_orders = transform_orders(orders)

    for order in transformed_orders:
        print(order)


if __name__ == "__main__":
    main()