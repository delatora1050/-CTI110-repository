# I was supposed to put a comment here
# My Last Name
# CTI-110
# P3HW1 - Debugging
# De La Torre, Alestacia
# 20220321
#

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60

    # TO DO: define the rest of the scores

    score = float(input('Enter grade: '))

    if score >= A_score:
        print('Your grade is: A')
    else:
        if score > B_score:
            print('Your grade is: B')
        else:
            if score >= C_score:
                print('Your grade is: C')
            else:
                if score < D_score:
                    print('Your grade is: F')  # TO DO: finish this
                else:
                    print('Your grade is : D')


# program start
main()
