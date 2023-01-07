def gradingStudents(grades):
    # Write your code here
    result = []
    for i in range(len(grades)):

        if(grades[i] >= 38):
            if grades[i] % 5 >= 3:
                result.append(grades[i] + (5-grades[i] % 5))
            else:
                result.append(grades[i])
        else:
            result.append(grades[i])
    
    return result