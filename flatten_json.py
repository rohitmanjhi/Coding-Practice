data = {
    "user": {  
        "id": 123,
        "name": "Rohit",
        "contact": {
            "email": "rohit@example.com",
            "phone": "+91-9876543210"
        }
    },
    "orders": [
        {
            "order_id": "ORD001",
            "items": [
                {"product_id": "P100", "name": "Laptop", "price": 75000},
                {"product_id": "P200", "name": "Mouse", "price": 1200}
            ],
            "status": "shipped"
        },
        {
            "order_id": "ORD002",
            "items": [
                {"product_id": "P300", "name": "Keyboard", "price": 3500}
            ],
            "status": "processing"
        }
    ],
    "metadata": {
        "signup_date": "2023-02-15",
        "is_premium": True
    }
}

def flatten_json(json_obj, parent_key='', sep='_'):
    items = {}
    for key, value in json_obj.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.update(flatten_json(value, new_key, sep=sep))
        elif isinstance(value, list):
            for i, item in enumerate(value):
                if isinstance(item, dict):
                    items.update(flatten_json(item, f"{new_key}{sep}{i}", sep=sep))
                else:
                    items[f"{new_key}{sep}{i}"] = item
        else:
            items[new_key] = value
    return items

print(flatten_json(data))

