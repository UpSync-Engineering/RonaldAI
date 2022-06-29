import pyfiglet as pyfiglet
from termcolor import colored
from src.engine.openai_engine import get_openai_response
from src.engine.crypto import get_cryptocurrency_price
from src.engine.system import *
from src.engine.information import get_weather_info
from src.engine.commands import *
from src.engine.constants import *


def welcome():
    title = pyfiglet.figlet_format('Welcome to RonaldAI', font='slant')
    print(colored(title, 'green'))
    print(colored('RonaldAI is the ultimate CLI tool.', 'green'))


def determine_action(user_input):
    # Parce the first word of the user input
    action = user_input.split()[0]

    # Check if action in the list of COMMANDS
    if action not in COMMAND_LIST:
        print(colored('Sorry, I don\'t understand.\nType \'all_commands\' for a list of available commands.', 'red'))
        return

    if action == "all_commands":
        # Print all commands from COMMAND_HELP dictionary
        print(colored('Here is a list of available commands:', 'green'))
        for command in COMMAND_HELP:
            print(colored(command + ' ' + COMMAND_HELP[command], 'green'))
        return

    elif action == 'exit':
        print('Bye!')
        exit()

    elif action == "time":
        # Get current time
        current_time = get_current_time()
        print(colored(current_time, 'green'))
        return

    payload = user_input.split(' ', 1)[1]
    if action == "help":
        if payload in COMMAND_HELP:
            print(colored(payload + ": " + COMMAND_HELP[payload], 'green'))
        else:
            print(colored('Sorry, I don\'t understand.\nType \'command_list\' for a list of available commands.', 'red'))
        return

    elif action == "openai":
        print(colored('You asked for a response from OpenAI.', 'green'))
        print(get_openai_response(payload))
        return

    elif action == "crypto":
        print(colored('{} price:'.format(payload), 'green'))
        print(get_cryptocurrency_price(payload))
        return

    elif action == "math":
        print(colored('You asked for a math calculation: ' + str(payload), 'green'))
        print(execute_math_calculation_from_string(payload))
        return

    elif action == "weather":
        print(colored('You asked for the weather in {}'.format(payload), 'green'))
        print(get_weather_info(payload))
        return

    elif action == "go":
        print(colored('Now opening {}'.format(payload), 'green'))
        website_params = payload.split(' ', 1)
        site_url = WEBSITES[website_params[0]]

        if website_params[0] == 'github':
            if website_params[1].split(' ', 1)[0] is not None and 'repo' == website_params[1].split(' ', 1)[0]:
                site_url = site_url + 'PopBot/' + website_params[1].split(' ', 1)[1]
        elif website_params[0] == 'google':
            site_url = site_url + website_params[1]
        elif website_params[0] == 'youtube':
            if website_params[1].split(' ', 1)[0] is not None and 'search' == website_params[1].split(' ', 1)[0]:
                site_url = site_url + 'results?search_query=' + website_params[1].split(' ', 1)[1].replace(' ', '+')
        elif website_params[0] == 'amazon':
            if website_params[1].split(' ', 1)[0] is not None and 'search' == website_params[1].split(' ', 1)[0]:
                site_url = site_url + 's?k=' + website_params[1].split(' ', 1)[1].replace(' ', '+')

        open_website(site_url)
        return

    else:
        print("Sorry, I don't understand.\nType 'all_commands' for a list of available commands.")
        return


if __name__ == '__main__':
    welcome()
    print("Enter command. Type 'all_commands' for a list of all commands. Type 'exit' to exit.")
    while True:
        user_input = input('> ')
        determine_action(user_input)
        print()
        print()

