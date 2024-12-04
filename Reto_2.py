# ⭐⭐⭐⭐⭐ 5 estrellas

from typing import List

def createFrame(names: List[str]) -> str:
    a = max(len(name) for name in names)
    border = '*' * (a + 4)
    return border + '\n'.join([f'* {name:{a}} *' for name in names]) + '\n' + border