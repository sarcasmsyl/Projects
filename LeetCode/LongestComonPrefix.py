def find_matching_letters(words):
    if not words:
        return ""
    matching_letters = ""
    
    for i in range(min(len(word) for word in words)):
        first_letter = words[0][i]
        if all(word[i] == first_letter for word in words):
            matching_letters += first_letter
        else:
            pass
    
    return matching_letters

# Example usage
words1 = ["apple", "apricot", "apron", "ape"]
words2 = ["banana", "band", "banner", "bacon"]
words3 = ["cherry", "charm", "chart", "cheese"]
words4 = ["dog", "cat", "fish"]

matching_letters1 = find_matching_letters(words1)
matching_letters2 = find_matching_letters(words2)
matching_letters3 = find_matching_letters(words3)
matching_letters4 = find_matching_letters(words4)

print(f"Matching letters in words1: '{matching_letters1}'")
print(f"Matching letters in words2: '{matching_letters2}'")
print(f"Matching letters in words3: '{matching_letters3}'")
print(f"Matching letters in words4: '{matching_letters4}'")