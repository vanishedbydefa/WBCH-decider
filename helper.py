import os
import time
import random
from colorama import init, Fore

init()
RED = Fore.RED
GREEN = Fore.GREEN
RESET = Fore.RESET

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
