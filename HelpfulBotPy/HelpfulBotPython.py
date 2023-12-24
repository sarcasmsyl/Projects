import os
import random
from Chess.images import ChessMain4 as chess
from os import startfile
from Projects.TicTacToe import TicTacToePygame2
import cv2
import numpy as np
import pandas as pd
import time
import webbrowser
import string
from random import randint
from random import choices
from random import sample


def clearscreen():
    os.system('cls')


def mainmenu():
    print('''
    
    Welcome to Helpfulbot Python
    
    What would you like to work on today?
    
    1. Notes
    2. Entertainment
    3. Toolbox
    4. Personal Notes
    5. About Helpfulbox
    6. Exit
    
    
    ''')
    mainmenuchoice = input(' ').lower()

    if mainmenuchoice == 'notes' or mainmenuchoice == '1':
        clearscreen()
        notes()
    elif mainmenuchoice == 'entertainment' or mainmenuchoice == '2':
        clearscreen()
        entertainmentmenu()
    elif mainmenuchoice == 'toolbox' or mainmenuchoice == '3':
        clearscreen()
        toolboxmenu()
    elif mainmenuchoice == 'personal notes' or mainmenuchoice == '4':
        personalnotesmenu()
    elif mainmenuchoice == 'exit' or mainmenuchoice == '6':
        print('Goodbye')
        quit()
    else:
        print(imsorry)
        input(' ')
        clearscreen()
        mainmenu()


# Where I stored my variables

imsorry = "I'm sorry I didn't understand that"
imsorrywrong = "I'm sorry that isn't the correct answer"
underconstruction = "I'm sorry this page is still under construction"
chrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

# Where I am registering webbrowser

webbrowser.register('chrome',
                    None,
                    webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))


# notes menu
def notes():
    clearscreen()
    print('''
    
    Welcome to Notes!
    
    1. Spanish
    2. Crash Course (Youtube)
    3. Finance for Everyone: Decisions
    4. Exit
    
    ''')

    noteschoice = input(' ').lower()

    if noteschoice == 'spanish' or noteschoice == '1':
        clearscreen()
        spanishmenu()
    elif noteschoice == 'crash course' or noteschoice == 'crash course youtube' or noteschoice == 'crash course (' \
                                                                                                  'youtube)' or \
            noteschoice == 'crash course yt' or noteschoice == '2':
        clearscreen()
        crashcoursemenu()
    elif noteschoice == 'exit' or noteschoice == '4':
        clearscreen()
        mainmenu()
    else:
        print(imsorry)
        input(' ')
        clearscreen()
        notes()


def crashcoursemenu():
    print('''
    Welcome to the Crash Course menu!
    What would you like to look at today?
    
    1. US History
    2. Philosophy
    3. Exit
    
    
    
    ''')

    crashcoursemenuchoice = input(' ').lower()

    if crashcoursemenuchoice == 'us history' or crashcoursemenuchoice == '1':
        clearscreen()
        crashcoursemenuhistory()
    elif crashcoursemenuchoice == 'philosophy' or crashcoursemenuchoice == '2':
        clearscreen()
        crashcoursephilosphy()
    elif crashcoursemenuchoice == 'exit' or crashcoursemenuchoice == '3':
        clearscreen()
        notes()
    else:
        print(imsorry)
        input(' ')
        clearscreen()
        crashcoursemenu()


def crashcoursemenuhistory():
    print('''
    Here are your notes on Crash Course US History.
    
    1. The Black Legend
    2. Native Americans
    3. Spaniards
    4. Exit
    
    ''')

    crashcoursemenuhistorychoice = input(' ').lower()

    if crashcoursemenuhistorychoice == 'the black legend' or crashcoursemenuhistorychoice == '1':
        clearscreen()
        crashcourseushistorytheblacklegend()
    elif crashcoursemenuhistorychoice == 'native americans' or crashcoursemenuhistorychoice == '2':
        pass
    elif crashcoursemenuhistorychoice == 'spaniards' or crashcoursemenuhistorychoice == '3':
        pass
    elif crashcoursemenuhistorychoice == 'exit' or crashcoursemenuhistorychoice == '4':
        clearscreen()
        crashcoursemenu()
    else:
        print(imsorry)
        input(' ')
        clearscreen()
        crashcoursemenuhistory()


def crashcourseushistorytheblacklegend():
    theblacklegendnotes = open('D:\Sterling\Helpfulbot\TheBlackLegend.txt', 'r')
    print(theblacklegendnotes.read())
    print("\n"
          "I am currently not programmed with any more info the subject currently, so we will have to go back to the "
          "menu, to exit these notes simply type in 1 or exit\n "
          "    ")

    crashcoursehistorytheblacklegendchoice = input(' ').lower()

    if crashcoursehistorytheblacklegendchoice == 'exit' or crashcoursehistorytheblacklegendchoice == '1':
        clearscreen()
        crashcoursemenuhistory()
    else:
        print(imsorry)
        crashcourseushistorytheblacklegend()


def crashcoursemenuphilosophy():
    print('''
    Sorry this page is still under construction
    ''')
    crashcoursemenu()


def spanishmenu():
    print('''
    
    What would you like to work on?
    
    1. Vocab
    2. Sentences
    3. Exit
    
    
    ''')

    spanishmenuchoice = input(' ').lower()

    if spanishmenuchoice == 'vocab' or spanishmenuchoice == '1':
        clearscreen()
        spanishvocabmenu()
    elif spanishmenuchoice == 'sentences' or spanishmenuchoice == '2':
        clearscreen()
        spanishsentencemenu()
    elif spanishmenuchoice == 'exit' or spanishmenuchoice == '3':
        clearscreen()
        mainmenu()
    else:
        print(imsorry)
        input('')
        clearscreen()
        spanishmenu()


def spanishvocabmenu():
    print('''
    
    Spanish Vocab Menu
    1. Vocab set 1
    2. Vocab set 2
    3. Vocab set 3
    4. Verbs
    5. Colors
    6. Numbers
    7. Months
    8. Exit
    
    
    ''')

    spanishvocabmenuchoice = input(' ').lower()

    if spanishvocabmenuchoice == 'vocab set 1' or spanishvocabmenuchoice == '1':
        clearscreen()
        spanishvocabset1v2()
    elif spanishvocabmenuchoice == 'vocab set 2' or spanishvocabmenuchoice == '2':
        spanishvocabset2()
        clearscreen()
        spanishvocabmenu()
    elif spanishvocabmenuchoice == 'vocab set 3' or spanishvocabmenuchoice == '3':
        spanishvocabset3()
        clearscreen()
        spanishvocabmenu()
    elif spanishvocabmenuchoice == 'verbs' or spanishvocabmenuchoice == '4':
        spanishvocabsetverbs()
        clearscreen()
        spanishvocabmenu()
    elif spanishvocabmenuchoice == 'vocab set 5' or spanishvocabmenuchoice == '5':
        spanishvocabsetcolors()
        clearscreen()
        spanishvocabmenu()
    elif spanishvocabmenuchoice == 'vocab set 6' or spanishvocabmenuchoice == '6':
        spanishvocabsetnumbersmenu()
        clearscreen()
        spanishvocabmenu()
    elif spanishvocabmenuchoice == 'vocab set 7' or spanishvocabmenuchoice == '7':
        spanishvocabsetmonths()
        clearscreen()
        spanishvocabmenu()
    elif spanishvocabmenuchoice == 'exit' or spanishvocabmenuchoice == '8':
        clearscreen()
        spanishmenu()
    else:
        print(imsorry)
        input(' ')
        clearscreen()
        spanishvocabmenu()

#verbs that i've used - Amar, Cambiar, Traer, Sonar, Quejar, Parar, Jugar, Correr, Caminar, Nadar

def spanishvocabsetverbs():
    print('''

        Spanish Vocab Menu
        1. Verb set 1
        2. Verb set 2
        3. Verb set 3
        4. Exit


        ''')

    spanishverbmenuchoice = input(' ').lower()

    if spanishverbmenuchoice == 'verb set 1' or spanishverbmenuchoice == '1':
        clearscreen()
        spanishverbset1()
    elif spanishverbmenuchoice == 'verb set 2' or spanishverbmenuchoice == '2':
        clearscreen()
        spanishverbset2()
    elif spanishverbmenuchoice == 'verb set 3' or spanishverbmenuchoice == '3':
        print(underconstruction)
        print(imsorry)
        input('')
        clearscreen()
        spanishvocabsetverbs()
    elif spanishverbmenuchoice == 'exit' or spanishverbmenuchoice == '4':
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorry)
        input(' ')
        clearscreen()
        spanishvocabsetverbs()

def verb1():
    print('''
        What does Amar mean?
        ''')

    verbvocabanswer = input('   ').lower()

    if verbvocabanswer == 'to love':
        print('''
        Good job!

        Amar means to love!''')
        input('')
        clearscreen()
    elif verbvocabanswer == 'exit' or verbvocabanswer == 'quit':
        print('time to study more next time!')
        spanishvocabsetverbs()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        verb1()

def verb2():
    print('''
            What does Cambiar mean?
            ''')

    verbvocabanswer = input('   ').lower()

    if verbvocabanswer == 'to change':
        print('''
            Good job!

            Cambiar means to change!''')
        input('')
        clearscreen()
    elif verbvocabanswer == 'exit' or verbvocabanswer == 'quit':
        print('time to study more next time!')
        spanishvocabsetverbs()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        verb2()


def verb3():
    print('''
                What does Traer mean?
                ''')

    verbvocabanswer = input('   ').lower()

    if verbvocabanswer == 'to bring':
        print('''
                Good job!

                Traer means to bring!''')
        input('')
        clearscreen()
    elif verbvocabanswer == 'exit' or verbvocabanswer == 'quit':
        print('time to study more next time!')
        spanishvocabsetverbs()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        verb3()

def verb4():
    print('''
                    What does Sonar mean?
                    ''')

    verbvocabanswer = input('   ').lower()

    if verbvocabanswer == 'to sound':
        print('''
                    Good job!

                    Sonar means to sound!''')
        input('')
        clearscreen()
    elif verbvocabanswer == 'exit' or verbvocabanswer == 'quit':
        print('time to study more next time!')
        spanishvocabsetverbs()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        verb4()

def verb5():
    print('''
                    What does Quejar mean?
                    ''')

    verbvocabanswer = input('   ').lower()

    if verbvocabanswer == 'to complain':
        print('''
                    Good job!

                    Quejar means to complain!''')
        input('')
        clearscreen()
    elif verbvocabanswer == 'exit' or verbvocabanswer == 'quit':
        print('time to study more next time!')
        spanishvocabsetverbs()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        verb5()

def verb6():
    print('''
                    What does Parar mean?
                    ''')

    verbvocabanswer = input('   ').lower()

    if verbvocabanswer == 'to stop':
        print('''
                    Good job!

                    Parar means to stop!''')
        input('')
        clearscreen()
    elif verbvocabanswer == 'exit' or verbvocabanswer == 'quit':
        print('time to study more next time!')
        spanishvocabsetverbs()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        verb6()

def spanishverbset1():
    spanishvocabverblist = [verb1, verb2, verb3, verb4, verb5, verb6]
    verbset1 = random.sample(spanishvocabverblist, k=6)
    verbset1[0]()
    verbset1[1]()
    verbset1[2]()
    verbset1[3]()
    verbset1[4]()
    verbset1[5]()
    print('good job! you completed Verb Set 1!')
    input(' ')
    clearscreen()
    spanishvocabsetverbs()

def verb7():
    print('''
                        What does Acordar mean?
                        ''')

    verbvocabanswer = input('   ').lower()

    if verbvocabanswer == 'to do something':
        print('''
                        Good job!

                        Acordar means to do something!''')
        input('')
        clearscreen()
    elif verbvocabanswer == 'exit' or verbvocabanswer == 'quit':
        print('time to study more next time!')
        spanishvocabsetverbs()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        verb7()

def verb8():
    print('''
                        What does Comer mean?
                        ''')

    verbvocabanswer = input('   ').lower()

    if verbvocabanswer == 'to eat':
        print('''
                        Good job!

                        Comer means to eat!''')
        input('')
        clearscreen()
    elif verbvocabanswer == 'exit' or verbvocabanswer == 'quit':
        print('time to study more next time!')
        spanishvocabsetverbs()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        verb8()

def verb9():
    print('''
                        What does Comprender mean?
                        ''')

    verbvocabanswer = input('   ').lower()

    if verbvocabanswer == 'to understand':
        print('''
                        Good job!

                        Comprender means to understand!''')
        input('')
        clearscreen()
    elif verbvocabanswer == 'exit' or verbvocabanswer == 'quit':
        print('time to study more next time!')
        spanishvocabsetverbs()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        verb9()

def verb10():
    print('''
                        What does Gustar mean?
                        ''')

    verbvocabanswer = input('   ').lower()

    if verbvocabanswer == 'to like':
        print('''
                        Good job!

                        Gustar means to like!''')
        input('')
        clearscreen()
    elif verbvocabanswer == 'exit' or verbvocabanswer == 'quit':
        print('time to study more next time!')
        spanishvocabsetverbs()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        verb10()

def verb11():
    print('''
                        What does Hervir mean?
                        ''')

    verbvocabanswer = input('   ').lower()

    if verbvocabanswer == 'to boil':
        print('''
                        Good job!

                        Hervir means to boil!''')
        input('')
        clearscreen()
    elif verbvocabanswer == 'exit' or verbvocabanswer == 'quit':
        print('time to study more next time!')
        spanishvocabsetverbs()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        verb11()

def verb12():
    print('''
                        What does Oír mean?
                        ''')

    verbvocabanswer = input('   ').lower()

    if verbvocabanswer == 'to hear':
        print('''
                        Good job!

                        Oír means to hear!''')
        input('')
        clearscreen()
    elif verbvocabanswer == 'exit' or verbvocabanswer == 'quit':
        print('time to study more next time!')
        spanishvocabsetverbs()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        verb12()

def spanishverbset2():
    spanishvocabverblist = [verb7, verb8, verb9, verb10, verb11, verb12]
    verbset2 = random.sample(spanishvocabverblist, k=6)
    verbset2[0]()
    verbset2[1]()
    verbset2[2]()
    verbset2[3]()
    verbset2[4]()
    verbset2[5]()
    print('good job! you completed Verb Set 2!')
    input(' ')
    clearscreen()
    spanishvocabsetverbs()

def jugarfunction():
    print('''
    What does Jugar mean?
    ''')

    jugarfunctionchoice = input('   ').lower()

    if jugarfunctionchoice == 'to play':
        print('''
    Good job!

    Jugar means to play!''')
        input('')
        clearscreen()
    elif jugarfunctionchoice == 'exit' or jugarfunctionchoice == 'quit':
        print('time to study more next time!')
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        jugarfunction()


def correrfunction():
    print('''
    What does Correr mean?
    ''')

    correrfunctionchoice = input('   ').lower()

    if correrfunctionchoice == 'to run':
        print('''
    Good job!

    Correr means to run!''')
        input(' ')
        clearscreen()
    elif correrfunctionchoice == 'exit' or correrfunctionchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        correrfunction()


def caminarfunction():
    print('''
    What does Caminar mean?
    ''')
    caminarfunctionchoice = input('     ').lower()

    if caminarfunctionchoice == 'to walk':
        print('''
    Good job!

    Caminar means to walk!''')
        input('  ')
        clearscreen()
    elif caminarfunctionchoice == 'exit' or caminarfunctionchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        caminarfunction()


def nadarfunction():
    print('''
    What does Nadar mean?
    ''')
    nadarfunctionchoice = input('   ').lower()

    if nadarfunctionchoice == 'to swim':
        print('''
    Good job!

    Nadar means to swim!''')
        input(' ')
        clearscreen()
    elif nadarfunctionchoice == 'exit' or nadarfunctionchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        nadarfunction()


def spanishvocabset1v2():
    spanishvocabset1list = [1, 2, 3, 4]
    spanishvocabset1v2choice = random.sample(spanishvocabset1list, 4)
    if spanishvocabset1v2choice == [1, 2, 3, 4]:
        jugarfunction()
        correrfunction()
        caminarfunction()
        nadarfunction()
    elif spanishvocabset1v2choice == [1, 2, 4, 3]:
        jugarfunction()
        correrfunction()
        nadarfunction()
        caminarfunction()
    elif spanishvocabset1v2choice == [1, 3, 2, 4]:
        jugarfunction()
        caminarfunction()
        correrfunction()
        nadarfunction()
    elif spanishvocabset1v2choice == [1, 3, 4, 2]:
        jugarfunction()
        caminarfunction()
        nadarfunction()
        correrfunction()
    elif spanishvocabset1v2choice == [1, 4, 2, 3]:
        jugarfunction()
        nadarfunction()
        correrfunction()
        caminarfunction()
    elif spanishvocabset1v2choice == [1, 4, 3, 2]:
        jugarfunction()
        nadarfunction()
        caminarfunction()
        correrfunction()
    elif spanishvocabset1v2choice == [2, 1, 3, 4]:
        correrfunction()
        jugarfunction()
        caminarfunction()
        nadarfunction()
    elif spanishvocabset1v2choice == [2, 1, 4, 3]:
        correrfunction()
        jugarfunction()
        nadarfunction()
        caminarfunction()
    elif spanishvocabset1v2choice == [2, 3, 1, 4]:
        correrfunction()
        caminarfunction()
        jugarfunction()
        nadarfunction()
    elif spanishvocabset1v2choice == [2, 3, 4, 1]:
        correrfunction()
        caminarfunction()
        nadarfunction()
        jugarfunction()
    elif spanishvocabset1v2choice == [2, 4, 1, 3]:
        correrfunction()
        nadarfunction()
        jugarfunction()
        caminarfunction()
    elif spanishvocabset1v2choice == [2, 4, 3, 1]:
        correrfunction()
        nadarfunction()
        caminarfunction()
        jugarfunction()
    elif spanishvocabset1v2choice == [3, 1, 2, 4]:
        caminarfunction()
        jugarfunction()
        correrfunction()
        nadarfunction()
    elif spanishvocabset1v2choice == [3, 1, 4, 2]:
        caminarfunction()
        jugarfunction()
        nadarfunction()
        correrfunction()
    elif spanishvocabset1v2choice == [3, 2, 1, 4]:
        caminarfunction()
        correrfunction()
        jugarfunction()
        nadarfunction()
    elif spanishvocabset1v2choice == [3, 2, 4, 1]:
        caminarfunction()
        correrfunction()
        nadarfunction()
        jugarfunction()
    elif spanishvocabset1v2choice == [3, 4, 1, 2]:
        caminarfunction()
        nadarfunction()
        jugarfunction()
        correrfunction()
    elif spanishvocabset1v2choice == [3, 4, 2, 1]:
        caminarfunction()
        nadarfunction()
        correrfunction()
        jugarfunction()
    elif spanishvocabset1v2choice == [4, 1, 2, 3]:
        nadarfunction()
        jugarfunction()
        correrfunction()
        caminarfunction()
    elif spanishvocabset1v2choice == [4, 1, 3, 2]:
        nadarfunction()
        jugarfunction()
        caminarfunction()
        correrfunction()
    elif spanishvocabset1v2choice == [4, 2, 1, 3]:
        nadarfunction()
        correrfunction()
        jugarfunction()
        caminarfunction()
    elif spanishvocabset1v2choice == [4, 2, 3, 1]:
        nadarfunction()
        correrfunction()
        caminarfunction()
        jugarfunction()
    elif spanishvocabset1v2choice == [4, 3, 1, 2]:
        nadarfunction()
        caminarfunction()
        jugarfunction()
        correrfunction()
    elif spanishvocabset1v2choice == [4, 3, 2, 1]:
        nadarfunction()
        caminarfunction()
        correrfunction()
        jugarfunction()
    else:
        print(imsorry)
        mainmenu()
    print('good job! you complated Vocab Set 1!')
    input(' ')
    clearscreen()
    spanishvocabmenu()


def estarfunction():
    print('''
    What does Estar mean?
    ''')
    estarfunctionchoice = input('   ').lower()

    if estarfunctionchoice == 'to be':
        print('''
    Good job!

    Estar means to be!''')
        input(' ')
        clearscreen()
    elif estarfunctionchoice == 'exit' or estarfunctionchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        estarfunction()


def tenerfunction():
    print('''
    What does Tener mean?
    ''')
    tenerfunctionchoice = input('   ').lower()

    if tenerfunctionchoice == 'to have':
        print('''
    Good job!

    Tener means to have!''')
        input(' ')
        clearscreen()
    elif tenerfunctionchoice == 'exit' or tenerfunctionchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        tenerfunction()


def irfunction():
    print('''
    What does Ir mean?
    ''')
    irfunctionchoice = input('   ').lower()

    if irfunctionchoice == 'to go':
        print('''
    Good job!

    Ir means to go!''')
        input(' ')
        clearscreen()
    elif irfunctionchoice == 'exit' or irfunctionchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        irfunction()


def saberfunction():
    print('''
    What does Saber mean?
    ''')
    saberfunctionchoice = input('   ').lower()

    if saberfunctionchoice == 'to know':
        print('''
    Good job!

    Saber means to know!''')
        input(' ')
        clearscreen()
    elif saberfunctionchoice == 'exit' or saberfunctionchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        saberfunction()


def spanishvocabset2():
    spanishvocablist2 = [1, 2, 3, 4]
    spanishvocabset2choice = random.sample(spanishvocablist2, 4)
    if spanishvocabset2choice == [1, 2, 3, 4]:
        estarfunction()
        tenerfunction()
        irfunction()
        saberfunction()
    elif spanishvocabset2choice == [1, 2, 4, 3]:
        estarfunction()
        tenerfunction()
        saberfunction()
        irfunction()
    elif spanishvocabset2choice == [1, 3, 2, 4]:
        estarfunction()
        irfunction()
        tenerfunction()
        saberfunction()
    elif spanishvocabset2choice == [1, 3, 4, 2]:
        estarfunction()
        irfunction()
        saberfunction()
        tenerfunction()
    elif spanishvocabset2choice == [1, 4, 2, 3]:
        estarfunction()
        tenerfunction()
        saberfunction()
        irfunction()
    elif spanishvocabset2choice == [1, 4, 3, 2]:
        estarfunction()
        saberfunction()
        tenerfunction()
        irfunction()
    elif spanishvocabset2choice == [2, 1, 3, 4]:
        tenerfunction()
        estarfunction()
        irfunction()
        saberfunction()
    elif spanishvocabset2choice == [2, 1, 4, 3]:
        tenerfunction()
        estarfunction()
        saberfunction()
        irfunction()
    elif spanishvocabset2choice == [2, 3, 1, 4]:
        tenerfunction()
        irfunction()
        saberfunction()
        estarfunction()
    elif spanishvocabset2choice == [2, 3, 4, 1]:
        tenerfunction()
        irfunction()
        saberfunction()
        estarfunction()
    elif spanishvocabset2choice == [2, 4, 1, 3]:
        tenerfunction()
        saberfunction()
        estarfunction()
        irfunction()
    elif spanishvocabset2choice == [2, 4, 3, 1]:
        tenerfunction()
        saberfunction()
        irfunction()
        estarfunction()
    elif spanishvocabset2choice == [3, 1, 2, 4]:
        irfunction()
        estarfunction()
        tenerfunction()
        saberfunction()
    elif spanishvocabset2choice == [3, 1, 4, 2]:
        irfunction()
        estarfunction()
        saberfunction()
        tenerfunction()
    elif spanishvocabset2choice == [3, 2, 1, 4]:
        irfunction()
        tenerfunction()
        estarfunction()
        saberfunction()
    elif spanishvocabset2choice == [3, 2, 4, 1]:
        irfunction()
        tenerfunction()
        saberfunction()
        estarfunction()
    elif spanishvocabset2choice == [3, 4, 1, 2]:
        irfunction()
        saberfunction()
        estarfunction()
        tenerfunction()
    elif spanishvocabset2choice == [3, 4, 2, 1]:
        irfunction()
        saberfunction()
        tenerfunction()
        estarfunction()
    elif spanishvocabset2choice == [4, 1, 2, 3]:
        saberfunction()
        estarfunction()
        tenerfunction()
        irfunction()
    elif spanishvocabset2choice == [4, 1, 3, 2]:
        saberfunction()
        estarfunction()
        irfunction()
        tenerfunction()
    elif spanishvocabset2choice == [4, 2, 1, 3]:
        saberfunction()
        tenerfunction()
        estarfunction()
        irfunction()
    elif spanishvocabset2choice == [4, 2, 3, 1]:
        saberfunction()
        tenerfunction()
        irfunction()
        estarfunction()
    elif spanishvocabset2choice == [4, 3, 1, 2]:
        saberfunction()
        irfunction()
        estarfunction()
        tenerfunction()
    elif spanishvocabset2choice == [4, 3, 2, 1]:
        saberfunction()
        irfunction()
        tenerfunction()
        estarfunction()
    else:
        print(imsorry)
        mainmenu()
    print('good job! you completed Vocab Set 2!')
    input(' ')
    clearscreen()
    spanishvocabmenu()


def partirfunction():
    print('''
    What does partir mean?
    ''')
    spanishchoice = input('   ').lower()

    if spanishchoice == 'to leave':
        print('''
    Good job!

    Partir means to leave!''')
        input(' ')
        clearscreen()
    elif spanishchoice == 'exit' or spanishchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        partirfunction()


def pedirfunction():
    print('''
    What does pedir mean?
    ''')
    spanishchoice = input('   ').lower()

    if spanishchoice == 'to ask':
        print('''
    Good job!

    Pedir means to ask!''')
        input(' ')
        clearscreen()
    elif spanishchoice == 'exit' or spanishchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        pedirfunction()


def aburrirfunction():
    print('''
    What does aburrir mean?
    ''')
    spanishchoice = input('   ').lower()

    if spanishchoice == 'to bore':
        print('''
    Good job!

    Aburrir means to bore!''')
        input(' ')
        clearscreen()
    elif spanishchoice == 'exit' or spanishchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        aburrirfunction()


def buscarfunction():
    print('''
    What does buscar mean?
    ''')
    spanishchoice = input('   ').lower()

    if spanishchoice == 'to look for':
        print('''
    Good job!

    Buscar means to look for!''')
        input(' ')
        clearscreen()
    elif spanishchoice == 'exit' or spanishchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        buscarfunction()

def cantarfunction():
    print('''
    What does cantar mean?
    ''')
    spanishchoice = input('   ').lower()

    if spanishchoice == 'to sing':
        print('''
    Good job!

    Cantar means to sing!''')
        input(' ')
        clearscreen()
    elif spanishchoice == 'exit' or spanishchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        cantarfunction()

def cocinarfunction():
    print('''
    What does cocinar mean?
    ''')
    spanishchoice = input('   ').lower()

    if spanishchoice == 'to cook':
        print('''
    Good job!

    Cocinar means to cook!''')
        input(' ')
        clearscreen()
    elif spanishchoice == 'exit' or spanishchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        cocinarfunction()

def spanishvocabset3():
    spanishvocabset3list = [partirfunction, pedirfunction, aburrirfunction, buscarfunction, cantarfunction, cocinarfunction]
    vocabset3 = random.sample(spanishvocabset3list, k=6)
    vocabset3[0]()
    vocabset3[1]()
    vocabset3[2]()
    vocabset3[3]()
    vocabset3[4]()
    vocabset3[5]()
    print('good job! you completed Vocab Set 3!')
    input(' ')
    clearscreen()
    spanishvocabmenu()

def spanishvocabsetnumbersmenu():
    print('''
    
    What would you like to work on?
    
    1. Numbers Set 1
    2. Numbers Set 2
    3. Exit
    
    
    ''')

    spanishmenuchoice = input(' ').lower()

    if spanishmenuchoice == 'numbers set 1' or spanishmenuchoice == 'set 1' or spanishmenuchoice == '1':
        spanishnumbersset1()
        clearscreen()
        spanishvocabmenu()
    elif spanishmenuchoice == 'numbers set 2' or spanishmenuchoice == 'set 2' or spanishmenuchoice == '2':
        print(underconstruction)
        input(' ')
        clearscreen()
        spanishvocabsetnumbersmenu()
    elif spanishmenuchoice == 'exit' or spanishmenuchoice == '3':
        clearscreen()
        mainmenu()
    else:
        print(imsorry)
        input('')
        clearscreen()
        spanishmenu()

def spanishunofunction():
    print('''
    What number is Uno?
    ''')
    spanishchoice = input('   ').lower()

    if spanishchoice == 'one' or spanishchoice == '1':
        print('''
    Good job!

    Uno is One!''')
        input(' ')
        clearscreen()
    elif spanishchoice == 'exit' or spanishchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabsetnumbersmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishunofunction()


def spanishdosfunction():
    print('''
    What number is Dos?
    ''')
    spanishchoice = input('   ').lower()

    if spanishchoice == 'two' or spanishchoice == '2':
        print('''
    Good job!

    Dos is Two!''')
        input(' ')
        clearscreen()
    elif spanishchoice == 'exit' or spanishchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabsetnumbersmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishdosfunction()


def spanishtresfunction():
    print('''
    What number is Tres?
    ''')
    spanishchoice = input('   ').lower()

    if spanishchoice == 'three' or spanishchoice == '3':
        print('''
    Good job!

    Tres is Three!''')
        input(' ')
        clearscreen()
    elif spanishchoice == 'exit' or spanishchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabsetnumbersmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishtresfunction()


def spanishcuatrofunction():
    print('''
    What number is Cuatro?
    ''')
    spanishchoice = input('   ').lower()

    if spanishchoice == 'four' or spanishchoice == '4':
        print('''
    Good job!

    Cuatro is Four!''')
        input(' ')
        clearscreen()
    elif spanishchoice == 'exit' or spanishchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabsetnumbersmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishcuatrofunction()


def spanishcincofunction():
    print('''
    What number is Cinco?
    ''')
    spanishchoice = input('   ').lower()

    if spanishchoice == 'five' or spanishchoice == '5':
        print('''
    Good job!

    Cinco is Five!''')
        input(' ')
        clearscreen()
    elif spanishchoice == 'exit' or spanishchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabsetnumbersmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishcincofunction()


def spanishseisfunction():
    print('''
    What number is Seis?
    ''')
    spanishchoice = input('   ').lower()

    if spanishchoice == 'six' or spanishchoice == '6':
        print('''
    Good job!

    Seis is Six!''')
        input(' ')
        clearscreen()
    elif spanishchoice == 'exit' or spanishchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabsetnumbersmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishseisfunction()


def spanishsietefunction():
    print('''
    What number is Siete?
    ''')
    spanishchoice = input('   ').lower()

    if spanishchoice == 'seven' or spanishchoice == '7':
        print('''
    Good job!

    Siete is Seven! (the best number)''')
        input(' ')
        clearscreen()
    elif spanishchoice == 'exit' or spanishchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabsetnumbersmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishsietefunction()


def spanishochofunction():
    print('''
    What number is Ocho?
    ''')
    spanishchoice = input('   ').lower()

    if spanishchoice == 'eight' or spanishchoice == '8':
        print('''
    Good job!

    Ocho is Eight!''')
        input(' ')
        clearscreen()
    elif spanishchoice == 'exit' or spanishchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabsetnumbersmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishochofunction()


def spanishnuevefunction():
    print('''
    What number is Nueve?
    ''')
    spanishchoice = input('   ').lower()

    if spanishchoice == 'nine' or spanishchoice == '9':
        print('''
    Good job!

    Nueve is Nine!''')
        input(' ')
        clearscreen()
    elif spanishchoice == 'exit' or spanishchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabsetnumbersmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishnuevefunction()


def spanishdiezfunction():
    print('''
    What number is Diez?
    ''')
    spanishchoice = input('   ').lower()

    if spanishchoice == 'ten' or spanishchoice == '10':
        print('''
    Good job!

    Diez is Ten!''')
        input(' ')
        clearscreen()
    elif spanishchoice == 'exit' or spanishchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabsetnumbersmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishdiezfunction()


def spanishochocincofunction():
    print('''
    Bonus Question (type 'pass' to skip)
    Who is Ocho Cinco?
    ''')
    spanishchoice = input('   ').lower()

    if spanishchoice == 'chad johnson':
        print('''
    Thats right!

    Ocho Cinco is Chad Johnson!''')
        input(' ')
        clearscreen()
    elif spanishchoice == 'clown' or spanishchoice == 'a clown':
        print('''
    Thats mean, no need to be rude.''')
        input(' ')
        clearscreen()
        spanishochocincofunction()
    elif spanishchoice == 'exit' or spanishchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabsetnumbersmenu()
    elif spanishchoice == 'pass':
        print('Ocho Cinco is Chad Johnson!')
        input(' ')
        clearscreen()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()


def spanishnumbersset1():
    spanishnumbersset1list = [spanishunofunction, spanishdosfunction, spanishtresfunction, spanishcuatrofunction,
                              spanishcincofunction, spanishseisfunction, spanishsietefunction, spanishochofunction,
                              spanishnuevefunction, spanishdiezfunction]
    spanishnumbersset1 = random.sample(spanishnumbersset1list, k=10)
    spanishnumbersset1[0]()
    spanishnumbersset1[1]()
    spanishnumbersset1[2]()
    spanishnumbersset1[3]()
    spanishnumbersset1[4]()
    spanishnumbersset1[5]()
    spanishnumbersset1[6]()
    spanishnumbersset1[7]()
    spanishnumbersset1[8]()
    spanishnumbersset1[9]()
    spanishochocincofunction()
    print('good job! you completed Numbers Set 1!')
    input(' ')
    clearscreen()
    spanishvocabsetnumbersmenu()


def spanishenerofunction():
    print('''
    What month is Enero?
    ''')
    spanishchoice = input('   ').lower()

    if spanishchoice == 'january':
        print('''
    Good job!

    Enero is January!''')
        input(' ')
        clearscreen()
    elif spanishchoice == 'exit' or spanishchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishenerofunction()


def spanishfebrerofunction():
    print('''
    What month is Febrero?
    ''')
    spanishchoice = input('   ').lower()

    if spanishchoice == 'february':
        print('''
    Good job!

    Febrero is February!''')
        input(' ')
        clearscreen()
    elif spanishchoice == 'exit' or spanishchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishfebrerofunction()


def spanishmarzofunction():
    print('''
    What month is Marzo?
    ''')
    spanishchoice = input('   ').lower()

    if spanishchoice == 'march':
        print('''
    Good job!

    Marzo is March!''')
        input(' ')
        clearscreen()
    elif spanishchoice == 'exit' or spanishchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishmarzofunction()


def spanishabrilfunction():
    print('''
    What month is Abril?
    ''')
    spanishchoice = input('   ').lower()

    if spanishchoice == 'april':
        print('''
    Good job!

    Abril is April!''')
        input(' ')
        clearscreen()
    elif spanishchoice == 'exit' or spanishchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishabrilfunction()


def spanishmayofunction():
    print('''
    What month is Mayo?
    ''')
    spanishchoice = input('   ').lower()

    if spanishchoice == 'may':
        print('''
    Good job!

    Mayo is May!''')
        input(' ')
        clearscreen()
    elif spanishchoice == 'exit' or spanishchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishmayofunction()


def spanishjuniofunction():
    print('''
    What month is Junio?
    ''')
    spanishchoice = input('   ').lower()

    if spanishchoice == 'june':
        print('''
    Good job!

    Junio is June!''')
        input(' ')
        clearscreen()
    elif spanishchoice == 'exit' or spanishchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishjuniounction()


def spanishjuliofunction():
    print('''
    What month is Julio?
    ''')
    spanishchoice = input('   ').lower()

    if spanishchoice == 'july':
        print('''
    Good job!

    Julio is July!''')
        input(' ')
        clearscreen()
    elif spanishchoice == 'exit' or spanishchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishjuliounction()


def spanishagostofunction():
    print('''
    What month is Agosto?
    ''')
    spanishchoice = input('   ').lower()

    if spanishchoice == 'august':
        print('''
    Good job!

    Agosto is August!''')
        input(' ')
        clearscreen()
    elif spanishchoice == 'exit' or spanishchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishagostofunction()


def spanishseptiembrefunction():
    print('''
    What month is Septiembre?
    ''')
    spanishchoice = input('   ').lower()

    if spanishchoice == 'september':
        print('''
    Good job!

    Septiembre is September!''')
        input(' ')
        clearscreen()
    elif spanishchoice == 'exit' or spanishchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishseptiembrefunction()


def spanishoctubrefunction():
    print('''
    What month is Octubre?
    ''')
    spanishchoice = input('   ').lower()

    if spanishchoice == 'october':
        print('''
    Good job!

    Octubre is October!''')
        input(' ')
        clearscreen()
    elif spanishchoice == 'exit' or spanishchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishoctubrefunction()


def spanishnoviembrefunction():
    print('''
    What month is Noviembre?
    ''')
    spanishchoice = input('   ').lower()

    if spanishchoice == 'november':
        print('''
    Good job!

    Noviembre is November!''')
        input(' ')
        clearscreen()
    elif spanishchoice == 'exit' or spanishchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()


def spanishdiciembrefunction():
    print('''
    What month is Diciembre?
    ''')
    spanishchoice = input('   ').lower()

    if spanishchoice == 'december':
        print('''
    Good job!

    Diciembre is December!''')
        input(' ')
        clearscreen()
    elif spanishchoice == 'exit' or spanishchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()

def spanishvocabsetmonths():
    spanishvocabmonthslist = [spanishenerofunction, spanishfebrerofunction, spanishmarzofunction,
                              spanishabrilfunction, spanishmayofunction, spanishjuniofunction,
                              spanishjuliofunction, spanishagostofunction, spanishseptiembrefunction,
                              spanishoctubrefunction, spanishnoviembrefunction, spanishdiciembrefunction]
    spanishmonthset = random.sample(spanishvocabmonthslist, k=12)
    spanishmonthset[0]()
    spanishmonthset[1]()
    spanishmonthset[2]()
    spanishmonthset[3]()
    spanishmonthset[4]()
    spanishmonthset[5]()
    spanishmonthset[6]()
    spanishmonthset[7]()
    spanishmonthset[8]()
    spanishmonthset[9]()
    spanishmonthset[10]()
    spanishmonthset[11]()
    print('good job! you completed the Month Vocab Set!')
    input(' ')
    clearscreen()
    spanishvocabmenu()


def spanishsentencemenu():
    print('''
    
    Spanish Sentence Menu
    1. Sentence set 1
    2. Sentence set 2
    3. Exit
    
    
    ''')

    spanishsentencemunuchoice = input(' ').lower()

    if spanishsentencemunuchoice == 'sentence set 1' or spanishsentencemunuchoice == '1':
        clearscreen()
        spanishsentenceset1()
    elif spanishsentencemunuchoice == 'sentence set 2' or spanishsentencemunuchoice == '2':
        clearscreen()
        spanishsentenceset2()
    elif spanishsentencemunuchoice == 'exit' or spanishsentencemunuchoice == '3':
        clearscreen()
        spanishmenu()
    else:
        print(imsorry)
        input(' ')
        clearscreen()
        spanishsentencemunu()

def spanishsentenceset1():
    spanishsentencelist1 = [1, 2, 3, 4]
    spanishsentencechoice1 = random.sample(spanishsentencelist1, 4)
    if spanishsentencechoice1 == [1, 2, 3, 4]:
        spanishsentence1()
        spanishsentence2()
        spanishsentence3()
        spanishsentence4()
    elif spanishsentencechoice1 == [1, 2, 4, 3]:
        spanishsentence1()
        spanishsentence2()
        spanishsentence4()
        spanishsentence3()
    elif spanishsentencechoice1 == [1, 3, 2, 4]:
        spanishsentence1()
        spanishsentence3()
        spanishsentence2()
        spanishsentence4()
    elif spanishsentencechoice1 == [1, 3, 4, 2]:
        spanishsentence1()
        spanishsentence3()
        spanishsentence4()
        spanishsentence2()
    elif spanishsentencechoice1 == [1, 4, 2, 3]:
        spanishsentence1()
        spanishsentence4()
        spanishsentence2()
        spanishsentence3()
    elif spanishsentencechoice1 == [1, 4, 3, 2]:
        spanishsentence1()
        spanishsentence4()
        spanishsentence3()
        spanishsentence2()
    elif spanishsentencechoice1 == [2, 1, 3, 4]:
        spanishsentence2()
        spanishsentence1()
        spanishsentence3()
        spanishsentence4()
    elif spanishsentencechoice1 == [2, 1, 4, 3]:
        spanishsentence2()
        spanishsentence1()
        spanishsentence4()
        spanishsentence3()
    elif spanishsentencechoice1 == [2, 3, 1, 4]:
        spanishsentence2()
        spanishsentence3()
        spanishsentence1()
        spanishsentence4()
    elif spanishsentencechoice1 == [2, 3, 4, 1]:
        spanishsentence2()
        spanishsentence3()
        spanishsentence4()
        spanishsentence1()
    elif spanishsentencechoice1 == [2, 4, 1, 3]:
        spanishsentence2()
        spanishsentence4()
        spanishsentence1()
        spanishsentence3()
    elif spanishsentencechoice1 == [2, 4, 3, 1]:
        spanishsentence2()
        spanishsentence4()
        spanishsentence3()
        spanishsentence1()
    elif spanishsentencechoice1 == [3, 1, 2, 4]:
        spanishsentence3()
        spanishsentence1()
        spanishsentence2()
        spanishsentence4()
    elif spanishsentencechoice1 == [3, 1, 4, 2]:
        spanishsentence3()
        spanishsentence1()
        spanishsentence4()
        spanishsentence2()
    elif spanishsentencechoice1 == [3, 2, 1, 4]:
        spanishsentence3()
        spanishsentence2()
        spanishsentence1()
        spanishsentence4()
    elif spanishsentencechoice1 == [3, 2, 4, 1]:
        spanishsentence3()
        spanishsentence2()
        spanishsentence4()
        spanishsentence1()
    elif spanishsentencechoice1 == [3, 4, 1, 2]:
        spanishsentence3()
        spanishsentence4()
        spanishsentence1()
        spanishsentence2()
    elif spanishsentencechoice1 == [3, 4, 2, 1]:
        spanishsentence3()
        spanishsentence4()
        spanishsentence2()
        spanishsentence1()
    elif spanishsentencechoice1 == [4, 1, 2, 3]:
        spanishsentence4()
        spanishsentence1()
        spanishsentence2()
        spanishsentence3()
    elif spanishsentencechoice1 == [4, 1, 3, 2]:
        spanishsentence4()
        spanishsentence1()
        spanishsentence3()
        spanishsentence2()
    elif spanishsentencechoice1 == [4, 2, 1, 3]:
        spanishsentence4()
        spanishsentence2()
        spanishsentence1()
        spanishsentence3()
    elif spanishsentencechoice1 == [4, 2, 3, 1]:
        spanishsentence4()
        spanishsentence2()
        spanishsentence3()
        spanishsentence1()
    elif spanishsentencechoice1 == [4, 3, 1, 2]:
        spanishsentence4()
        spanishsentence3()
        spanishsentence1()
        spanishsentence2()
    elif spanishsentencechoice1 == [4, 3, 2, 1]:
        spanishsentence4()
        spanishsentence3()
        spanishsentence2()
        spanishsentence1()
    else:
        print(imsorry)
        mainmenu()
    print('good job! you completed Sentence Set 1!')
    input(' ')
    clearscreen()
    spanishsentencemenu()


def spanishsentence1():
    print('''
    Translate the sentence
    
    Quisiera unas papas fritas.
    ''')
    spanishsentence1choice = input('   ').lower()

    if spanishsentence1choice == 'i would like some french fries' or \
            spanishsentence1choice == 'i would like french fries':
        print('''
    Good job!

    You got it correct!''')
        input(' ')
        clearscreen()
    elif spanishsentence1choice == 'exit' or spanishsentence1choice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishsentencemenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishsentence1()


def spanishsentence2():
    print('''
    Translate the sentence

    El cafe esta listo.
    ''')
    spanishsentence2choice = input('   ').lower()

    if spanishsentence2choice == 'the coffee is ready':
        print('''
    Good job!

    You got it correct!''')
        input(' ')
        clearscreen()
    elif spanishsentence2choice == 'exit' or spanishsentence2choice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishsentencemenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishsentence2()


def spanishsentence3():
    print('''
    Translate the sentence

    La leche esta en la heladera.
    ''')
    spanishsentence3choice = input('   ').lower()

    if spanishsentence3choice == 'the milk is in the fridge':
        print('''
    Good job!

    You got it correct!''')
        input(' ')
        clearscreen()
    elif spanishsentence3choice == 'exit' or spanishsentence3choice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishsentencemenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishsentence3()


def spanishsentence4():
    print('''
    Translate the sentence

    Tienen helado de chocolate y vainilla.
    ''')
    spanishsentence4choice = input('   ').lower()

    if spanishsentence4choice == 'they have chocolate and vanilla ice cream':
        print('''
    Good job!

    You got it correct!''')
        input(' ')
        clearscreen()
    elif spanishsentence4choice == 'exit' or spanishsentence4choice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishsentencemenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishsentence4()

def spanishsentenceset2():
    spanishsentencelist2 = [spanishsentence1set2, spanishsentence2set2, spanishsentence3set2,
                            spanishsentence4set2, spanishsentence5set2, spanishsentence6set2]
    sentenceset2 = random.sample(spanishsentencelist2, k=6)
    sentenceset2[0]()
    sentenceset2[1]()
    sentenceset2[2]()
    sentenceset2[3]()
    sentenceset2[4]()
    sentenceset2[5]()
    print('good job! you completed Sentence Set 2!')
    input(' ')
    clearscreen()
    spanishsentencemenu()

def spanishsentence1set2():
    print('''
        Translate the sentence

        Es hora de codificar.
        ''')
    spanishsentencechoice = input('   ').lower()

    if spanishsentencechoice == 'it is time to code':
        print('''
        Good job!

        You got it correct!''')
        input(' ')
        clearscreen()
    elif spanishsentencechoice == 'exit' or spanishsentencechoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishsentencemenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishsentence1set2()

def spanishsentence2set2():
    print('''
        Translate the sentence

        La última puerta a la derecha.
        ''')
    spanishsentencechoice = input('   ').lower()

    if spanishsentencechoice == 'the last door on the right':
        print('''
        Good job!

        You got it correct!''')
        input(' ')
        clearscreen()
    elif spanishsentencechoice == 'exit' or spanishsentencechoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishsentencemenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishsentence2set2()

def spanishsentence3set2():
    print('''
        Translate the sentence

        Por favor ve a lavar los platos.
        ''')
    spanishsentencechoice = input('   ').lower()

    if spanishsentencechoice == 'please go wash the dishes':
        print('''
        Good job!

        You got it correct!''')
        input(' ')
        clearscreen()
    elif spanishsentencechoice == 'exit' or spanishsentencechoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishsentencemenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishsentence3set2()

def spanishsentence4set2():
    print('''
        Translate the sentence

        Salgamos a comer esta noche.
        ''')
    spanishsentencechoice = input('   ').lower()

    if spanishsentencechoice == 'lets go out to eat tonight':
        print('''
        Good job!

        You got it correct!''')
        input(' ')
        clearscreen()
    elif spanishsentencechoice == 'exit' or spanishsentencechoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishsentencemenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishsentence4set2()

def spanishsentence5set2():
    print('''
        Translate the sentence

        Prefieres rojo o azul.
        ''')
    spanishsentencechoice = input('   ').lower()

    if spanishsentencechoice == 'do you prefer red or blue':
        print('''
        Good job!

        You got it correct!''')
        input(' ')
        clearscreen()
    elif spanishsentencechoice == 'exit' or spanishsentencechoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishsentencemenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishsentence5set2()

def spanishsentence6set2():
    print('''
        Translate the sentence

        Deberías practicar contando.
        ''')
    spanishsentencechoice = input('   ').lower()

    if spanishsentencechoice == 'you should practice counting':
        print('''
        Good job!

        You got it correct!''')
        input(' ')
        clearscreen()
    elif spanishsentencechoice == 'exit' or spanishsentencechoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishsentencemenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishsentence6set2()

def spanishcolorrojo():
    print('''
    What is Rojo?
    ''')
    spanishcolorchoice = input('   ').lower()

    if spanishcolorchoice == 'red':
        print('''
    Good job!

    You got it correct!''')
        input(' ')
        clearscreen()
    elif spanishcolorchoice == 'exit' or spanishcolorchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishcolorrojo()


def spanishcolorazul():
    print('''
    What is Azul?
    ''')
    spanishcolorchoice = input('   ').lower()

    if spanishcolorchoice == 'blue':
        print('''
    Good job!

    You got it correct!''')
        input(' ')
        clearscreen()
    elif spanishcolorchoice == 'exit' or spanishcolorchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishcolorazul()

def spanishcoloranaranjado():
    print('''
    What is Anaranjado?
    ''')
    spanishcolorchoice = input('   ').lower()

    if spanishcolorchoice == 'orange':
        print('''
    Good job!

    You got it correct!''')
        input(' ')
        clearscreen()
    elif spanishcolorchoice == 'exit' or spanishcolorchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishcoloranaranjado()


def spanishcolorverde():
    print('''
    What is Verde?
    ''')
    spanishcolorchoice = input('   ').lower()

    if spanishcolorchoice == 'green':
        print('''
    Good job!

    You got it correct!''')
        input(' ')
        clearscreen()
    elif spanishcolorchoice == 'exit' or spanishcolorchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishcolorverde()


def spanishcoloramarillo():
    print('''
    What is Amarillo?
    ''')
    spanishcolorchoice = input('   ').lower()

    if spanishcolorchoice == 'yellow':
        print('''
    Good job!

    You got it correct!''')
        input(' ')
        clearscreen()
    elif spanishcolorchoice == 'exit' or spanishcolorchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishcoloramarillo()


def spanishcolorblanco():
    print('''
    What is Blanco?
    ''')
    spanishcolorchoice = input('   ').lower()

    if spanishcolorchoice == 'white':
        print('''
    Good job!

    You got it correct!''')
        input(' ')
        clearscreen()
    elif spanishcolorchoice == 'exit' or spanishcolorchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishcolorblanco()

def spanishcolornegro():
    print('''
    What is Negro?
    ''')
    spanishcolorchoice = input('   ').lower()

    if spanishcolorchoice == 'black':
        print('''
    Good job!

    You got it correct!''')
        input(' ')
        clearscreen()
    elif spanishcolorchoice == 'exit' or spanishcolorchoice == 'quit':
        print('time to study more next time!')
        input(' ')
        clearscreen()
        spanishvocabmenu()
    else:
        print(imsorrywrong)
        input(' ')
        clearscreen()
        spanishcolornegro()


def spanishvocabsetcolors():
    spanishvocabsetcolorslist = [spanishcolorrojo, spanishcolorblanco, spanishcolorverde,
                                 spanishcoloramarillo, spanishcolorazul, spanishcoloranaranjado, spanishcolornegro]
    vocabsetcolors = random.sample(spanishvocabsetcolorslist, k=6)
    vocabsetcolors[0]()
    vocabsetcolors[1]()
    vocabsetcolors[2]()
    vocabsetcolors[3]()
    vocabsetcolors[4]()
    vocabsetcolors[5]()
    print('good job! you completed Colors Vocab!')
    input(' ')
    clearscreen()
    spanishvocabmenu()


# entertainment menu
def entertainmentmenu():
    print('''
    
    What would you like to do?
    1. Games
    2. Sports
    3. Videos
    4. Exit
    
    ''')

    entertainmentmenuchoice = input(' ').lower()

    if entertainmentmenuchoice == 'games' or entertainmentmenuchoice == '1':
        clearscreen()
        entertainmentgamesmenu()
    elif entertainmentmenuchoice == 'sports' or entertainmentmenuchoice == '2':
        clearscreen()
        entertainmentsports()
    elif entertainmentmenuchoice == 'videos' or entertainmentmenuchoice == '3':
        clearscreen()
        entertainmentmenuvideos()
    elif entertainmentmenuchoice == 'exit' or entertainmentmenuchoice == '4':
        clearscreen()
        mainmenu()
    else:
        print(imsorry)
        input(' ')
        clearscreen()
        entertainmentmenu()


def entertainmentgamesmenu():
    print('''
    Welcome to the Games page!
    
    1. Rock Paper Scissors
    2. Chess
    3. Tic Tac Toe
    4. Exit
    
    ''')

    entertainmentgamesmenuchoice = input(' ').lower()
    if entertainmentgamesmenuchoice == 'rock paper scissors' or entertainmentgamesmenuchoice == '1':
        print(underconstruction)
        clearscreen()
        entertainmentgamesmenu()
    elif entertainmentgamesmenuchoice == 'chess' or entertainmentgamesmenuchoice == '2':
        if __name__ == '__main__':
            chess.main()
            clearscreen()
            entertainmentgamesmenu()
    elif entertainmentgamesmenuchoice == 'chess' or entertainmentgamesmenuchoice == '3':
        if __name__ == '__main__':
            TicTacToePygame2.main()
            clearscreen()
            entertainmentgamesmenu()
    elif entertainmentgamesmenuchoice == 'exit' or entertainmentgamesmenuchoice == '4':
        entertainmentmenu()
    else:
        print(imsorry)
        clearscreen()
        entertainmentgamesmenu()


def entertainmentsports():
    print(underconstruction)
    input(' ')
    clearscreen()
    entertainmentmenu()


def entertainmentmenuvideos():
    print('''
    Here are some videos currently accessible by HelpfulBot
    
    1. South Park Bigger, Longer, and Uncut
    2. Big Hero 6
    3. Spongebob Squarepants
    4. Exit
    ''')

    entertainmentmenuvideoschoice = input(' ').lower()

    if entertainmentmenuvideoschoice == 'southpark bigger longer and uncut' \
            or entertainmentmenuvideoschoice == 'southpark bigger, longer, and uncut' \
            or entertainmentmenuvideoschoice == '1':
        startfile("D:\Sterling\Video\Movies\South Park Bigger, Longer & Uncut (1999)\SouthParkBiggerLongerandUncut.mkv")
        entertainmentmenuvideos()
    elif entertainmentmenuvideoschoice == 'big hero 6' or entertainmentmenuvideoschoice == '2':
        startfile("D:\Sterling\Video\Movies\Big Hero 6 (2014)\Big.Hero.6.2014.720p.BluRay.x264.YIFY.mp4")
        entertainmentmenuvideos()
    elif entertainmentmenuvideoschoice == 'spongebob squarepants' or entertainmentmenuvideoschoice == 'spongebob' or entertainmentmenuvideoschoice == '3':
        entertainmentvideosspongebobmenu()
    elif entertainmentmenuvideoschoice == 'exit' or entertainmentmenuvideoschoice == '4':
        entertainmentmenu()
    else:
        print(imsorry)
        input(' ')
        clearscreen()
        entertainmentmenuvideos()


def southparkbiggerlongeranduncut():
    print('Enjoy the show!')
    startfile("D:\Sterling\Video\Movies\South Park Bigger, Longer & Uncut (1999)\SouthParkBiggerLongerandUncut.mkv")
    entertainmentmenuvideos()

    # video = cv2.VideoCapture("D:\Sterling\Video\Movies\South Park Bigger, Longer & Uncut (1999)\SouthParkBiggerLongerandUncut.mkv")

    # while(video.isOpened()):
    #    ret,frame = video.read()

    #    frame = cv2.resize(frame, (1920, 1080))

    #    cv2.imshow("video", frame)

    #    if cv2.waitKey(10) & 0xFF == ord('q'):
    #        break
    #        entertainmentmenuvideos()


def bighero6():
    print('Enjoy the show!')
    startfile("D:\Sterling\Video\Movies\Big Hero 6 (2014)\Big.Hero.6.2014.720p.BluRay.x264.YIFY.mp4")
    entertainmentmenuvideos()

    # clearscreen()
    # print('Enjoy the show! Press q to exit the video at any time')

    # video = cv2.VideoCapture(
    #    "D:\Sterling\Video\Movies\Big Hero 6 (2014)\Big.Hero.6.2014.720p.BluRay.x264.YIFY.mp4")

    # while (video.isOpened()):
    #    ret, frame = video.read()

    #    frame = cv2.resize(frame, (1920, 1080))

    #    cv2.imshow("video", frame)

    #    if cv2.waitKey(10) & 0xFF == ord('q'):
    #        break
    #        entertainmentmenuvideos()


def entertainmentvideosspongebobmenu():
    print('''
    
    Which season would you like to watch?
    
    1. Season 1
    2. Season 2
    3. Season 3
    4. Exit
    
    
    ''')

    entertainmentvideosspongebobmenuchoice = input(' ').lower()

    if entertainmentvideosspongebobmenuchoice == 'season 1' or entertainmentvideosspongebobmenuchoice == '1':
        webbrowser.get('chrome').open_new(
            "https://www.amazon.com/Help-Wanted-Reef-Blowers-Treedome/dp/B0076QMOOG/ref=sr_1_1?crid=2NUYG86F4DQUB&keywords=spongebob+season+1&qid=1660302132&sprefix=spongebob+season+1%2Caps%2C83&sr=8-1")
        entertainmentvideosspongebobmenu()
    if entertainmentvideosspongebobmenuchoice == 'season 2' or entertainmentvideosspongebobmenuchoice == '2':
        webbrowser.get('chrome').open_new(
            "https://www.amazon.com/Sailor-Mouth-Artist-Unknown/dp/B0076QAL7I/ref=sr_1_2?crid=8XKBPWNGAH0&keywords=spongebob+season+2&qid=1660893232&sprefix=spongebob+season+2%2Caps%2C91&sr=8-2")
        entertainmentvideosspongebobmenu()
    if entertainmentvideosspongebobmenuchoice == 'exit' or entertainmentvideosspongebobmenuchoice == '4':
        entertainmentmenuvideos()
    else:
        print(imsorry)
        entertainmentvideosspongebobmenu()


# toolbox menu
def toolboxmenu():
    print('''

    Welcome to the Toolbox Menu!
    What can I help you with?

    1. Password Generator
    2. Exit


    ''')

    toolboxmenuchoice = input(' ').lower()

    if toolboxmenuchoice == 'password generator' or toolboxmenuchoice == '1':
        passwordgenerator()
        passwordgeneratorloop()
    if toolboxmenuchoice == 'exit' or toolboxmenuchoice == '2':
        mainmenu()
    else:
        print(imsorry)
        toolboxmenu()


def passwordgeneratorloop():
    passwordgeneratoranswer = input('Would you like another password? Y/N ').lower()
    if passwordgeneratoranswer == 'y' or passwordgeneratoranswer == 'yes':
        passwordgenerator()
        passwordgeneratorloop()
    else:
        toolboxmenu()


# password generator
def passwordgenerator():
    text_file = open('textfiles\\usa.txt', 'r')
    file_content = text_file.read()
    content_list = file_content.split('\n')

    # user inputs length of password they would like
    length = None

    while length == None:
        try:
            length = int(input('\nPassword length: '))
        except:
            print('sorry that isnt a number')

    # variables
    num = string.digits
    symbols = string.punctuation

    random3 = randint(1, 3)
    random2 = randint(1, 2)
    number_of_numbers = random2
    number_of_words = random3
    randomnumbers = random.choices(num, k=number_of_numbers)
    randompuncutation = random.choices(symbols, k=number_of_numbers)
    temp2 = ''.join(randompuncutation) + ''.join(randomnumbers)
    temp3 = ''.join(random.sample(temp2, len(temp2)))

    content_list_sorted = sorted(content_list, key=len)

    oneletterword = []
    twoletterword = []
    threeletterword = []
    fourletterword = []
    fiveletterword = []
    sixletterword = []
    sevenletterword = []
    eightletterword = []
    nineletterword = []
    tenletterword = []
    elevenletterword = []
    twelveletterword = []
    thirteenletterword = []

    for i in content_list_sorted:
        if len(i) == 1:
            oneletterword.append(i)
        elif len(i) == 2:
            twoletterword.append(i)
        elif len(i) == 3:
            threeletterword.append(i)
        elif len(i) == 4:
            fourletterword.append(i)
        elif len(i) == 5:
            fiveletterword.append(i)
        elif len(i) == 6:
            sixletterword.append(i)
        elif len(i) == 7:
            sevenletterword.append(i)
        elif len(i) == 8:
            eightletterword.append(i)
        elif len(i) == 9:
            nineletterword.append(i)
        elif len(i) == 10:
            tenletterword.append(i)
        elif len(i) == 11:
            elevenletterword.append(i)
        elif len(i) == 12:
            twelveletterword.append(i)
        elif len(i) == 13:
            thirteenletterword.append(i)
        else:
            pass

    number_of_characters = length - len(temp3)

    if number_of_characters == 1:
        password = random.choice(oneletterword) + temp3
    elif number_of_characters == 2:
        password = random.choice(twoletterword) + temp3
    elif number_of_characters == 3:
        password = random.choice(threeletterword) + temp3
    elif number_of_characters == 4:
        password = random.choice(fourletterword) + temp3
    elif number_of_characters == 5:
        password = random.choice(fiveletterword) + temp3
    elif number_of_characters == 6:
        passcombo = randint(1, 4)
        if passcombo == 1:
            password = random.choice(sixletterword) + temp3
        if passcombo == 2:
            password = random.choice(threeletterword) + random.choice(threeletterword) + temp3
        if passcombo == 3:
            password = random.choice(fourletterword) + random.choice(twoletterword) + temp3
        if passcombo == 4:
            password = random.choice(twoletterword) + random.choice(fourletterword) + temp3
    elif number_of_characters == 7:
        passcombo = randint(1, 5)
        if passcombo == 1:
            password = random.choice(sevenletterword) + temp3
        if passcombo == 2:
            password = random.choice(threeletterword) + random.choice(fourletterword) + temp3
        if passcombo == 3:
            password = random.choice(fourletterword) + random.choice(threeletterword) + temp3
        if passcombo == 4:
            password = random.choice(twoletterword) + random.choice(fiveletterword) + temp3
        if passcombo == 5:
            password = random.choice(fiveletterword) + random.choice(twoletterword) + temp3
    elif number_of_characters == 8:
        passcombo = randint(1, 4)
        if passcombo == 1:
            password = random.choice(eightletterword) + temp3
        if passcombo == 2:
            password = random.choice(fourletterword) + random.choice(fourletterword) + temp3
        if passcombo == 3:
            password = random.choice(fiveletterword) + random.choice(threeletterword) + temp3
        if passcombo == 4:
            password = random.choice(threeletterword) + random.choice(fiveletterword) + temp3
    elif number_of_characters == 9:
        passcombo = randint(1, 6)
        if passcombo == 1:
            password = random.choice(nineletterword) + temp3
        elif passcombo == 2:
            password = random.choice(fourletterword) + random.choice(fiveletterword) + temp3
        elif passcombo == 3:
            password = random.choice(fiveletterword) + random.choice(fourletterword) + temp3
        elif passcombo == 4:
            password = random.choice(threeletterword) + random.choice(threeletterword) \
                       + random.choice(threeletterword) + temp3
        elif passcombo == 5:
            password = random.choice(sixletterword) + random.choice(threeletterword) + temp3
        elif passcombo == 6:
            password = random.choice(threeletterword) + random.choice(sixletterword) + temp3
    elif number_of_characters == 10:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(tenletterword) + temp3
        elif passcombo == 2:
            password = random.choice(fiveletterword) + random.choice(fiveletterword) + temp3
        elif passcombo == 3:
            password = random.choice(sixletterword) + random.choice(fourletterword) + temp3
        elif passcombo == 4:
            password = random.choice(fourletterword) + random.choice(sixletterword) + temp3
        elif passcombo == 5:
            password = random.choice(fourletterword) + random.choice(threeletterword) \
                       + random.choice(threeletterword) + temp3
        elif passcombo == 6:
            password = random.choice(threeletterword) + random.choice(fourletterword) \
                       + random.choice(threeletterword) + temp3
        elif passcombo == 7:
            password = random.choice(threeletterword) + random.choice(threeletterword) \
                       + random.choice(fourletterword) + temp3
        elif passcombo == 8:
            password = random.choice(fiveletterword) + random.choice(threeletterword) \
                       + random.choice(twoletterword) + temp3
        elif passcombo == 9:
            password = random.choice(threeletterword) + random.choice(twoletterword) \
                       + random.choice(fiveletterword) + temp3
        elif passcombo == 10:
            password = random.choice(twoletterword) + random.choice(fiveletterword) \
                       + random.choice(threeletterword) + temp3
        elif passcombo == 11:
            password = random.choice(threeletterword) + random.choice(fiveletterword) \
                       + random.choice(twoletterword) + temp3
        elif passcombo == 12:
            password = random.choice(fiveletterword) + random.choice(twoletterword) \
                       + random.choice(threeletterword) + temp3
        elif passcombo == 13:
            password = random.choice(fourletterword) + random.choice(fourletterword) \
                       + random.choice(twoletterword) + temp3
        elif passcombo == 14:
            password = random.choice(fourletterword) + random.choice(twoletterword) \
                       + random.choice(fourletterword) + temp3
        elif passcombo == 15:
            password = random.choice(twoletterword) + random.choice(fourletterword) \
                       + random.choice(fourletterword) + temp3
    elif number_of_characters == 11:
        passcombo = randint(1, 8)
        if passcombo == 1:
            password = random.choice(elevenletterword) + temp3
        elif passcombo == 2:
            password = random.choice(sixletterword) + random.choice(fiveletterword) + temp3
        elif passcombo == 3:
            password = random.choice(fiveletterword) + random.choice(sixletterword) + temp3
        elif passcombo == 4:
            password = random.choice(sevenletterword) + random.choice(fourletterword) + temp3
        elif passcombo == 5:
            password = random.choice(fourletterword) + random.choice(fiveletterword) \
                       + random.choice(twoletterword) + temp3
        elif passcombo == 6:
            password = random.choice(fiveletterword) + random.choice(fourletterword) \
                       + random.choice(twoletterword) + temp3
        elif passcombo == 7:
            password = random.choice(sixletterword) + random.choice(threeletterword) \
                       + random.choice(threeletterword) + temp3
        elif passcombo == 8:
            password = random.choice(sixletterword) + random.choice(threeletterword) \
                       + random.choice(threeletterword) + temp3
    elif number_of_characters == 12:
        passcombo = randint(1, 10)
        if passcombo == 1:
            password = random.choice(twelveletterword) + temp3
        elif passcombo == 2:
            password = random.choice(sixletterword) + random.choice(sixletterword) + temp3
        elif passcombo == 3:
            password = random.choice(sevenletterword) + random.choice(fiveletterword) + temp3
        elif passcombo == 4:
            password = random.choice(fiveletterword) + random.choice(sevenletterword) + temp3
        elif passcombo == 5:
            password = random.choice(eightletterword) + random.choice(fourletterword) + temp3
        elif passcombo == 6:
            password = random.choice(fourletterword) + random.choice(eightletterword) + temp3
        elif passcombo == 7:
            password = random.choice(threeletterword) + random.choice(threeletterword) \
                       + random.choice(sixletterword) + temp3
        elif passcombo == 8:
            password = random.choice(threeletterword) + random.choice(sixletterword) \
                       + random.choice(threeletterword) + temp3
        elif passcombo == 9:
            password = random.choice(sixletterword) + random.choice(threeletterword) \
                       + random.choice(threeletterword) + temp3
        elif passcombo == 10:
            password = random.choice(fourletterword) + random.choice(fourletterword) \
                       + random.choice(fourletterword) + temp3
    elif number_of_characters == 13:
        passcombo = randint(1, 12)
        if passcombo == 1:
            password = random.choice(thirteenletterword) + temp3
        elif passcombo == 2:
            password = random.choice(sevenletterword) + random.choice(sixletterword) + temp3
        elif passcombo == 3:
            password = random.choice(sixletterword) + random.choice(sevenletterword) + temp3
        else:
            password = random.choice(eightletterword) + random.choice(fiveletterword) + temp3
    elif number_of_characters == 14:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(fourletterword) + random.choice(tenletterword) + temp3
        elif passcombo == 2:
            password = random.choice(fiveletterword) + random.choice(nineletterword) + temp3
        elif passcombo == 3:
            password = random.choice(sixletterword) + random.choice(eightletterword) + temp3
        elif passcombo == 4:
            password = random.choice(sevenletterword) + random.choice(sevenletterword) + temp3
        elif passcombo == 5:
            password = random.choice(eightletterword) + random.choice(sixletterword) + temp3
        elif passcombo == 6:
            password = random.choice(sixletterword) + random.choice(eightletterword) + temp3
        elif passcombo == 7:
            password = random.choice(tenletterword) + random.choice(fourletterword) + temp3
        else:
            password = random.choice(nineletterword) + random.choice(fiveletterword) + temp3
    elif number_of_characters == 15:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(tenletterword) + random.choice(fiveletterword) + temp3
        else:
            password = random.choice(nineletterword) + random.choice(sixletterword) + temp3
    elif number_of_characters == 16:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(elevenletterword) + random.choice(fiveletterword) + temp3
        else:
            password = random.choice(tenletterword) + random.choice(sixletterword) + temp3
    elif number_of_characters == 17:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(twelveletterword) + random.choice(fiveletterword) + temp3
        else:
            password = random.choice(elevenletterword) + random.choice(sixletterword) + temp3
    elif number_of_characters == 18:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(twelveletterword) + random.choice(sixletterword) + temp3
        else:
            password = random.choice(elevenletterword) + random.choice(sevenletterword) + temp3
    elif number_of_characters == 19:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(twelveletterword) + random.choice(sevenletterword) + temp3
        else:
            password = random.choice(elevenletterword) + random.choice(eightletterword) + temp3
    elif number_of_characters == 20:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(twelveletterword) + random.choice(eightletterword) + temp3
        else:
            password = random.choice(elevenletterword) + random.choice(nineletterword) + temp3
    elif number_of_characters == 21:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(twelveletterword) + random.choice(nineletterword) + temp3
        else:
            password = random.choice(elevenletterword) + random.choice(tenletterword) + temp3
    elif number_of_characters == 22:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(twelveletterword) + random.choice(tenletterword) + temp3
        else:
            password = random.choice(elevenletterword) + random.choice(elevenletterword) + temp3
    elif number_of_characters == 23:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(tenletterword) + random.choice(fiveletterword) \
                       + random.choice(eightletterword) + temp3
        else:
            password = random.choice(nineletterword) + random.choice(fiveletterword) \
                       + random.choice(nineletterword) + temp3
    elif number_of_characters == 24:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(tenletterword) + random.choice(fiveletterword) \
                       + random.choice(nineletterword) + temp3
        else:
            password = random.choice(nineletterword) + random.choice(fiveletterword) \
                       + random.choice(tenletterword) + temp3
    elif number_of_characters == 25:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(tenletterword) + random.choice(sixletterword) \
                       + random.choice(nineletterword) + temp3
        else:
            password = random.choice(nineletterword) + random.choice(tenletterword) \
                       + random.choice(sixletterword) + temp3
    elif number_of_characters == 26:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(tenletterword) + random.choice(sevenletterword) \
                       + random.choice(nineletterword) + temp3
        else:
            password = random.choice(nineletterword) + random.choice(tenletterword) \
                       + random.choice(sevenletterword) + temp3
    elif number_of_characters == 27:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(tenletterword) + random.choice(eightletterword) \
                       + random.choice(nineletterword) + temp3
        else:
            password = random.choice(nineletterword) + random.choice(tenletterword) \
                       + random.choice(eightletterword) + temp3
    elif number_of_characters == 28:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(tenletterword) + random.choice(nineletterword) \
                       + random.choice(nineletterword) + temp3
        else:
            password = random.choice(nineletterword) + random.choice(tenletterword) \
                       + random.choice(nineletterword) + temp3
    elif number_of_characters == 29:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(tenletterword) + random.choice(nineletterword) \
                       + random.choice(tenletterword) + temp3
        else:
            password = random.choice(tenletterword) + random.choice(tenletterword) \
                       + random.choice(nineletterword) + temp3
    elif number_of_characters == 30:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(tenletterword) + random.choice(fiveletterword) \
                       + random.choice(tenletterword) + random.choice(fiveletterword) + temp3
        else:
            password = random.choice(tenletterword) + random.choice(tenletterword) \
                       + random.choice(fiveletterword) + random.choice(fiveletterword) + temp3
    elif number_of_characters == 31:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(tenletterword) + random.choice(sixletterword) \
                       + random.choice(tenletterword) + random.choice(fiveletterword) + temp3
        else:
            password = random.choice(tenletterword) + random.choice(tenletterword) \
                       + random.choice(sixletterword) + random.choice(fiveletterword) + temp3
    elif number_of_characters == 32:
        passcombo = randint(1, 15)
        if passcombo == 1:
            password = random.choice(tenletterword) + random.choice(sixletterword) \
                       + random.choice(tenletterword) + random.choice(sixletterword) + temp3
        else:
            password = random.choice(tenletterword) + random.choice(tenletterword) \
                       + random.choice(sixletterword) + random.choice(sixletterword) + temp3
    else:
        password = 'sorry we currently do not support that many characters at the moment'

    print(password)


# personal notes menu
def personalnotesmenu():
    clearscreen()
    print('''
    This is where I keep my personal notes that are not included in the github, maybe you can put your own notes here!

    ''')

    input(' ')
    mainmenu()

mainmenu()
