# ⭐⭐⭐⭐⭐ 5 estrellas

def createXmasTree(height: int, ornament: str) -> str:
    tree = []
    
    for i in range(height):
        spaces = '_' * (height - i - 1)
        ornaments = ornament * (2 * i + 1)
        tree.append(f'{spaces}{ornaments}{spaces}')
    
    for _ in range(2):
        tree.append('_' * (height - 1) + '#' + '_' * (height - 1))
    
    return '\n'.join(tree)