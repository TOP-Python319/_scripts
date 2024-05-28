from dataclasses import dataclass
from typing import List


@dataclass
class InventoryItem:
    name: str
    price: float
    quantity: int


@dataclass
class ProgramStaff:
    items: List[InventoryItem]


desk = InventoryItem('Стол', 1000, 10)
pen = InventoryItem('Ручка', 5, 100000)
monitor = InventoryItem('Монитор', 5000, 3)


staff = ProgramStaff([desk, pen, monitor])
print(staff)


# broken_staff = ProgramStaff([1, 2, 3])
# print(broken_staff)
