cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
cities_gen = (cities[i % len(cities)] for i in range(1000001))
list(map(lambda _: print(next(cities_gen), end=' '), range(20)))
