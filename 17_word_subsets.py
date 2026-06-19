from collections import Counter

def word_subsets(words1, words2):
    required = Counter()

    for word in words2:
        count = Counter(word)

        for char in count:
            required[char] = max(required[char], count[char])

    result = []

    for word in words1:
        count = Counter(word)
        valid = True

        for char in required:
            if count[char] < required[char]:
                valid = False
                break

        if valid:
            result.append(word)

    return result

print(word_subsets(["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"]))
print(word_subsets(["amazon", "apple", "facebook", "google", "leetcode"], ["l", "e"]))
