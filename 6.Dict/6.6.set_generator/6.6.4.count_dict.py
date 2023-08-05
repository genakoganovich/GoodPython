words = list(map(str.lower, input().split()))
d = {w: words.count(w) for w in words}
print(d['и'] if 'и' in d else 0)
