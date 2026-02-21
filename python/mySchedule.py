blocks = {
1: "English",
2: "Algebra",
3: "History",
4: "Chemistry",
5: "Latin",
6: "Research",
7: "Dialogue",
8: "Art",
9: "CSE",
10: "Specials",
}

schedule = {
"Monday": [1, 10, 2 ,6],
"Tuesday": [2, 6, 1, 4, 5, 3],
"Wednesday": [9, 1, 5, 8, 2],
"Thursday": [8, 3, 4, 2, 7],
"Friday": [5, 4, 3, 9, 1],
}
for day in schedule:
    print(day + ":")
    for block in schedule[day]:
        print ("- " + blocks[block])
    print()    
