print("отчислен" if any(map(lambda x: x < 3, map(int, input().split()))) else "учится")
