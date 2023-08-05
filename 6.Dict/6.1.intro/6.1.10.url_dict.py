import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
d = dict()
for url in lst_in:
    if url not in d:
        d[url] = f'HTML-страница для адреса {url}'
        print(d[url])
    else:
        print(f'Взято из кэша: {d[url]}')
