def count_substring(string, sub_string):
    counter = 0
    for i in range(len(string)):
        if sub_string == string[i:len(sub_string)+i]:
            counter  += 1
    return counter

if __name__ == '__main__':
    string = input()
    substring = input()
    print(count_substring(string, substring))