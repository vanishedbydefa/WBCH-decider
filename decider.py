import argparse
import random
import time
import json

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'  # Reset to default color

f = open('epdb.json')
data = json.load(f)
f.close()

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

def get_season():
    seasons = {} #dict, containing the amount of episodes of each season
    for key in data:
        key = data[key]
        if key["season"] != 0 and type(key["season"]) == int:
            seasons[key["season"]] = len(key["episodes"])
    
    #randomly choose a season, based on the amount of episodes in it
    entries, weights = zip(*seasons.items())
    return random.choices(entries, weights=weights, k=1)[0]

def get_episode(premium=False, season=None):   
    if season == None:
        season = get_season()
    for key in data:
        key = data[key]
        if key["season"] == season:
            while True:
                if premium:
                    episodes = itertools.chain(key["episodes"], key["premium_episodes"])
                    episode = random.choice(list(epsidoes))
                else:
                    episode = random.choices(key["episodes"], k=1)[0]
                if episode[next(iter(episode))] != "NOWARMUP":
                    break
            loading("Episode:", overwrite=True)
            print(f'Episode: "{next(iter(episode))}"')
    

def main():
    parser = argparse.ArgumentParser(prog='WBCH Decider', description='Automatic decisions for doing WBCH episodes', epilog='https://github.com/vanishedbydefa')
    parser.add_argument('-p', '--premium', action='store_true', help='Include premium episodes')

    args = parser.parse_args()
    premium = args.premium
    
    print(f'Start: {time.strftime("%H:%M:%S", time.localtime())}')   
    while True:
        decider_ans = input("Do you wan't to start the full decider program?(y/n): ")
        if decider_ans in ["y", "Y", "j", "J"]:
            break
        else:
            Coinflip()
            return
    
    loading("Bust your Balls:", overwrite=False)
    if get_random_num():
        print(GREEN + "True" + RESET)
    elif random.randrange(0,11) > 6:
        print(GREEN + "True" + RESET)
    elif random.randrange(0,101) > 70:
        print(GREEN + "True" + RESET)
    elif random.randrange(0,1001) > 800:
        print(GREEN + "True" + RESET)
    else:
        print(RED + "False" + RESET)
        if get_random_num():
            wording = "must"
        else:
            wording = "can"
        if get_random_num():
            print("(un)lucky, you " + wording + " retry in " + str(random.randrange(1,6)) + " minutes")
        elif get_random_num():
            print("(un)lucky, you " + wording + " retry in " + str(random.randrange(5,11)) + " minutes")
        else:
            print("(un)lucky, you " + wording + " retry in " + str(random.randrange(10,21)) + " minutes")
        return
    
    get_episode(premium=premium)

    loading("Warmup:", overwrite=False)
    if get_random_num():
        print(GREEN + "True" + RESET)
        loading("  Warmup with busting:", overwrite=False)
        if get_random_num():
            print(GREEN + "True" + RESET)
            loading("    Warmup with a WBCH special:", overwrite=False)
            if get_random_num():
                print(GREEN + "True" + RESET)
                get_episode("WBCHSPECIAL")
            else:
                print(RED + "False" + RESET)
                print("    -> Warmup by looking at " + str(random.randrange(10,501)) + " QOS pictures.")
                print("       When ever you see a 'qos, blacked, Vixen' sign or text, bust your balls\n as many times as you see it")
        else:
            print(RED + "False" + RESET)
            print("  -> Warmup by stroking and squeezing your balls for 2min")
    else:
        print(RED + "False" + RESET)    
    print("\nNow it's decision time if you cum by busting or not!")
    time.sleep(2)
    print("The decider will start it's calculations and tell you the result. Wait a few seconds")
    border = 0
    cum_from_busting = False
    for i in range(0,10):
        loading("Cum from busting:", overwrite=True)
        if get_random_num():
            border += 1
        if border == 5:
            cum_from_busting = True
            loading("Cum from busting:", overwrite=False)
            print(GREEN + "True" + RESET)
            break
    
    if not cum_from_busting:
        print("Wait")
        print("It looks like you don't need to cum from busting.")
        print("But a final test will decide about it and test your white luck another time!")
        while True:
            dig = input("How often did you already busted yourself to an orgasm?(0-50)")
            try:
                dig = int(dig)
            except ValueError:
                print("Insert a number between 0 and 50")
                continue
            
            if int(dig) < 0 or int(dig) > 50:
                print("Insert a number between 0 and 50")
                continue
            else:
                rand_val = random.randrange(0,int(dig)+1)
                border = 0
                cum_from_busting = False
                for i in range(0, rand_val):
                    if get_random_num():
                        border +=1
                    if border == (rand_val//2)+1:
                        cum_from_busting == True
                        break
                break

    if cum_from_busting:
        print("\nResult: Bust your balls until you cum!")
        print("If you do not cum within the given episode, press 'y' for another episode. Otherwise press 'n'")
        print("Do not terminate this program until you came!\n")

        while True:
            another = input("Press 'y' for another episode or 'n' if you cam from busting: ")
            if another in ["n", "N"]:
                return
            elif another in ["y", "Y", "j", "J"]:
                get_episode()
                print("")

    else:
        print("Result: You don't need to cum from busting. But you are suposed to do the")
        print("given episode. After that you can decide on your own what to do next!")
        print("Now, BUST!")
        
main()
