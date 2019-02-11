# Python Text RPG

import sys
import os
import time

screen_width = 100


#### Player Setup ####
class Player:
    def __init__(self):
        self.name = ''
        self.incentive = 0
        self.motivation = 0
        self.job = ''
        self.status_effects = []
        self.location = 'b2'
        self.game_over = False


myPlayer = Player()


#### Title Screen ####

def title_screen_selections():
    option = input("> ")
    if option.lower() == "play":
        setup_game()
    elif option.lower() == "help":
        help_menu()
    elif option.lower() == "quit":
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command (-play -help -quit).")
        option = input("> ")
        if option.lower() == "play":
            setup_game()
        elif option.lower() == "help":
            help_menu()
        elif option.lower() == "quit":
            sys.exit()


def title_screen():
    os.system('cls')
    print('###############################################')
    print('#         Welcome to this Text RPG!           #')
    print('###############################################')
    print(' > Play                                        ')
    print(' > Help                                        ')
    print(' > Quit                                        ')
    print(' Have fun.                                     ')
    title_screen_selections()


def help_menu():
    print('###############################################')
    print('#         Welcome to this Text RPG!           #')
    print('###############################################')
    print('- Use up, down, left and right to move.        ')
    print('- Type your commands                           ')
    print('- Use "look" to inspect something              ')
    print('- Email me if there is a bug.                  ')
    title_screen_selections()

    #### Game functionality ####

    #### map ####
    """
    a1 a2...
    -------------
    |  |  |  |  | a4
    -------------
    |  |  |  |  | b4 ...
    -------------
    |  |  |  |  |
    -------------
    |  |  |  |  |
    -------------
    """


ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examination'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False}

zonemap = {
    'a1': {
        'ZONENAME': 'Front Door Entrance',
        'DESCRIPTION': "Finally, at the temple of all treasures. Is that the smell of wealth??? Gotta find it before anyone catches me",
        'EXAMINATION': 'examination',
        'SOLVED': False,
        UP: '',
        DOWN: 'b1',
        LEFT: '',
        RIGHT: 'a2'
    },
    'a2': {
        'ZONENAME': 'Kings Hall',
        'DESCRIPTION': 'This must be the famous Kings Hall. Where all the trasure is checked. But where is it stored?!?!',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        UP: '',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3'
    },
    'a3': {
        'ZONENAME': 'Chambers of Princess Annabell',
        'DESCRIPTION': 'Is that the princess?? She is beautiful. Do I say hi? Wait!, the treasure?? Too bad, gotta go!!!',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        UP: '',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4'
    },
    'a4': {
        'ZONENAME': 'Army Training Station',
        'DESCRIPTION': 'Wooww, such a huge army... Poor little me, I wonder what they can do to me, chap chap fleeing away...',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        UP: '',
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: ''
    },

    'b1': {
        'ZONENAME': 'Black Magical Door',
        'DESCRIPTION': 'Finally, the Magical door. I can smell treasure, closer than ever, but how do I get in???',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        UP: 'a1',
        DOWN: 'c1',
        LEFT: '',
        RIGHT: 'b2'
    },
    'b2': {
        'ZONENAME': 'Spiked Floor',
        'DESCRIPTION': 'Ooohh, the spiked floor. one wrong move and spears protrude from everywhere to stab you to death... one step at a time',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3'
    },
    'b3': {
        'ZONENAME': 'Scorpions Shed',
        'DESCRIPTION': 'I hear the Scorpions here are the most venomous, quickly but steadily...',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        UP: 'a3',
        DOWN: 'c3',
        LEFT: 'b2',
        RIGHT: 'b4'
    },
    'b4': {
        'ZONENAME': 'Rotating Floor',
        'DESCRIPTION': 'Wait!!! This wasnt in the map!!! Time to be innovative.',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        UP: 'a4',
        DOWN: 'c4',
        LEFT: 'b3',
        RIGHT: ''
    },

    'c1': {
        'ZONENAME': 'c1',
        'DESCRIPTION': 'description',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        UP: 'b1',
        DOWN: 'd1',
        LEFT: '',
        RIGHT: 'c2'
    },
    'c2': {
        'ZONENAME': 'c2',
        'DESCRIPTION': 'description',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        UP: 'b2',
        DOWN: 'd2',
        LEFT: 'c1',
        RIGHT: 'c3'
    },
    'c3': {
        'ZONENAME': 'c3',
        'DESCRIPTION': 'description',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        UP: 'b3',
        DOWN: 'd3',
        LEFT: 'c2',
        RIGHT: 'c4'
    },
    'c4': {
        'ZONENAME': 'c4',
        'DESCRIPTION': 'description',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        UP: 'b4',
        DOWN: 'd4',
        LEFT: 'c3',
        RIGHT: ''
    },

    'd1': {
        'ZONENAME': 'The Magical Chambers',
        'DESCRIPTION': 'Sssshhh... Quiet, Quiet... Dont wake up Bari, the Demon Goddess',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        UP: 'c1',
        DOWN: '',
        LEFT: '',
        RIGHT: 'd2'
    },
    'd2': {
        'ZONENAME': 'Dark Chambers',
        'DESCRIPTION': 'Night vision goggles time!!!, I bet Bari, the Demon Goddess has not seen tech like this...',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        UP: 'c2',
        DOWN: '',
        LEFT: 'd1',
        RIGHT: 'd3'
    },
    'd3': {
        'ZONENAME': 'Treasure Door',
        'DESCRIPTION': 'Finally at the entrance, riches!!! riches!!!, hoo hoooo, hooooo....',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        UP: 'c3',
        DOWN: '',
        LEFT: 'd2',
        RIGHT: 'd4'
    },
    'd4': {
        'ZONENAME': 'Treasure Chambers',
        'DESCRIPTION': 'Look, all that Gold, and Diamonds... The magical Eye!!! That must be worth a fortune. Quick Quick, grab it all..',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        UP: 'c4',
        DOWN: '',
        LEFT: 'd3',
        RIGHT: ''
    },
}


#### Game interactivity ####

def print_location():
    print('\n' + ('#' * (4 + (len(myPlayer.location)))))
    print('# ' + zonemap[myPlayer.location]['ZONENAME'] + ' #')
    print('# ' + zonemap[myPlayer.location]['DESCRIPTION'] + ' #')
    print('\n' + ('#' * (4 + (len(myPlayer.location)))))


def prompt():
    print('\n' + '=========================')
    print('what would you like to do?')
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel',
                          'walk', 'quit', 'examine',
                          'interact', 'look', 'inspect']
    while action.lower() not in acceptable_actions:
        print("Unknown action, try again!")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'interact', 'look', 'inspect']:
        player_examine(action.lower())


def player_move(action):
    ask = 'Where do you want to go exactly?\n'
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        mouvement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.location][LEFT]
        mouvement_handler(destination)
    elif dest in ['right', 'east']:
        destination = zonemap[myPlayer.location][RIGHT]
        mouvement_handler(destination)
    elif dest in ['down', 'south']:
        destination = zonemap[myPlayer.location][DOWN]
        mouvement_handler(destination)


def mouvement_handler(destination):
    print('\n' + 'You have arrived to your destination.')
    myPlayer.location = destination
    print_location()


def player_examine(action):
    if zonemap[myPlayer.location]['SOLVED']:
        print('You have already been to this zone.')
    else:
        print('You can trigger a puzzle here.')


#### Game functionality ####

def main_game_loop():
    while myPlayer.game_over is False:
        prompt()
    # here handle if puzzle have been solved (full completion)


def setup_game():
    os.system('cls')

    question1 = 'Hello, what is your name?\n'
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name

    question2 = 'What is your title/job?\n'
    question2added = 'You can be a cook, a barman or barmaid, or a singer.\n'
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    player_job = input("> ")
    valid_jobs = ['cook', 'barman', 'barmaid', 'singer']
    while player_job.lower() not in valid_jobs:
        player_job = input("> ")
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print('Good. We need a decent ' + player_job + ' in our pub.\n')

    ### Player Stats ###
    if myPlayer.job is 'cook':
        self.incentive = 100
        self.motivation = 40
    if myPlayer.job is 'barman':
        self.incentive = 70
        self.motivation = 70
    if myPlayer.job is 'barmaid':
        self.incentive = 60
        self.motivation = 80
    if myPlayer.job is 'singer':
        self.incentive = 45
        self.motivation = 95

    ### Introduction ###
    question3 = 'Welcome ' + player_name + ' the ' + player_job + '!\n'
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name

    os.system('cls')
    speech1 = 'Welcome to our humble pub.\n'
    speech2 = 'We know you are new in this area.\n'
    speech3 = 'Make a name for your self here and beyond!\n'
    speech4 = 'Good luck, you will need it.\n'
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.3)
    os.system('cls')
    print('####################################')
    print('##   The adventure starts now!    ##')
    print('####################################')
    main_game_loop()


title_screen()
