d = dict(s.split('=') for s in input().split())
for key in d:
  d[key] = int(d[key])
print(*sorted(d.items()))