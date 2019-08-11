#Jacob Bourque
#August 4th, 2019
#SEC 290 30071
#Programming assignment 4

menu = """
Scoring Engine

1: Exit
2: List scores so far
3: Add a score
4: Display the highest and lowest scores
"""
score_list = [ 85.3, 85.2, 21.99 ]
done = False


while not done:
    print(menu)
    
        
    selection = input('Please enter a selection between 1 and 4: ')

    if selection == "1":
        done = True
        print('Finished! Thank you! ')

    elif selection == "2":
        print('Scores recorded so far: \n')
        for value in sorted(score_list, reverse=True):
            print('{:.2f}'.format(value))

    elif selection =="3":
        value = float(input('Please enter a score between 0 and 100: '))
        if value < 0.0:
            print('Please enter a valid score between 0 and 100 ')
        elif value > 100.0:
            print ('Please enter a valid score between 0 and 100 ')
        else:
            score_list.append(float(value))

    elif selection == "4":
        score_list.sort()
        print(' Highest is: ',score_list[len(score_list)-1], 'Lowest is: ',score_list[0])
        
    else:
        print(' {} is not a valid selection. \n Please select 1, 2, 3 or 4.'.format(selection))
    
