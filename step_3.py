def text_to_morse(x):
    """Convert the upper case letter to Morse code"""
    if (x == "J"):
        return ('The morse code for J is .---')
    elif (x == "A"):
        return ('The morse code for A is .-')
    elif (x == "K"):
        return ('The morse code for K is -.-')
    elif (x == "E"):
        return ('The morse code for E is .')
    else:
        return ('That letter is unknown')
    
#Ask the user to input an uppercase letter they wish to have translated up to 4 times
count = 1
while(count <= 4):
    input1 = input('Please enter an upper case letter to see its Morse code.')
    x = input1
    translation = text_to_morse(x)
    print(translation)
    count = count + 1




