#Jacob Bourque
#8-11-2019
#Programming assignment week 5
#SEC 290.30071


menu = """
===========================
Frequently Asked Questions
===========================

0: Exit
1: List FAQ's
2: Add FAQ
3: Delete FAQ

"""

FAQ = {}

done = False

while not done:
    print(menu)
    choice = input('Please enter your choice: ')

    if choice == "0":
        done = True
        print('Exiting session')

    elif choice == "1":
        for item in FAQ:
            print('\nQuestion: ', item)
            print('Answer: ', FAQ[item])
            print()

    elif choice =="2":
        while True:
            question = input('\nPlease enter the question: ')
            if question in FAQ:
                print('\n{} is already in the notebook. \nPlease rephrase the question.'.format(question))
                
            else:    
                answer = input('\nPlease enter the answer: ')
                FAQ[question] = answer
                print('\nHas been added to the notebook. ')
                break

    elif choice == "3":
        item = input('Please enter the question to be deleted: ')
        if item in FAQ:
            del(FAQ[item])
            print('{} has been removed from the FAQs.'.format(item))
        else:
            print('Could not find {} in the FAQ.\nNo changes made.'.format(item))

    else:
        print(' {} is not a valid choice. \n Please select 0, 1, 2 or 3.'.format(choice))
                

        

