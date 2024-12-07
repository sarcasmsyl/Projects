import random

def RandomChamp():
    line_number = 0
    selected_line = None
    filename = 'DiscordBot/textfiles/Champs.txt'

    with open(filename, 'r') as file:
        for line in file:
            line_number += 1
            if random.randint(1, line_number) == 1:
                selected_line = line.strip()

    return selected_line