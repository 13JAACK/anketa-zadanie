def chastota(filename):
    result = {}

    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
    words = text.lower().split()
    for word in words:
        word = word.strip(".,!?;:")
        if word:
            result[word] = result.get(word, 0) + 1
    return result