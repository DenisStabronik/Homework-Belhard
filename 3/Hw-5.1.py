def concat(*strings, reversed=False):
    strings = list(strings)
    if reversed == True:
        strings = [s for s in strings[::-1]]
    concat_strings = "".join(strings)
    print(concat_strings)
    return concat_strings
concat('Hello', ' ', 'World',reversed=True)



