gpas = [4.3, 2.8, 3.7]

def average_gpa(gpas):  
    ''' Find the average GPA from the list '''

    # Add them up.
    sum = 0
    for gpa in gpas:
        sum += gpa

     # gpas list shold have more than 0 elements
    assert len(gpas) > 0

    # Compute the average and return.
    average = sum / len(gpas)
    print(average)
    return average


print(average_gpa)