if __name__ == '__main__':
    #Find the second highest score in an array of scores.
    def second_highest_score():
        n = int(input())
        arr = list(map(int, input().split()))
        new_s = sorted(arr, reverse=True)
        no_max = []
        highest_max = max(new_s)
        for numb in new_s:
            if numb != highest_max:
                no_max.append(numb)
        second_highest = max(no_max)
        print(second_highest)
     
    