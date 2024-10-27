from idlelib.iomenu import encoding
from io import open
from os import path
from timeit import timeit
from search.boyer_moore_search import boyer_moore_search
from search.kmp_search import kmp_search
from search.rabin_karp_search import rabin_karp_search
import json

if __name__ == "__main__":
    result = []

    with open(path.abspath("files/text1.txt"), mode="r", encoding="windows-1251") as f1:
        text1 = f1.read()
    with open(path.abspath("files/text2.txt"), mode="r", encoding="utf-8") as f1:
        text2 = f1.read()

    search_phrases = ["простий приклад завдання", "популярних мов програмування", "І москаля нема, немає москаля"]
    # search_phrases = ["приклад", "космодесант", "Правильно підібраний алгоритм пошуку, що враховує ці обмеження відіграє визначальну роль у продуктивності системи"]

    for phrase in search_phrases:
        bm_time1 = timeit(lambda: boyer_moore_search(text1, phrase), number=1)
        bm_time2 = timeit(lambda: boyer_moore_search(text2, phrase), number=1)

        kmp_time1 = timeit(lambda: kmp_search(text1, phrase), number=1)
        kmp_time2 = timeit(lambda: kmp_search(text2, phrase), number=1)

        rk_time1 = timeit(lambda: rabin_karp_search(text1, phrase), number=1)
        rk_time2 = timeit(lambda: rabin_karp_search(text2, phrase), number=1)

        result.append({'phrase': phrase, 'times': [{'text': 'text1', 'BM': bm_time1, 'KMP': kmp_time1, 'RK': rk_time1},
                                                   {'text': 'text2', 'BM': bm_time2, 'KMP': kmp_time2,
                                                    'RK': rk_time2}]})

    print(json.dumps(result, indent=4))