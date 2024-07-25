#Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) 
#of any student(s) having the second lowest grade.
#Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    lowest = second_lowest = float('inf')
    second_lowest_names = lowest_names = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        if score < lowest:
            second_lowest = lowest
            second_lowest_names = lowest_names[:]
            lowest = score
            lowest_names = [name]
        elif score == lowest:
            lowest_names.append(name)
        elif lowest < score < second_lowest:
            second_lowest = score
            second_lowest_names = [name]
        elif score == second_lowest:
            second_lowest_names.append(name)
    
    second_lowest_names.sort()
        
    for name in second_lowest_names:
        print(name)
