def mutate_string(string, position, character):
    first_half = string[:position]
    second_half = string[position+1:]
    new_str = first_half + character + second_half
    return new_str

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)