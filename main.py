import random
import time
import os
debug = True
def srt_game():
    answer = random.randint(1, 20)
    if debug:
        print(f"Answer is {answer}")
        print()
    print(f"I am thinking of a number between 1 and 20. Can you guess it?")
    prediction = input("Your guess: ")
    # noinspection PyBroadException
    try:
        # noinspection PyUnresolvedReferences
        numpred = int(prediction)
    except:
        print(":o a wild error has occurred, please insure that your guess is a number.")
        time.sleep(2)
        os.system('cls')
        srt_game()
    close = answer-numpred
    print(close)
    if close == 0:
        os.system('cls')
        print(f"Congratulations you guessed the correct number: {answer}")
    elif 1 <= close <= 5:
        os.system('cls')
        print(f"So close! You were {close} away! ")
    elif 6 <= close <= 10:
        os.system('cls')
        print(f"Getting there... You were {close} away.")
    elif 11 <= close <= 20:
        os.system('cls')
        print(f"You were far off at {close} away.")

srt_game()