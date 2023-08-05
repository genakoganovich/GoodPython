setA = set(map(int, input().split()))
setB = set(map(int, input().split()))
s = setA ^ setB
print(*sorted(s))
