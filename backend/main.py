from datetime import date, datetime
from enum import Enum
from typing import Optional

from fastapi import FastAPI, HTTPException, Query, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, field_validator


class RepairStatus(str, Enum):
    received = "Received"
    diagnosing = "Diagnosing"
    waiting_for_parts = "Waiting for parts"
    repairing = "Repairing"
    ready_for_pickup = "Ready for pickup"
    completed = "Completed"
    cancelled = "Cancelled"


class StatusHistoryEntry(BaseModel):
    status: RepairStatus
    date: str


class RepairOrderInput(BaseModel):
    customerName: str = Field(min_length=1)
    phone: str = ""
    deviceType: str = "Laptop"
    deviceModel: str = Field(min_length=1)
    problem: str = Field(min_length=1)
    receivedDate: date
    status: RepairStatus
    technician: str = ""
    estimatedCost: Optional[float] = Field(default=None, ge=0)
    notes: str = ""

    @field_validator("customerName", "deviceModel", "problem")
    @classmethod
    def required_text_must_not_be_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("This field cannot be empty")
        return value.strip()


class RepairOrder(RepairOrderInput):
    id: str
    history: list[StatusHistoryEntry]


class StatusChange(BaseModel):
    status: RepairStatus


class SparePartInput(BaseModel):
    name: str = Field(min_length=1)
    stock: int = Field(ge=0)
    unitPrice: float = Field(ge=0)

    @field_validator("name")
    @classmethod
    def name_must_not_be_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Part name cannot be empty")
        return value.strip()


class SparePart(SparePartInput):
    id: str


class PublicOrderStatus(BaseModel):
    id: str
    deviceModel: str
    receivedDate: date
    status: RepairStatus
    message: str


PUBLIC_MESSAGES = {
    "Received": "Your device has been received and is waiting for a technician.",
    "Diagnosing": "A technician is checking your device to find the problem.",
    "Waiting for parts": "The repair is waiting for the required part to arrive.",
    "Repairing": "The repair is in progress.",
    "Ready for pickup": "Your device is ready. Please contact the shop to arrange pickup.",
    "Completed": "This repair has been completed.",
    "Cancelled": "This repair order has been cancelled.",
}


def now_text() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def starter_orders() -> list[dict]:
    return [
        {"id": "FF-1001", "customerName": "Aigerim S.", "phone": "+7 701 123 45 67", "deviceType": "Laptop", "deviceModel": "ASUS TUF Gaming A15", "problem": "Laptop gets too hot and shuts down.", "receivedDate": "2026-10-20", "status": "Diagnosing", "technician": "Arman", "estimatedCost": 12000, "notes": "Check cooling system and clean fans.", "history": [{"status": "Received", "date": "2026-10-20 10:20"}, {"status": "Diagnosing", "date": "2026-10-21 09:15"}]},
        {"id": "FF-1002", "customerName": "Daniyar K.", "phone": "+7 707 555 11 22", "deviceType": "Laptop", "deviceModel": "MacBook Air M1", "problem": "Battery does not hold charge for long.", "receivedDate": "2026-10-19", "status": "Waiting for parts", "technician": "Nursultan", "estimatedCost": 28000, "notes": "Waiting for a compatible battery.", "history": [{"status": "Received", "date": "2026-10-19 12:05"}, {"status": "Waiting for parts", "date": "2026-10-20 11:30"}]},
        {"id": "FF-1003", "customerName": "Madina A.", "phone": "+7 747 444 22 00", "deviceType": "Phone", "deviceModel": "iPhone 13", "problem": "Charging port is loose.", "receivedDate": "2026-10-18", "status": "Ready for pickup", "technician": "Arman", "estimatedCost": 18000, "notes": "Repair completed. Customer can pick it up.", "history": [{"status": "Received", "date": "2026-10-18 11:10"}, {"status": "Ready for pickup", "date": "2026-10-20 17:00"}]},
        {"id": "FF-1004", "customerName": "Timur B.", "phone": "+7 775 222 33 44", "deviceType": "Laptop", "deviceModel": "Lenovo IdeaPad 5", "problem": "Screen flickers when moving the lid.", "receivedDate": "2026-10-17", "status": "Repairing", "technician": "Nursultan", "estimatedCost": 22000, "notes": "Checking the display cable.", "history": [{"status": "Received", "date": "2026-10-17 09:40"}, {"status": "Repairing", "date": "2026-10-18 10:00"}]},
        {"id": "FF-1005", "customerName": "Alina R.", "phone": "+7 702 888 77 66", "deviceType": "Tablet", "deviceModel": "iPad 9th Gen", "problem": "Glass is cracked.", "receivedDate": "2026-10-15", "status": "Completed", "technician": "Arman", "estimatedCost": 35000, "notes": "Picked up by the customer.", "history": [{"status": "Received", "date": "2026-10-15 16:45"}, {"status": "Completed", "date": "2026-10-17 13:00"}]},
    ]


def starter_parts() -> list[dict]:
    return [
        {"id": "PT-01", "name": "Laptop fan", "stock": 6, "unitPrice": 4500},
        {"id": "PT-02", "name": "USB-C charging port", "stock": 10, "unitPrice": 2200},
        {"id": "PT-03", "name": "Thermal paste", "stock": 14, "unitPrice": 1800},
        {"id": "PT-04", "name": "Laptop battery", "stock": 2, "unitPrice": 18000},
    ]


orders = starter_orders()
parts = starter_parts()


def reset_data() -> None:
    global orders, parts
    orders = starter_orders()
    parts = starter_parts()


def next_number(items: list[dict], prefix: str, start: int = 0) -> int:
    values = [int(item["id"].replace(prefix, "")) for item in items if item["id"].startswith(prefix)]
    return max([start, *values]) + 1


app = FastAPI(title="FixFlow API", version="1.0.0", description="A simple repair shop API.")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "PATCH", "OPTIONS"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/orders", response_model=list[RepairOrder])
def list_repair_orders(search: str = Query(default=""), status_filter: Optional[RepairStatus] = Query(default=None, alias="status")) -> list[dict]:
    term = search.strip().lower()
    result = orders
    if term:
        result = [order for order in result if term in order["id"].lower() or term in order["customerName"].lower() or term in order["deviceModel"].lower()]
    if status_filter:
        result = [order for order in result if order["status"] == status_filter.value]
    return result


@app.post("/orders", response_model=RepairOrder, status_code=status.HTTP_201_CREATED)
def create_repair_order(payload: RepairOrderInput) -> dict:
    data = payload.model_dump(mode="json")
    data["id"] = f"FF-{next_number(orders, 'FF-', 1000)}"
    data["history"] = [{"status": data["status"], "date": now_text()}]
    orders.insert(0, data)
    return data


@app.get("/orders/{order_id}", response_model=RepairOrder)
def get_repair_order(order_id: str) -> dict:
    order = next((item for item in orders if item["id"] == order_id), None)
    if order is None:
        raise HTTPException(status_code=404, detail="Repair order not found")
    return order


@app.patch("/orders/{order_id}", response_model=RepairOrder)
def edit_repair_order(order_id: str, payload: RepairOrderInput) -> dict:
    order = next((item for item in orders if item["id"] == order_id), None)
    if order is None:
        raise HTTPException(status_code=404, detail="Repair order not found")
    data = payload.model_dump(mode="json")
    old_status = order["status"]
    order.update(data)
    if old_status != order["status"]:
        order["history"].append({"status": order["status"], "date": now_text()})
    return order


@app.patch("/orders/{order_id}/status", response_model=RepairOrder)
def change_repair_status(order_id: str, payload: StatusChange) -> dict:
    order = next((item for item in orders if item["id"] == order_id), None)
    if order is None:
        raise HTTPException(status_code=404, detail="Repair order not found")
    order["status"] = payload.status.value
    order["history"].append({"status": payload.status.value, "date": now_text()})
    return order


@app.get("/parts", response_model=list[SparePart])
def list_spare_parts() -> list[dict]:
    return parts


@app.post("/parts", response_model=SparePart, status_code=status.HTTP_201_CREATED)
def create_spare_part(payload: SparePartInput) -> dict:
    data = payload.model_dump()
    data["id"] = f"PT-{next_number(parts, 'PT-'):02d}"
    parts.append(data)
    return data


@app.patch("/parts/{part_id}", response_model=SparePart)
def edit_spare_part(part_id: str, payload: SparePartInput) -> dict:
    part = next((item for item in parts if item["id"] == part_id), None)
    if part is None:
        raise HTTPException(status_code=404, detail="Spare part not found")
    part.update(payload.model_dump())
    return part


@app.get("/public/orders/{order_id}", response_model=PublicOrderStatus)
def get_public_order_status(order_id: str) -> dict:
    order = next((item for item in orders if item["id"].lower() == order_id.lower()), None)
    if order is None:
        raise HTTPException(status_code=404, detail="Repair order not found")
    return {
        "id": order["id"],
        "deviceModel": order["deviceModel"],
        "receivedDate": order["receivedDate"],
        "status": order["status"],
        "message": PUBLIC_MESSAGES[order["status"]],
    }
