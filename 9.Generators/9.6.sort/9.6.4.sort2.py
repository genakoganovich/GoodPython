sorted_up = sorted(map(int, input().split()))
sorted_down = sorted(map(int, input().split()), reverse=True)
print(*list(map(lambda x: x[0] + x[1], zip(sorted_up, sorted_down))))
