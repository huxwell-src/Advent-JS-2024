# ⭐⭐⭐⭐ 4 estrellas

from typing import List, Dict
from collections import defaultdict

def organizeInventory(inventory: List[Dict]) -> Dict:
    result = defaultdict(lambda: defaultdict(int))
    for item in inventory:
        result[item['category']][item['name']] += item['quantity']
    return dict(result)
