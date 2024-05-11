from typing import List, Any

result: list[Any] = []


def divider(a, b):

    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a/b


data = {10: 2, 2: 5, 4: 18, 0: [], 15: 8, }
for key in data:
    res: Any = divider(key, data[key])
    result.append(res)

    print(result)
