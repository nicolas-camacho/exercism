def is_isogram(string):
    mod_string = ''.join(l.lower() for l in string if l.isalpha())
    return len(mod_string) == len(set(mod_string))
