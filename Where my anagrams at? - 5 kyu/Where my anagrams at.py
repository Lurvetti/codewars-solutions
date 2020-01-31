def anagrams(word, words):
    new = [w for w in words if set(w) == set(word) and len(w) == len(word)]
    return new