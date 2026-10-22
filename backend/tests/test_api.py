from fastapi.testclient import TestClient

from main import app, reset_data

client = TestClient(app)


def setup_function():
    reset_data()


def valid_order(**updates):
    data = {
        "customerName": "Test Customer",
        "phone": "+7 777 111 22 33",
        "deviceType": "Laptop",
        "deviceModel": "Test Notebook",
        "problem": "Does not turn on",
        "receivedDate": "2026-10-22",
        "status": "Received",
        "technician": "Arman",
        "estimatedCost": 10000,
        "notes": "Test note",
    }
    data.update(updates)
    return data


def test_health_and_list_orders():
    assert client.get("/health").json() == {"status": "ok"}
    response = client.get("/orders")
    assert response.status_code == 200
    assert len(response.json()) == 5
    assert response.json()[0]["id"] == "FF-1001"


def test_create_order_assigns_id_and_history():
    response = client.post("/orders", json=valid_order())
    assert response.status_code == 201
    assert response.json()["id"] == "FF-1006"
    assert response.json()["history"][0]["status"] == "Received"


def test_missing_required_text_is_rejected():
    response = client.post("/orders", json=valid_order(customerName="  "))
    assert response.status_code == 422


def test_negative_estimated_cost_is_rejected():
    response = client.post("/orders", json=valid_order(estimatedCost=-1))
    assert response.status_code == 422


def test_update_order_records_status_change():
    response = client.patch("/orders/FF-1001", json=valid_order(status="Repairing", deviceModel="Updated Laptop"))
    assert response.status_code == 200
    data = response.json()
    assert data["deviceModel"] == "Updated Laptop"
    assert data["status"] == "Repairing"
    assert data["history"][-1]["status"] == "Repairing"


def test_unknown_order_is_404():
    assert client.get("/orders/FF-9999").status_code == 404
    assert client.patch("/orders/FF-9999", json=valid_order()).status_code == 404


def test_spare_part_can_be_created_and_updated():
    created = client.post("/parts", json={"name": "HDMI cable", "stock": 3, "unitPrice": 1200})
    assert created.status_code == 201
    assert created.json()["id"] == "PT-05"
    updated = client.patch("/parts/PT-05", json={"name": "HDMI cable", "stock": 5, "unitPrice": 1250})
    assert updated.status_code == 200
    assert updated.json()["stock"] == 5


def test_negative_part_stock_is_rejected():
    response = client.post("/parts", json={"name": "Bad part", "stock": -1, "unitPrice": 100})
    assert response.status_code == 422


def test_public_status_does_not_return_private_fields():
    response = client.get("/public/orders/FF-1003")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "Ready for pickup"
    assert "notes" not in data
    assert "phone" not in data


def test_search_and_status_filter_can_be_combined():
    response = client.get("/orders", params={"search": "iPhone", "status": "Ready for pickup"})
    assert len(response.json()) == 1
    assert response.json()[0]["id"] == "FF-1003"
