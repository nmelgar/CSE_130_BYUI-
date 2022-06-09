def display_grade(grade):  
    ''' Break a grade such as "A+" into "A" and "+" '''
    letter = grade[0]
    sign   = grade[1]

    print("Your letter grade is", letter,
          "and your sign is", sign)

b = 88
display_grade(b)