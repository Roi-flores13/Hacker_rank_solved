def string_validator(s):
    if s.isalnum():
        return print(True)
    else: 
        return print(False)
    if s.isalpha():
        return print(True)
    else:
        return print(False)
    if s.isupper():
        return print(True)
    else:
        return print(False)
    if s.islower():
        return print(True)
    else:
        return print(False)
if __name__ == '__main__':
    s = input()
    print(string_validator(s))