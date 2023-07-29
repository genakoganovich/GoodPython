banknotes = [64, 32, 16, 8, 4, 2, 1]
n = int(input())
for note in banknotes:
    while n >= note:
        n -= note
        print(note, end=' ')
