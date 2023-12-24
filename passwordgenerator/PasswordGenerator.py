import random
import string
from random import randint


#currently a work in progress, but functional to some degree

text_file = open('textfiles\\usa.txt', 'r')
file_content = text_file.read()
content_list = file_content.split('\n')



#user inputs length of password they would like

length = None

while length == None:
    try:
        length = int(input('\nPassword length: '))
    except:
        print('sorry that isnt a number')


#variables
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
    passcombo = randint(1,8)
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
    elif passcombo == 2:
        password = random.choice(tenletterword) + random.choice(tenletterword) \
                   + random.choice(sixletterword) + random.choice(fiveletterword) + temp3
    elif passcombo == 3:
        password = random.choice(tenletterword) + random.choice(elevenletterword) \
                   + random.choice(fiveletterword) + random.choice(fiveletterword) + temp3
    elif passcombo == 4:
        password = random.choice(tenletterword) + random.choice(twelveletterword) \
                   + random.choice(fiveletterword) + random.choice(fourletterword) + temp3
    elif passcombo == 5:
        password = random.choice(tenletterword) + random.choice(twelveletterword) \
                   + random.choice(fourletterword) + random.choice(fiveletterword) + temp3
    elif passcombo == 6:
        password = random.choice(tenletterword) + random.choice(tenletterword) \
                   + random.choice(sevenletterword) + random.choice(fourletterword) + temp3
    elif passcombo == 7:
        password = random.choice(tenletterword) + random.choice(tenletterword) \
                   + random.choice(fourletterword) + random.choice(sevenletterword) + temp3
    else:
        password = random.choice(tenletterword) + random.choice(tenletterword) \
                   + random.choice(eightletterword) + random.choice(threeletterword) + temp3
elif number_of_characters == 32:
    passcombo = randint(1, 15)
    if passcombo == 1:
        password = random.choice(tenletterword) + random.choice(sixletterword) \
                   + random.choice(tenletterword) + random.choice(sixletterword) + temp3
    else:
        password = random.choice(tenletterword) + random.choice(tenletterword) \
                   + random.choice(sixletterword) + random.choice(sixletterword) + temp3
elif number_of_characters == 33:
    passcombo = randint(1, 15)
    if passcombo == 1:
        password = random.choice(twelveletterword) + random.choice(twelveletterword) \
                   + random.choice(nineletterword) + temp3
    else:
        password = random.choice(twelveletterword) + random.choice(elevenletterword) \
                   + random.choice(tenletterword) + temp3
elif number_of_characters == 34:
    passcombo = randint(1, 15)
    if passcombo == 1:
        password = random.choice(twelveletterword) + random.choice(twelveletterword) \
                   + random.choice(tenletterword) + temp3
    else:
        password = random.choice(twelveletterword) + random.choice(elevenletterword) \
                   + random.choice(elevenletterword) + temp3
elif number_of_characters == 35:
    passcombo = randint(1, 15)
    if passcombo == 1:
        password = random.choice(twelveletterword) + random.choice(twelveletterword) \
                   + random.choice(elevenletterword) + temp3
    else:
        password = random.choice(twelveletterword) + random.choice(elevenletterword) \
                   + random.choice(twelveletterword) + temp3
else:
    password = 'sorry we currently do not support that many characters at the moment'

print(password)






