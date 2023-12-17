import random
import time

SEASON_ONE = [5,6,7]
SEASON_TWO = [1,2,3,4,"Midseason Final",5,6,8, "Final"]
SEASON_THREE = [1,2,3,4,"Midseason Final",5,6,7,8,"Final"]
SEASON_FOUR = [1,2,3,4,"Midseason Final",6,7,8,9,10,"WBCH NNN Final"]
ALL_SEASONS = {"1": SEASON_ONE, "2": SEASON_TWO, "3": SEASON_THREE, "4": SEASON_FOUR}

def get_random_num():
    if random.randrange(0, 2):
        return 1
    else:
        return 0

def loading():
    print("/", end='\r')
    time.sleep(round(random.uniform(0, 1), 2))
    print("-", end='\r')
    time.sleep(round(random.uniform(0, 1), 2))
    print("\\", end='\r')
    time.sleep(round(random.uniform(0, 1), 2))
    print("-", end='\r')
    time.sleep(round(random.uniform(0, 1), 2))

def Coinflip():
    to_decide = input("Event on HEAD: ")
    loading()
        
    if get_random_num():
        print("Head")
    else:
        print("Tail")


def get_episode():
    print("The episode will be in season: ")
    loading()
    seasons = {}
    if get_random_num():
        seasons["1"] = SEASON_ONE
    if get_random_num():
        seasons["2"] = SEASON_TWO
    if get_random_num():
        seasons["3"] = SEASON_THREE
    if get_random_num():
        seasons["4"] = SEASON_FOUR
    if len(seasons.keys()) == 0:
        seasons = ALL_SEASONS
    
    for i,season in enumerate(list(seasons.keys())):
        print(str(season), end="")
        if i < len(list(seasons.keys()))-1:
            print(" or ", end="")

    time.sleep(1)

    print("\nYou will do: ")
    loading()
    all_episodes = 0
    for season in list(seasons.values()):
        all_episodes += len(season)

    conc_episode_of_all = random.randrange(1,all_episodes+2)

    conc_seas = 0
    conc_ep = 0
    for key,season in seasons.items():
        for ep in season:
            all_episodes -= 1
            if all_episodes == conc_episode_of_all:
                conc_seas = key
                conc_ep = ep
                print("Season: " + str(conc_seas) + ", Episode: " + str(conc_ep))


def main():
    print(time.strftime("%H:%M:%S", time.localtime()))
    print("I knew you would come back. Don't waste time, choose!\n")
    
    while True:
        decider_ans = input("Do you wan't to start the full decider program?(y/n): ")
        if decider_ans in ["y", "Y", "j", "J"]:
            break
        else:
            Coinflip()
            return
    
    print("Bust your Balls if Head")
    loading()
    if get_random_num():
        print("Head")
    elif random.randrange(0,11) > 7:
        print("Head")
    elif random.randrange(0,101) > 80:
        print("Head")
    elif random.randrange(0,1001) > 900:
        print("Head")
    else:
        print("Tail")
        if get_random_num():
            wording = "must"
        else:
            wording = "can"
        if get_random_num():
            print("(un)lucky, you " + wording + " retry in " + str(random.randrange(0,10)) + " minutes")
        elif get_random_num():
            print("(un)lucky, you " + wording + " retry in " + str(random.randrange(0,21)) + " minutes")
        else:
            print("(un)lucky, you " + wording + " retry in " + str(random.randrange(1,31)) + " minutes")
        return

    print("Make it searious if Head")
    loading()
    if random.randrange(0,11) <= 7:
        print("Head")
    else:
        print("Tail")
        if get_random_num():
            print("You ran in a second round.")
            loading()
            if get_random_num():
                print("Head")
            else:
                print("Tail")
                print("strength = " + str(random.randrange(7,10)) + " /10(serious)")
        else:
            print("strength = " + str(random.randrange(4,7)) + " /10(serious)")
    
    get_episode()

    print("Warmup if Head")
    loading()
    if get_random_num():
        print("Head")
        print("Warmup by busting if Head")
        loading()
        if get_random_num():
            print("Head")
            print("Warmup with a WBCH special if Head")
            loading()
            if get_random_num():
                print("Head")
            else:
                print("Tail")
                print("Warmup by looking at " + str(random.randrange(10,1001)) + " QOS pictures.")
                print("When ever you see a 'qos, blacked, Vixen' sign or text, bust your balls\n as many times as you see it")
        else:
            print("Tail")
            print("Warmup by stroking and squeezing your balls for 2min")
    else:
        print("Tail")
        print("Do not warmup")

    
    print("\nNow it's decision time if you cum by busting or not!")
    time.sleep(2)
    print("The decider will start it's calculations and tell you the result. Wait a few seconds")
    border = 0
    cum_from_busting = False
    for i in range(0,10):
        loading()
        if get_random_num():
            border += 1
        if border == 5:
            cum_from_busting = True
    
    if not cum_from_busting:
        print("It looks like you don't need to cum from busting.")
        print("But a final test will decide about it and test your white luck another time!")
        while True:
            dig = int(input("How often did you already busted yourself to an orgasm?(0-50)"))
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
        print("Result: Bust your balls until you cum!")
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
