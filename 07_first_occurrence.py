def str_str(haystack, needle):
    if needle == "":
        return 0

    n = len(haystack)
    m = len(needle)

    for i in range(n - m + 1):
        if haystack[i:i + m] == needle:
            return i

    return -1

print(str_str("sadbutsad", "sad"))
print(str_str("leetcode", "leeto"))
