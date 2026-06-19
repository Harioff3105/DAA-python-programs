def can_segment(s, dictionary):
    words = set(dictionary)
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break

    return dp[len(s)]

dictionary = ["i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"]

for s in ["ilike", "ilikesamsung"]:
    if can_segment(s, dictionary):
        print(s, ": Yes")
    else:
        print(s, ": No")
