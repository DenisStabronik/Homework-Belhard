def inspect(function):
    def basic_function(*args: str, **kwargs: bool):
        print(f'Args : {args}')
        print(f'Kwargs : {kwargs}')
        retvalue = function(*args, **kwargs)
        print(f"Retvalue : {retvalue}")
        return retvalue
    return basic_function
@inspect
def concat(*strings, reversed=False):
    strings = list(strings)
    if reversed == True:
        strings = [s for s in strings[::-1]]
    concat_strings = "".join(strings)
    print(concat_strings)
    return concat_strings
concat('Hello', ' ', 'World',reversed=True)