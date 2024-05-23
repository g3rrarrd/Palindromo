from Game import management 

class main:

    ma = management.management()

    word = input("Digite una palabra: \n")

    if(ma.validator(word)):
        print("\nEs palindromo!")
    else:
        print("\nNo es un palindromo!")