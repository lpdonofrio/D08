#!/usr/bin/env python3
# Imports
import random


# Body
def print_roster(roster):
    """ prints entire roster """
    for x in roster:
        print(x)


def get_random_participant_index(roster):
    """ Returns random index of person in roster """
    return random.randint(0, len(roster) - 1)


def get_person(index, roster):
    """ Returns person (string) from roster """
    # rewrite getPerson() to take a index and roster; return name at index
    
    # number, person
    for x,y in enumerate(roster):
        # print("number: {}, name: {}".format(x,y))
        if x == index:
            return y
    

def add_person(roster, add_name):
    """ Adds person (string) to roster """
    # rewrite addPersion() to take a name and roster; add name to roster
    roster.append(add_name)
    print("You added {} to {}.".format(add_name, roster))

def get_excuse():
    excuses = ["My dog ate my homework",
               "I drank too much beer last night.",
               "\"Bored to Death\" marathon",
               "Laptop went up in flames",
               "Ain't nobody got time for that!",
               "My plane got stuck in Vegas",
               "I was watching \"The Big Lebowski\"",
               "Wait, I was supposed to do something?"]

    return excuses[random.randint(0, len(excuses) - 1)]


###############################################################################
def main():
    """ Main -- prints the bootcamp roster, adds Daniel, and then prints
    excuses """
    bootcamp_participants = ["Malavika", "Edward", "Nancy", "Ankeet", "Anna",
                            "Arnav", "Sandeep", "Shannon", "Natalia", "Nia",
                            "Nicolas", "Nihar", "Suchismita", "Vikram", "Yifei",
                            "Avi", "Nisha", "Peter", "Priyanka", "Rohit",
                            "Sophie", "Selenne", "Carina", "Lucia", "Meghana",
                            "Harman", "Robin", "Karan", "Liz", "Shazeda",
                            "Jolly", "Michelle", "Morgan", "Mudit"]

    # your one line of code goes here to print roster #
    print_roster(bootcamp_participants)
    
    # add 'Daniel' to bootcampParticipants
    add_person(bootcamp_participants, "Daniel")
    
    # Your Code Here ###
    # get random participant
    index = get_random_participant_index(bootcamp_participants)
    print(get_person(index, bootcamp_participants))
    # print person's name who has excuse today.
    name = get_person(index, bootcamp_participants)
    #excuse = get_excuse()
    #
    # print person's name who has excuse today.
    # Fix code below to print name and excuse of person:
    print("{} said: {}".format(name, get_excuse()))


if __name__ == "__main__":
    print("Excuse Generator: ") 
    main()
