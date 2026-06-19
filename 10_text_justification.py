def full_justify(words, maxWidth):
    result = []
    i = 0

    while i < len(words):
        line_length = len(words[i])
        j = i + 1

        while j < len(words) and line_length + 1 + len(words[j]) <= maxWidth:
            line_length += 1 + len(words[j])
            j += 1

        line_words = words[i:j]
        spaces_needed = maxWidth - sum(len(word) for word in line_words)

        if j == len(words) or len(line_words) == 1:
            line = " ".join(line_words)
            line += " " * (maxWidth - len(line))
        else:
            gaps = len(line_words) - 1
            spaces_each = spaces_needed // gaps
            extra_spaces = spaces_needed % gaps

            line = ""
            for k in range(gaps):
                line += line_words[k]
                line += " " * (spaces_each + (1 if k < extra_spaces else 0))
            line += line_words[-1]

        result.append(line)
        i = j

    return result

print(full_justify(["This", "is", "an", "example", "of", "text", "justification."], 16))
print(full_justify(["What","must","be","acknowledgment","shall","be"], 16))
