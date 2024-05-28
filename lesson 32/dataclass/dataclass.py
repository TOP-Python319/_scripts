from dataclasses import dataclass


# class InventoryItem:
#     def __init__(self, name, price=10, quantity=1):
#         self.name = name
#         self.price = price
#         self.quantity = quantity


@dataclass
class InventoryItem:
    name: str
    price: float = 10
    quantity: int = 1


desk = InventoryItem('Стол', 1000, 10)
pen = InventoryItem('Ручка')
monitor = InventoryItem('Монитор', 5000)


print(desk)
print(pen)
print(monitor)