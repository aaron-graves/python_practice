#Aaron Graves 100116
#Python practice

import string, random, sys

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
all_letters = vowels + consonants
names = ['']*10

print("\nThis file takes three inputs and returns 10 random strings: ")

#get a single user input
def get_input():
    l = input("-V for vowel, C for consonant, and L for all letters. \n")
    if l == "v" or l == "V" or l == "c" or l == "C" or l == "l" or l == "L":
        if l == "v" or l == "V":
            l = "v"
        elif l == "c" or l == "C":
            l = "c"
        elif l == "l" or l == "L":
            l = "l"
        return l
    else:
        sys.exit("Not V, C, or L.  Restart program")
    
#store 3 inputs in list
def store_input():
    name = []
    for i in range(3):
        name.insert(i,get_input())
    return name

#determine letter based on stored list
def run_generator(l):
        if l == "v" or l == "V":
            l = random.choice(vowels)
        elif l == "c" or l == "C":
            l = random.choice(consonants)
        elif l == "l" or l == "L":
            l = random.choice(all_letters)
        return l

#store each "name" created by run_generator()    
def store_name(letters):
    name = ""
    for l in letters:
        name += run_generator(l)
    return name

#get ten names and store in names list
def ten_times(names):
    letters = store_input()
    for i in range(10):
        names[i] += str(store_name(letters)) 
    return 

#program start 
ten_times(names)
print("Output:")
for name in names:
    print(name)
