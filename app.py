from constants import PLAYERS,  TEAMS
import copy


PLAYERS_PER_TEAM = len(PLAYERS) / len(TEAMS)
teams_copy = copy.deepcopy(TEAMS)
players_copy = copy.deepcopy(PLAYERS)
balanced_teams = {key: [] for key in TEAMS}
experienced = []
no_experience = []

def clean_data():
    for player in players_copy:
        if player.get('experience') == 'NO':
            player['experience'] = False
        else:
            player['experience'] = True
        player['height'] = int(player['height'][:2])
        player['guardians'] = player['guardians'].split( " and ")


def balance_experience():
    for player in players_copy:
        if player.get('experience') == True:
            experienced.append(player)
        else:
            no_experience.append(player)


def balance_teams():
    balance_counter = 0
    while len(balanced_teams.get('Panthers')) < PLAYERS_PER_TEAM:
        for key, values in balanced_teams.items():
            player_experience = experienced[balance_counter]
            player_no_experience = no_experience[balance_counter]
            items = {key:values.append(player_experience)}
            items = {key:values.append(player_no_experience)}
            balance_counter += 1 
        
        for keys, values in balanced_teams.items():
            if len(values) > PLAYERS_PER_TEAM:
                items = {key:values.pop()}


def menu():
    print('Welcome to the basketball team stats tool!\n'
    '►►►Menu◄◄◄\n'
    'Here are your choices, please select one:\n\n'
    '1) Display Team Stats\n'
    '2) Exit')

    choice = input('Enter your choice here. 1 or 2: ')

    while True:
        if choice == '1':
            teams_menu() 
            break
        elif choice == '2':
            print('Thanks for visiting! See you next time!')
            break
        else:
            choice = input('Please enter a valid option(1 or 2): ')


def teams_menu():
    choice1 = input('Choose a team by selecting the respective number:\n'
    '1) Panthers\n'
    '2) Warriors\n'
    '3) Bandits\n')

    while True:
        if choice1 == '1':
            team_stats(1)
        elif choice1 == '2':
            team_stats(2)
        elif choice1 == '3':
            team_stats(3)
        else:
            choice1 = input('That is not a valid option, please enter a value between 1 and 3 ')


def team_stats(choice1):
    if choice1 == 1:
        format_stats('Panthers')
    elif choice1 == 2:
        format_stats('Warriors')
    elif choice1 == 3:
        format_stats('Bandits')

def format_stats(team):
    print('Team: {} Stats'.format(team))
    print('-' * 10)
    print('Total players : ' + str(PLAYERS_PER_TEAM))
    print('Players on team:')
    
    player_list = []
    
    for player in balanced_teams.get(team):
        player_list.append(player.get('name'))
    print(', '.join(player_list))


    show_experience(team)
    average_height(team)
    show_guardians(team)

    continue_tool()

def continue_tool():
    choice = None
    while choice == None:
        choice = input('Would you like to continue? Y or N.  ')
        if choice.lower !='n' or choice.lower != 'y':
            print('Please enter a valid choice.')
            
        elif choice.lower == 'n':
            print('Thank for visiting!')
           
        else:
            teams_menu()
            

def show_experience(team):
    experienced = 0
    not_experienced = 0
    for player in balanced_teams.get(team):
        if player.get('experience') == True:
            experienced += 1 
        else:
            not_experienced += 1 
    print('There are {} experienced players and  {} players with no experience at all.'.format(experienced, not_experienced))

def average_height(team):
    total_height = 0
    for player in balanced_teams.get(team):
        total_height += player.get('height')
    average_height = total_height / PLAYERS_PER_TEAM
    print('The average height of this team is {} inches.'.format(round(float(average_height))))

def show_guardians(team):
    guardians = []
    for player in balanced_teams.get(team):
        guardians += player.get('guardians')
    team_guardians = ', '.join(guardians)
    print('The guardians for this team are: {}'.format(team_guardians))

if __name__ == '__main__':
    clean_data()
    balance_experience()
    balance_teams()
    menu()