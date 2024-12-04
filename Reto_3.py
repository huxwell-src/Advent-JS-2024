# ⭐⭐⭐⭐ 4 estrellas

from typing import List, Dict
from collections import defaultdict

def organizeInventory(inventory: List[Dict]) -> Dict:
    result = defaultdict(lambda: defaultdict(int))
    for item in inventory:
        result[item['category']][item['name']] += item['quantity']
    return dict(result)


inventary = [
    {"name": "doll", "quantity": 5, "category": "toys"},
    {"name": "car", "quantity": 3, "category": "toys"},
    {"name": "ball", "quantity": 2, "category": "sports"},
    {"name": "car", "quantity": 2, "category": "toys"},
    {"name": "racket", "quantity": 4, "category": "sports"}
]

print(organizeInventory(inventary))