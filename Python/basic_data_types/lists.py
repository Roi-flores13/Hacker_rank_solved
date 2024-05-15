if __name__ == '__main__':
    N = int(input())
    initial = []
    
    for command in range(N):
        operation = input().lower().strip().split(" ")
        
        if len(operation) == 1:
            
            if operation[0] == "print":
                print(initial)
                
            elif operation[0] == "pop":
                initial.pop()
                
            elif operation[0] == "reverse":
                initial.reverse()
                
            elif operation[0] == "sort":
                initial.sort()
                
        elif len(operation) == 2:
            
            if operation[0] == "remove":
                initial.remove(int(operation[1]))
            elif operation[0] == "append":
                initial.append(int(operation[1]))
                
        elif len(operation) == 3:
            initial.insert(int(operation[1]), int(operation[2]))