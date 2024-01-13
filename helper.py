import itertools
import random
import json
import time
import sys
import os

from colorama import init, Fore

init()
RED = Fore.RED
GREEN = Fore.GREEN
RESET = Fore.RESET

def get_data_file_path(filename):
    if getattr(sys, 'frozen', False):  # Check if the application is run as a bundle
        # If run as a bundle (e.g., PyInstaller executable), use sys._MEIPASS
        return os.path.join(sys._MEIPASS, filename)
    else:
        # If run as a script, file is in cwd
        return filename

def load_json_file(filename:str):
    file_path = get_data_file_path(filename)
    with open(file_path, 'r') as f:
        return json.load(f)

def get_random_num():
    if random.randrange(0, 2):
        return 1
    else:
        return 0

def loading(loading_str:str, overwrite:bool):
    print(f"{loading_str} |", end='\r')
    time.sleep(round(random.uniform(0, 1), 2))
    print(f"{loading_str} /", end='\r')
    time.sleep(round(random.uniform(0, 1), 2))
    print(f"{loading_str} -", end='\r')
    time.sleep(round(random.uniform(0, 1), 2))
    print(f"{loading_str} \\", end='\r')
    time.sleep(round(random.uniform(0, 1), 2))
    print(f"{loading_str} |", end='\r')
    time.sleep(round(random.uniform(0, 1), 2))
    if overwrite:
        print(f"{loading_str} ", end='\r')
    else:
        print(f"{loading_str} ", end='')


def Coinflip():
    to_decide = input("Event on HEAD: ")
    loading(to_decide + ":", overwrite=False)
        
    if get_random_num():
        print(GREEN + "Head" + RESET)
    else:
        print(RED + "Tail" + RESET)


def check_path_exists(path:str, create=False):
    '''
    Check wether path exists or not.
    If path do not exist but create=True,
    create a directory.
    '''
    path_exist = os.path.exists(path)
    if path_exist:
        return True

    #path do not exist, try to create it
    if create:
        try:
            os.makedirs(path)
            return True
        except OSError as e:
            print(f"Failed to create directory: {path}")
            print(f"Error: {e}")
            return False
    return False

def exe_helper():
    while True:
        premium = input("Do you want to include premium episodes? [y/n]: ")
        if premium not in ["y", "Y", "j", "J", "yes", "Yes", "n", "N", "no", "No"]:
            print("Type 'y' to include premium episodes in the decisions, otherwise enter 'n': ")
            continue
        elif premium in ["y", "Y", "j", "J", "yes", "Yes"]:
            premium = True
            break
        elif premium in ["n", "N", "no", "No"]:
            premium = False
            break

def get_season():
    data = load_json_file('epdb.json')
    seasons = {} #dict, containing the amount of episodes of each season
    for key in data:
        key = data[key]
        if key["season"] != 0 and type(key["season"]) == int:
            seasons[key["season"]] = len(key["episodes"])
    
    #randomly choose a season, based on the amount of episodes in it
    entries, weights = zip(*seasons.items())
    return random.choices(entries, weights=weights, k=1)[0]

def get_episode(premium=False, season=None):
    data = load_json_file('epdb.json')   
    if season == None:
        season = get_season()
    for key in data:
        key = data[key]
        if key["season"] == season:
            while True:
                if premium:
                    episodes = itertools.chain(key["episodes"], key["premium_episodes"])
                    episode = random.choice(list(episodes))
                else:
                    episode = random.choices(key["episodes"], k=1)[0]
                if episode[next(iter(episode))] != "NOWARMUP":
                    break
            loading("Episode:", overwrite=True)
            print(f'Episode: "{next(iter(episode))}"')
