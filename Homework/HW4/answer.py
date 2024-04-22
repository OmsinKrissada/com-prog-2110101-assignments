# HW4_Social_Media_Data

# ให้ลบบรรทัด pass แล้วแทนด้วยโค้ดของนิสิต


def social_media_data(file_in):
    the_dict = {}
    with open(file_in, encoding="utf-8") as f:
        f.readline()
        for line in f.readlines():
            s = line.strip().split(",")
            if len(s) != 13:
                print(len(s))
            s = [x.strip() for x in s]
            the_dict[s[0]] = [s[1], s[5], int(s[6]), int(s[7]), s[8], s[9]]
    return the_dict


def is_stopword(word):
    with open("stopwords.txt", encoding="utf-8") as f:
        sts = [x.strip() for x in f.read().strip().split(",")]
    return sanitize(word.lower()) in sts


def count_words_from_text(word_count_dict, text):
    for w in text.split(" "):
        tw = sanitize(w).lower()
        if tw == "" or is_stopword(tw):
            continue
        if tw in word_count_dict:
            word_count_dict[tw] += 1
        else:
            word_count_dict[tw] = 1
    return word_count_dict


def count_words_from_data_dict(data_dict, year, country, platform):
    # { Post_ID: [Text, Platform, Retweets, Likes, Country, Year] }
    total_word = {}
    for v in data_dict.values():
        if (
            (platform == "all" or v[1] == platform)
            and (country == "all" or v[4] == country)
            and (year == "all" or v[5] == year)
        ):
            total_word = count_words_from_text(total_word, v[0])
    return total_word


def top_k_words(word_count_dict, k):
    filtered = []
    sorted_list = sorted([(-v, k) for k, v in word_count_dict.items()])

    for count, word in sorted_list:
        # first condition for possible compare skip
        if k < len(word_count_dict) and count > sorted_list[k - 1][0]:
            break
        filtered.append(word)
    return filtered


print(
    top_k_words(
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
        1,
    )
)


def count_word_summary(file_in, file_out, k, year, country, platform):
    counts = count_words_from_data_dict(
        social_media_data(file_in), year, country, platform
    )
    words = top_k_words(counts, k)
    with open(file_out, "w", encoding="utf-8") as f:
        if len(words) == 0:
            f.write("No data")
        else:
            for w in words:
                f.write(f"{w}:{counts[w]}\n")


# Write your functions here ONLY (If any)


def sanitize(text: str):
    chars = ".,:;?()[]\"'{}-/|_!"
    # text.strip(chars)
    # return text.strip(chars)
    result = ""
    for c in text:
        if c not in chars:
            result += c
    return result


# print(is_stopword("this?"))

# print(
#     len(
#         count_words_from_data_dict(
#             social_media_data("social_media_data.csv"), "all", "all", "all"
#         )
#     )
# )

# print(count_words_from_text({}, "The new movie release is a must-watch!  "))

# print(
#     top_k_words(
#         {"market": 1, "aroma": 1},
#         5,
#     )
# )

# count_word_summary("social_media_data.csv", "summary.txt", 5, "2023", "Thailand", "all")
