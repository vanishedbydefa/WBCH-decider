import argparse
import random
import time
import sys
import os

from colorama import init, Fore

from helper import exe_helper, loading, get_random_num, Coinflip, check_path_exists, get_season, get_episode

init()
RED = Fore.RED
GREEN = Fore.GREEN
RESET = Fore.RESET
    
def main():
    print(f'Start: {time.strftime("%H:%M:%S", time.localtime())}')
    parser = argparse.ArgumentParser(prog='WBCH Decider', description='Automatic decisions for doing WBCH episodes', epilog='https://github.com/vanishedbydefa')
    parser.add_argument('-p', '--premium', action='store_true', help='Include premium episodes')

    args = parser.parse_args()
    premium = args.premium  

    exe = False
    if sys.argv[0][-4:] == ".exe":
        exe = True

    while True:
        decider_ans = input("Do you wan't to start the full decider program?(y/n): ")
        if decider_ans in ["y", "Y", "j", "J"]:
            break
        else:
            Coinflip()
            if exe:
                os.system("pause")
            return

    if exe:
        premium = exe_helper()

    # Check if epdb is present and not running as exe. (exe already included the data)
    if not check_path_exists(os.getcwd()+"\\decider.exe", create=False) and not exe:
        print("Please start program in the folder where epdb.json is stored")
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
    for i in range(0,5):
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
            dig = input("How often did you already busted yourself to an orgasm?(0-50): ")
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
        print("\n\nResult: Bust your balls until you cum!")
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
        print("\nResult: You don't need to cum from busting. But you are suposed to do the")
        print("given episode. After that you can decide on your own what to do next!")
        print("Now, BUST!\n")

    if exe:
        os.system("pause")
main()
