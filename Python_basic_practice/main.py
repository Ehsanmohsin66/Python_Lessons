# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from math import *


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_shape():
    print("   /|")
    print("  / |")
    print(" /  |")
    print("/___|")


def print_by_variable(Name,Age):
    print('Candidate name is '+Name+' and age is '+Age)


def analyse_string(str_input):
    print('String has ' + str(len(str_input)) + ' letters')
    if str_input.isupper():
        print('String is in upper')
    if str_input.index('M') == 0:
        print('String starts with letter M')


def manipulate_numbers_calculator(first_num,second_num,third_num):
    print('Max input number is '+str(max(first_num, second_num, third_num)))
    print('Square root of sum of squares of 3 numbers '+str(sqrt(pow(first_num, 2)+pow(second_num, 2)+pow(third_num, 2))))


def get_input():
    first_num = input('Enter first num:')
    second_num = input('Enter second num:')
    third_num = input('Enter third num:')
    return float(first_num), float(second_num), float(third_num)


def mad_lib_game():
    Color = input('Enter a Color:')
    Plural_noun = input('Enter a Plural Noun:')
    Celebrity = input('Enter a Celebrity:')

    print('Roses are '+Color)
    print(Plural_noun + ' are Blue')
    print('i love ' + Celebrity)


def list_manipulation(list_inp):
    list_out=[]
    for i in range(1, len(list_inp)+1):
        list_out.append(list_inp[0-i])
    return list_out


def guessing_game(keyword,attempts):
    guess_attempt=0
    while guess_attempt < attempts:
        key_guess=input('Enter the guess:')
        if key_guess == keyword:
            print('You won Congratulations')
            break
        else:
            print('Try one more time!')
        guess_attempt = guess_attempt+1
    if guess_attempt >= attempts:
        print('Sorry! you lost. Better luck next time')


def print2d_list(list2d):
    for i in range(len(list2d)):
        for j in range(len(list2d[i])):
            print(list2d[i][j])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Hello World')
    print_shape()
    print_by_variable('Mohsin', '34')
    analyse_string('MOHSIN')
    first, second, third= get_input()
    manipulate_numbers_calculator(first, second, third)
    mad_lib_game()
    list_old=['Red','Orange','Yellow','Green','Blue','Indigo','Violet']
    new_list=list_manipulation(list_old)
    print(new_list)
    guessing_game('Monopoly', 3)   #Guess word monoploy in 3 attempts
    list_test = [[1, 2, 3], [5, 'n'], [0], []]
    print2d_list(list_test)

