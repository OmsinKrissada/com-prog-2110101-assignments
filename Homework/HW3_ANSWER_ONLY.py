def generate_random_sequence(a, b, n, seed):
    import random

    random.seed(seed)
    return [random.randint(a, b) for i in range(n)]


def all_values_in_list(a, b, data):
    remaining = [x for x in range(a, b + 1)]
    for n in data:
        if n in remaining:
            remaining.remove(n)
    return len(remaining) == 0


def get_shortest_sequence_range(a, b, sequence):
    uniques = []
    result = []
    for n in sequence:
        if a <= n and n <= b:
            if n not in uniques:
                uniques.append(n)
            result.append(n)
        if len(uniques) == b - a + 1:
            return result


def check_all_occurrence(value, n, data):
    count = 0
    for num in data:
        if num == value:
            count += 1
    return count >= n


def generate_shortest_sequence_from_a2b(a, b, seed):
    import random

    random.seed(seed)
    uniques = []
    result = []
    while len(uniques) < b - a + 1:
        rand = random.randint(a, b)
        if rand not in uniques:
            uniques.append(rand)
        result.append(rand)
    return result


def get_unique_sequence(sequence):
    uniques = []
    result = []
    for n in sequence:
        if n not in uniques:
            uniques.append(n)
        result.append(n)
    return uniques


def generate_course_hc_scales(seed):
    import random

    even = []
    odd = []
    for n in get_unique_sequence(generate_shortest_sequence_from_a2b(1, 18, seed)):
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)
    return odd + even


def holes_sorted_by_hc_scales(hc_scales):
    return [hc_scales.index(i) + 1 for i in range(1, 19)]


import unittest


class TestHW3(unittest.TestCase):

    @unittest.expectedFailure
    def test_import_random(self):
        self.assertIsNotNone(random.random())

    def test_generate_random_sequence(self):
        test_cases = [
            {"args": [2, 5, 10, 2566], "expected": [2, 5, 3, 4, 5, 4, 4, 2, 5, 2]},
            {
                "args": [2, 5, 20, 2566],
                "expected": [
                    2,
                    5,
                    3,
                    4,
                    5,
                    4,
                    4,
                    2,
                    5,
                    2,
                    3,
                    5,
                    4,
                    4,
                    4,
                    2,
                    3,
                    2,
                    4,
                    5,
                ],
            },
            {"args": [2, 6, 10, 2566], "expected": [2, 5, 3, 4, 5, 4, 4, 2, 5, 2]},
            {
                "args": [2, 6, 20, 2566],
                "expected": [
                    2,
                    5,
                    3,
                    4,
                    5,
                    4,
                    4,
                    2,
                    5,
                    2,
                    6,
                    6,
                    3,
                    5,
                    4,
                    4,
                    6,
                    4,
                    6,
                    2,
                ],
            },
            {"args": [1, 9, 10, 2566], "expected": [2, 8, 4, 6, 8, 5, 6, 1, 8, 2]},
            {
                "args": [1, 18, 10, 2566],
                "expected": [4, 16, 7, 11, 16, 9, 11, 1, 16, 3],
            },
            {"args": [2, 5, 10, 2567], "expected": [4, 4, 4, 2, 5, 3, 5, 2, 5, 2]},
            {"args": [2, 6, 10, 2567], "expected": [4, 4, 4, 2, 5, 3, 5, 6, 2, 6]},
            {"args": [1, 9, 10, 2567], "expected": [6, 6, 6, 1, 8, 3, 8, 2, 9, 8]},
            {
                "args": [1, 18, 10, 2567],
                "expected": [12, 11, 12, 1, 15, 5, 15, 3, 18, 15],
            },
        ]
        for i, test_case in enumerate(test_cases):
            with self.subTest(i=i):
                a, b, n, seed = test_case["args"]
                result = generate_random_sequence(a, b, n, seed)
                self.assertEqual(result, test_case["expected"])

    def test_all_values_in_list(self):
        test_cases = [
            {"args": [2, 5, [2, 5, 3]], "expected": False},
            {"args": [2, 5, [2, 5, 3, 4]], "expected": True},
            {"args": [2, 5, [2, 8, 4, 6, 8, 5, 6, 1, 8, 2, 9, 9]], "expected": False},
            {"args": [2, 5, [2, 8, 4, 6, 8, 5, 6, 1, 8, 2, 9, 9, 3]], "expected": True},
        ]
        for i, test_case in enumerate(test_cases):
            with self.subTest(i=i):
                a, b, data = test_case["args"]
                self.assertEqual(all_values_in_list(a, b, data), test_case["expected"])

    def test_get_shortest_sequence_range(self):
        test_cases = [
            {
                "args": [
                    2,
                    5,
                    [2, 5, 3, 4, 5, 4, 4, 2, 5, 2, 6, 6, 3, 5, 4, 4, 6, 4, 6, 2],
                ],
                "expected": [2, 5, 3, 4],
            },
            {
                "args": [
                    2,
                    6,
                    [2, 5, 3, 4, 5, 4, 4, 2, 5, 2, 6, 6, 3, 5, 4, 4, 6, 4, 6, 2],
                ],
                "expected": [2, 5, 3, 4, 5, 4, 4, 2, 5, 2, 6],
            },
            {
                "args": [
                    2,
                    5,
                    [2, 8, 4, 6, 8, 5, 6, 1, 8, 2, 9, 9, 3, 8, 6, 5, 9, 6, 2, 3],
                ],
                "expected": [2, 4, 5, 2, 3],
            },
            {
                "args": [
                    2,
                    6,
                    [2, 8, 4, 6, 8, 5, 6, 1, 8, 2, 9, 9, 3, 8, 6, 5, 9, 6, 2, 3],
                ],
                "expected": [2, 4, 6, 5, 6, 2, 3],
            },
            {
                "args": [
                    2,
                    5,
                    [4, 4, 4, 2, 5, 3, 5, 6, 2, 6, 5, 6, 6, 2, 6, 4, 2, 3, 2, 4],
                ],
                "expected": [4, 4, 4, 2, 5, 3],
            },
            {
                "args": [
                    2,
                    6,
                    [4, 4, 4, 2, 5, 3, 5, 6, 2, 6, 5, 6, 6, 2, 6, 4, 2, 3, 2, 4],
                ],
                "expected": [4, 4, 4, 2, 5, 3, 5, 6],
            },
            {
                "args": [
                    2,
                    5,
                    [6, 6, 6, 1, 8, 3, 8, 2, 9, 8, 9, 1, 9, 5, 1, 4, 1, 5, 6, 6],
                ],
                "expected": [3, 2, 5, 4],
            },
            {
                "args": [
                    2,
                    6,
                    [6, 6, 6, 1, 8, 3, 8, 2, 9, 8, 9, 1, 9, 5, 1, 4, 1, 5, 6, 6],
                ],
                "expected": [6, 6, 6, 3, 2, 5, 4],
            },
        ]

        for i, test_case in enumerate(test_cases):
            with self.subTest(i=i):
                a, b, sequence = test_case["args"]
                self.assertEqual(
                    get_shortest_sequence_range(a, b, sequence), test_case["expected"]
                )

    def test_check_all_occurrence(self):
        test_cases = [
            {"args": [3, 1, [2, 5, 3, 4, 5, 4, 4, 2, 5, 2]], "expected": True},
            {"args": [3, 2, [2, 5, 3, 4, 5, 4, 4, 2, 5, 2]], "expected": False},
            {"args": [5, 2, [2, 5, 3, 4, 5, 4, 4, 2, 5, 2]], "expected": True},
            {"args": [5, 3, [2, 5, 3, 4, 5, 4, 4, 2, 5, 2]], "expected": True},
            {"args": [5, 4, [2, 5, 3, 4, 5, 4, 4, 2, 5, 2]], "expected": False},
        ]
        for i, test_case in enumerate(test_cases):
            with self.subTest(i=i):
                value, n, data = test_case["args"]
                self.assertEqual(
                    check_all_occurrence(value, n, data), test_case["expected"]
                )

    def test_generate_shortest_sequence_from_a2b(self):
        test_cases = [
            {"args": [2, 5, 2566], "expected": [2, 5, 3, 4]},
            {"args": [2, 5, 2567], "expected": [4, 4, 4, 2, 5, 3]},
            {"args": [2, 6, 2566], "expected": [2, 5, 3, 4, 5, 4, 4, 2, 5, 2, 6]},
            {"args": [2, 6, 2567], "expected": [4, 4, 4, 2, 5, 3, 5, 6]},
            {
                "args": [1, 9, 2566],
                "expected": [
                    2,
                    8,
                    4,
                    6,
                    8,
                    5,
                    6,
                    1,
                    8,
                    2,
                    9,
                    9,
                    3,
                    8,
                    6,
                    5,
                    9,
                    6,
                    2,
                    3,
                    2,
                    5,
                    7,
                ],
            },
        ]
        for i, test_case in enumerate(test_cases):
            with self.subTest(i=i):
                a, b, seed = test_case["args"]
                self.assertEqual(
                    generate_shortest_sequence_from_a2b(a, b, seed),
                    test_case["expected"],
                )

    def test_get_unique_sequence(self):
        test_cases = [
            {"args": [2, 5, 3, 4, 5, 4, 4, 2, 5, 2], "expected": [2, 5, 3, 4]},
            {
                "args": [5, 3, 6, 4, 3, 5, 4, 6, 3, 5, 4, 5, 6, 6, 3, 4, 6, 4, 6, 2],
                "expected": [5, 3, 6, 4, 2],
            },
            {
                "args": [6, 6, 6, 1, 8, 3, 8, 2, 9, 8, 9, 1, 9, 5, 1, 4, 1, 5, 6, 6],
                "expected": [6, 1, 8, 3, 2, 9, 5, 4],
            },
            {
                "args": generate_random_sequence(1, 18, 100, 2566),
                "expected": [
                    4,
                    16,
                    7,
                    11,
                    9,
                    1,
                    3,
                    18,
                    5,
                    12,
                    10,
                    17,
                    13,
                    8,
                    2,
                    15,
                    6,
                    14,
                ],
            },
            {
                "args": generate_random_sequence(1, 18, 100, 2567),
                "expected": [12, 11, 1, 15, 5, 3, 18, 17, 2, 9, 8, 10, 16, 7, 4, 6, 13],
            },
        ]
        for i, test_case in enumerate(test_cases):
            with self.subTest(i=i):
                self.assertEqual(
                    get_unique_sequence(test_case["args"]), test_case["expected"]
                ),

    def test_generate_course_hc_scales(self):
        test_cases = [
            {
                "args": 2566,
                "expected": [
                    7,
                    11,
                    9,
                    1,
                    3,
                    5,
                    17,
                    13,
                    15,
                    4,
                    16,
                    18,
                    12,
                    10,
                    8,
                    2,
                    6,
                    14,
                ],
            },
            {
                "args": 2567,
                "expected": [
                    11,
                    1,
                    15,
                    5,
                    3,
                    17,
                    9,
                    7,
                    13,
                    12,
                    18,
                    2,
                    8,
                    10,
                    16,
                    4,
                    6,
                    14,
                ],
            },
        ]
        for i, test_case in enumerate(test_cases):
            with self.subTest(i=i):
                self.assertEqual(
                    generate_course_hc_scales(test_case["args"]), test_case["expected"]
                )

    def test_holes_sorted_by_hc_scales(self):
        test_cases = [
            {
                "args": [17, 3, 13, 15, 5, 7, 9, 1, 11, 2, 6, 14, 16, 8, 12, 18, 4, 10],
                "expected": [
                    8,
                    10,
                    2,
                    17,
                    5,
                    11,
                    6,
                    14,
                    7,
                    18,
                    9,
                    15,
                    3,
                    12,
                    4,
                    13,
                    1,
                    16,
                ],
            },
            {
                "args": [7, 11, 9, 1, 3, 5, 17, 13, 15, 4, 16, 18, 12, 10, 8, 2, 6, 14],
                "expected": [
                    4,
                    16,
                    5,
                    10,
                    6,
                    17,
                    1,
                    15,
                    3,
                    14,
                    2,
                    13,
                    8,
                    18,
                    9,
                    11,
                    7,
                    12,
                ],
            },
            {
                "args": [11, 1, 15, 5, 3, 17, 9, 7, 13, 12, 18, 2, 8, 10, 16, 4, 6, 14],
                "expected": [
                    2,
                    12,
                    5,
                    16,
                    4,
                    17,
                    8,
                    13,
                    7,
                    14,
                    1,
                    10,
                    9,
                    18,
                    3,
                    15,
                    6,
                    11,
                ],
            },
            {
                "args": [9, 3, 5, 7, 15, 13, 1, 17, 11, 16, 4, 12, 10, 8, 18, 14, 6, 2],
                "expected": [
                    7,
                    18,
                    2,
                    11,
                    3,
                    17,
                    4,
                    14,
                    1,
                    13,
                    9,
                    12,
                    6,
                    16,
                    5,
                    10,
                    8,
                    15,
                ],
            },
        ]
        for i, test_case in enumerate(test_cases):
            with self.subTest(i=i):
                self.assertEqual(
                    holes_sorted_by_hc_scales(test_case["args"]), test_case["expected"]
                )


unittest.main(argv=[""], verbosity=2, exit=False)


# print(holes_sorted_by_hc_scales(generate_course_hc_scales(2566)))
