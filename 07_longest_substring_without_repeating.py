def length_of_longest_substring(s):
    seen = {}
    left = 0
    answer = 0

    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1

        seen[char] = right
        answer = max(answer, right - left + 1)

    return answer

print(length_of_longest_substring("abcabcbb"))
print(length_of_longest_substring("bbbbb"))
print(length_of_longest_substring("pwwkew"))
