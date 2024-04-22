filename = "answer.py"
print(f"Checking answer from {filename}")
exec(open(filename, encoding="utf8").read())

import unittest


def is_function_defined(func_name):
    return func_name in globals()


def skip_if_not_implemented(func_name):
    def decorator(test_func):
        if not is_function_defined(func_name):
            return unittest.skip(
                '"' + func_name + '()" is not defined or not implemented'
            )(test_func)
        return test_func

    return decorator


class TestHW4(unittest.TestCase):

    @skip_if_not_implemented("social_media_data")
    def test_1_social_media_data(self):
        test_case = {"args": "social_media_data.csv", "expected": "1_1.txt"}
        result = social_media_data(test_case["args"])
        fsol = open(test_case["expected"], "r", encoding="utf-8")
        self.assertEqual(str(sorted(result.items())), "".join(fsol.readlines()))
        fsol.close()

        test_case = {"args": "empty_data.csv", "expected": {}}
        result = social_media_data(test_case["args"])
        self.assertEqual(result, test_case["expected"])

    @skip_if_not_implemented("is_stopword")
    def test_2_is_stopword(self):
        test_cases = [
            {"args": "Happy", "expected": False},
            {"args": "birthDay", "expected": False},
            {"args": "on", "expected": True},
            {"args": "whiCH", "expected": True},
            {"args": "Into", "expected": True},
            {"args": "After", "expected": True},
            {"args": "AFTER", "expected": True},
            {"args": "afTEr", "expected": True},
            {"args": "can't", "expected": False},
            {"args": "cant", "expected": False},
        ]
        for i, test_case in enumerate(test_cases):
            with self.subTest(i=i):
                result = is_stopword(test_case["args"])
                self.assertEqual(result, test_case["expected"])

    @skip_if_not_implemented("count_words_from_text")
    def test_3_count_words_from_text(self):
        test_cases = [
            {
                "args": [{"aroma": 1, "market": 1}, "Hello today! #Happy"],
                "expected": {
                    "aroma": 1,
                    "market": 1,
                    "hello": 1,
                    "today": 1,
                    "#happy": 1,
                },
            },
            {
                "args": [
                    {"aroma": 1, "market": 1},
                    "Exploring the local market today, can't wait to share with everyone!",
                ],
                "expected": {
                    "aroma": 1,
                    "market": 2,
                    "exploring": 1,
                    "local": 1,
                    "today": 1,
                    "cant": 1,
                    "wait": 1,
                    "share": 1,
                    "everyone": 1,
                },
            },
            {
                "args": [
                    {"aroma": 1, "market": 1},
                    "LoVe Aroma THeRapy!! LoVed it LoVe it #AROMA.",
                ],
                "expected": {
                    "aroma": 2,
                    "market": 1,
                    "love": 2,
                    "therapy": 1,
                    "loved": 1,
                    "#aroma": 1,
                },
            },
            {
                "args": [
                    {},
                    'Mary has "A little Lamb", LiTTLE Lamb, MARY has a Little cat!! #lamb #cat',
                ],
                "expected": {
                    "mary": 2,
                    "little": 3,
                    "lamb": 2,
                    "cat": 1,
                    "#lamb": 1,
                    "#cat": 1,
                },
            },
            {
                "args": [{}, "Mary has A lot of Lambs, a little lamb."],
                "expected": {"mary": 1, "lot": 1, "lambs": 1, "little": 1, "lamb": 1},
            },
            {
                "args": [
                    {"mary": 2, "little": 3},
                    "Twinkle twinkle 'little' star..... How I wonder what you are.",
                ],
                "expected": {
                    "mary": 2,
                    "little": 4,
                    "twinkle": 2,
                    "star": 1,
                    "wonder": 1,
                },
            },
        ]
        for i, test_case in enumerate(test_cases):
            with self.subTest(i=i):
                d, t = test_case["args"]
                result = count_words_from_text(d, t)
                self.assertEqual(result, test_case["expected"])

    @skip_if_not_implemented("count_words_from_data_dict")
    def test_4_count_words_from_data_dict(self):
        test_cases = [
            {"args": ["all", "all", "all"], "expected": "4_1.txt"},
            {"args": ["2023", "USA", "Facebook"], "expected": "4_2.txt"},
            {
                "args": ["all", "Thailand", "all"],
                "expected": {
                    "heart": 1,
                    "bustling": 1,
                    "market": 1,
                    "street": 1,
                    "food": 1,
                    "connoisseur": 1,
                    "indulges": 1,
                    "culinary": 1,
                    "adventure": 1,
                    "savoring": 1,
                    "diverse": 1,
                    "flavors": 1,
                    "aromas": 1,
                    "#culinaryadventure": 1,
                    "#streetfooddelights": 1,
                },
            },
            {"args": ["2023", "Thailand", "all"], "expected": {}},
            {
                "args": ["2020", "Japan", "Twitter"],
                "expected": {
                    "avoiding": 1,
                    "shards": 1,
                    "shattered": 1,
                    "dreams": 1,
                    "walking": 1,
                    "tightrope": 1,
                    "resilience": 1,
                    "#resilience": 1,
                    "#tightropewalk": 1,
                },
            },
            {"args": ["2020", "japan", "twitter"], "expected": {}},
        ]
        data_dict = social_media_data("social_media_data.csv")
        for i, test_case in enumerate(test_cases):
            with self.subTest(i=i):
                y, c, p = test_case["args"]
                result = count_words_from_data_dict(data_dict, y, c, p)
                if i < 2:
                    fsol = open(test_case["expected"], "r", encoding="utf-8")
                    self.assertEqual(
                        str(sorted(result.items())), "".join(fsol.readlines())
                    )
                    fsol.close()
                else:
                    self.assertEqual(result, test_case["expected"])

    @skip_if_not_implemented("top_k_words")
    def test_5_top_k_words(self):
        test_cases = [
            {
                "args": [
                    {
                        "new": 43,
                        "like": 27,
                        "day": 26,
                        "feeling": 26,
                        "dreams": 25,
                        "heart": 24,
                        "laughter": 24,
                        "joy": 23,
                        "night": 23,
                        "life": 22,
                    },
                    5,
                ],
                "expected": ["new", "like", "day", "feeling", "dreams"],
            },
            {
                "args": [
                    {
                        "new": 43,
                        "like": 27,
                        "day": 26,
                        "feeling": 26,
                        "dreams": 25,
                        "heart": 24,
                        "laughter": 24,
                        "joy": 23,
                        "night": 23,
                        "life": 22,
                    },
                    3,
                ],
                "expected": ["new", "like", "day", "feeling"],
            },
            {
                "args": [
                    {
                        "heart": 1,
                        "food": 1,
                        "diverse": 1,
                        "flavors": 1,
                        "aromas": 1,
                        "#culinaryadventure": 1,
                        "#streetfooddelights": 1,
                    },
                    5,
                ],
                "expected": [
                    "#culinaryadventure",
                    "#streetfooddelights",
                    "aromas",
                    "diverse",
                    "flavors",
                    "food",
                    "heart",
                ],
            },
            {
                "args": [
                    {
                        "heart": 1,
                        "food": 1,
                        "diverse": 1,
                        "flavors": 1,
                        "aromas": 1,
                        "#culinaryadventure": 1,
                        "#streetfooddelights": 1,
                    },
                    3,
                ],
                "expected": [
                    "#culinaryadventure",
                    "#streetfooddelights",
                    "aromas",
                    "diverse",
                    "flavors",
                    "food",
                    "heart",
                ],
            },
            {"args": [{"market": 1, "aroma": 1}, 5], "expected": ["aroma", "market"]},
            {"args": [{"market": 1, "aroma": 1}, 3], "expected": ["aroma", "market"]},
            {
                "args": [
                    {
                        "aroma": 2,
                        "market": 1,
                        "love": 2,
                        "therapy": 1,
                        "loved": 1,
                        "#aroma": 1,
                    },
                    5,
                ],
                "expected": ["aroma", "love", "#aroma", "loved", "market", "therapy"],
            },
            {
                "args": [
                    {
                        "aroma": 2,
                        "market": 1,
                        "love": 2,
                        "therapy": 1,
                        "loved": 1,
                        "#aroma": 1,
                    },
                    3,
                ],
                "expected": ["aroma", "love", "#aroma", "loved", "market", "therapy"],
            },
        ]
        for i, test_case in enumerate(test_cases):
            with self.subTest(i=i):
                d, k = test_case["args"]
                result = top_k_words(d, k)
                self.assertEqual(result, test_case["expected"])

    @skip_if_not_implemented("count_word_summary")
    def test_6_count_word_summary(self):
        test_cases = [
            {
                "args": [
                    "social_media_data.csv",
                    "summary.txt",
                    5,
                    "all",
                    "all",
                    "all",
                ],
                "expected": "new:43\nlike:27\nday:26\nfeeling:26\ndreams:25",
            },
            {
                "args": [
                    "social_media_data.csv",
                    "summary2.txt",
                    3,
                    "all",
                    "all",
                    "all",
                ],
                "expected": "new:43\nlike:27\nday:26\nfeeling:26",
            },
            {
                "args": [
                    "social_media_data.csv",
                    "summary.txt",
                    5,
                    "2023",
                    "USA",
                    "Facebook",
                ],
                "expected": "art:4\nevery:3\nexperience:3\nexploring:3\nlocal:3\nlove:3",
            },
            {
                "args": [
                    "social_media_data.csv",
                    "summary2.txt",
                    3,
                    "2023",
                    "USA",
                    "Facebook",
                ],
                "expected": "art:4\nevery:3\nexperience:3\nexploring:3\nlocal:3\nlove:3",
            },
            {
                "args": [
                    "social_media_data.csv",
                    "summary.txt",
                    5,
                    "all",
                    "Thailand",
                    "all",
                ],
                "expected": "#culinaryadventure:1\n#streetfooddelights:1\nadventure:1\naromas:1\nbustling:1\nconnoisseur:1\nculinary:1\ndiverse:1\nflavors:1\nfood:1\nheart:1\nindulges:1\nmarket:1\nsavoring:1\nstreet:1",
            },
            {
                "args": [
                    "social_media_data.csv",
                    "summary1.txt",
                    3,
                    "2023",
                    "Thailand",
                    "all",
                ],
                "expected": "No data",
            },
            {
                "args": [
                    "social_media_data.csv",
                    "summary2.txt",
                    5,
                    "2023",
                    "UK",
                    "Instagram",
                ],
                "expected": "new:7\nadventure:4\nfriends:4\nart:3\nday:3\nmagic:3\nweekend:3\nwine:3\nyears:3",
            },
            {
                "args": [
                    "social_media_data.csv",
                    "summary3.txt",
                    3,
                    "all",
                    "India",
                    "all",
                ],
                "expected": "day:5\nnew:5\npainting:5",
            },
            {
                "args": [
                    "social_media_data.csv",
                    "summary4.txt",
                    5,
                    "all",
                    "India",
                    "all",
                ],
                "expected": "day:5\nnew:5\npainting:5\n#gratitude:4\n#hopeful:4\ndreams:4\nhopeful:4\nlife:4\noptimism:4",
            },
        ]
        for i, test_case in enumerate(test_cases):
            with self.subTest(i=i):
                file_in, file_out, k, year, country, platform = test_case["args"]
                count_word_summary(file_in, file_out, k, year, country, platform)
                f = open(file_out, "r", encoding="utf-8")
                self.assertEqual("".join(f.readlines()).strip(), test_case["expected"])
                f.close()


unittest.main(argv=[""], verbosity=2, exit=False)
