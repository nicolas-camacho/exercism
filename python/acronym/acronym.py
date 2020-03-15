def abbreviate(words):
    return ''.join(x for x in words.replace("'", "").title() if x.isupper())
