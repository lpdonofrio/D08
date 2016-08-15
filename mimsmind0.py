#Sample place-in exam, part 1

#imports
import random
import sys

#body
def generate_random():
    try:
        x = sys.argv[1]
    except:
        x = 1
    random_concat = ""
    for n in range(0, int(x)):
        random_number = str(random.randint(0, 9))
        random_concat = random_concat + random_number
    return random_concat, x

def guess_number():
    random_concat, x = generate_random()
    print("Let's play the mimsmind0 game.")
    user_input = input("Guess a {}-digit number: ".format(x))
    counter = 1
    while True:
        if user_input < random_concat:
            user_input = input("Try again. Guess a higher number: ")
            counter += 1
        elif user_input > random_concat:
            user_input = input("Try again. Guess a lower number: ")
            counter += 1
        else:
            print("Congratulations. You guessed the correct number "
                  "in {} tries.".format(counter))
            return

#########################################################################
def main():

    guess_number()

if __name__ == '__main__':
    main()