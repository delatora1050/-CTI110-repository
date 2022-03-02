# CTI-110
# P2HW2 - Score Avg
# De La Torre, Alestacia
# 20220302
#

#First you have to ask the user to input numbers for 7 scores.
user_score1 = float(input('Enter score #1: '))
user_score2 = float(input('Enter score #2: '))
user_score3 = float(input('Enter score #3: '))
user_score4 = float(input('Enter score #4: '))
user_score5 = float(input('Enter score #5: '))
user_score6 = float(input('Enter score #6: '))
user_score7 = float(input('Enter score #7: '))

#give space between user input and the result output
print('\n')


#Then we must put together the score that were inputed into the list
score_list = [user_score1, user_score2, user_score3, user_score4, user_score5, user_score6, user_score7]


#Next we must find the lowest score from the list (processing)
lowest_score = min(score_list)


# We must find the lowest and remove it from the list(processing)
score_list.remove(lowest_score)


# The average of inputed number omitting the lowest score(processing)
score_average = sum(score_list) / len(score_list)




# The output of the processing and results. Format to two decimal points if needed.
print('-------------------Results-------------------')
print('Lowest Score: ',lowest_score )
print('Modified List:', score_list)
print('Scores Average: ', f'{score_average:.2f}')
print('---------------------------------------------')