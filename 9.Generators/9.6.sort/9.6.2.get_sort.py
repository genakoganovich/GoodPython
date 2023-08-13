d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}


def get_sort(d):
    return [item[1] for item in sorted(d.items(), reverse=True)]


print(get_sort(d))
