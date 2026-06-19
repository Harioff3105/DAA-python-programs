class WordFilter:
    def __init__(self, words):
        self.map = {}

        for index, word in enumerate(words):
            for i in range(len(word) + 1):
                prefix = word[:i]
                for j in range(len(word) + 1):
                    suffix = word[j:]
                    self.map[(prefix, suffix)] = index

    def f(self, pref, suff):
        return self.map.get((pref, suff), -1)

wordFilter = WordFilter(["apple"])
print(wordFilter.f("a", "e"))
