#Find the name of the second lowest score in an nested list.
    #The list contains [name, score].
    #If there are two or more repetions of the second lowest grade, you must present the names in alphabetical order    
lowest = 100    
names_scores = []
for _ in range(int(input())):
    name = input()
    score = float(input())

    if score < lowest:
        lowest = score

    combined = [name, score]
    names_scores.append(combined)

names_scores.sort(key= lambda x: x[1])

clean_names_scores = []
for combination in names_scores:
    if combination[1] != lowest:
        clean_names_scores.append(combination)

new_lowest = clean_names_scores[0][1]

last_cleaning = []

for new in clean_names_scores:
    if new[1] == new_lowest:
        last_cleaning.append(new)

last_cleaning.sort(key= lambda x: x[0])

for i in last_cleaning:
    print(i[0])