import random

# 1から99までの乱数を生成
numbers = [random.randint(1, 99) for _ in range(10)]

# 生成された乱数を表示
print("生成された乱数:", numbers)

# 乱数を小さい順に並べ替え
numbers.sort()

# 並べ替えた乱数を表示
print("並べ替えた乱数:", numbers)
