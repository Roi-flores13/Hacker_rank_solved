if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    average = round(sum(student_marks[query_name]) / len(student_marks[query_name]), 2)
    average = str(average)
    
    #This is not necessary, this part of the code is only implemented for output requirements for hacker rank.
    #The average is correctly computed, this part only adds an extra zero if the float only has 1 decimal
    if len(average) == 4:
        average = average + "0"  
    elif len(average.split(".")[1]) == 1:
        average = average + "0"
    print(average)