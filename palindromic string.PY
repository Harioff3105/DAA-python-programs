def first_palindrome(words):
    for word in words:
        if word == word[::-1]:
            return word
    return ""

# Example 1
words = ["abc", "car", "ada", "racecar", "cool"]
print("Output:", first_palindrome(words))