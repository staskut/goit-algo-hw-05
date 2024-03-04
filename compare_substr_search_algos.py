import timeit

from substr_search_algos import kmp_search, boyer_moore_search, rabin_karp_search


with open('стаття 1.txt', 'r',encoding="cp1251") as file:
    article1 = file.read()

with open('стаття 2.txt', 'r',encoding="cp1251") as file:
    article2 = file.read()


existing_substring_art1 = "Інтерполяційний пошук використовується для пошуку елементів у відсортованому масиві."
non_existing_substring_art1 = "Інтерполяційний пошук не використовується для пошуку елементів у відсортованому масиві."

existing_substring_art2 = "Об’єктом дослідження є процес зберігання даних рекомендаційної системи."
non_existing_substring_art2 = "Об’єктом дослідження не є процес зберігання даних рекомендаційної системи."

case1 = {"text": article1, "existing_pattern": existing_substring_art1, "non_existing_pattern": non_existing_substring_art1}
case2 = {"text": article2, "existing_pattern": existing_substring_art2, "non_existing_pattern": non_existing_substring_art2}

def measure_time(func, text, pattern):
    setup = f'from __main__ import {func.__name__}'
    stmt = f'{func.__name__}(text, pattern)'
    return timeit.timeit(stmt, setup=setup, globals={"text": text, "pattern": pattern}, number=100)


for case in [case1, case2]:
    print("-"*20)
    for f in [kmp_search, boyer_moore_search, rabin_karp_search]:
        for pat in ["existing_pattern", "non_existing_pattern"]:
            time = measure_time(f, case["text"], case[pat])
            print(f"{f.__name__:<{20}} | {pat:<{20}} | {time:<{20}}")
