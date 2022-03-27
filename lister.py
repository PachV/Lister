### This is a lister for anything, movies you have watched and their rating (IMDb, MyAnimeList, VNDb, etc). WIP
# To do list:
# Change the value of the value that is already added in .json
# Add QT GUI and a image saving function(probably need to learn C++) 
# Add plan-to watch list-
#  plan-to watch list will be in another file (json) as a list[] datatype, if the user writes the key to the list.json that is
#  already in the to plan-to watch list file, the list file's index (name) will be deleted  
 
import json
import read_algo as readalgo
import write_algo as writealgo
file = 'list.json'

def read():
    with open(file, "r") as f:
        data = json.load(f)
    tasks = int(input("--------------------------\\n1=Print all\n2=Sort value from highest to lowest\n\
3=Sort value from lowerst to highest\n4=Sort key from highest to lowest\n5=Sort key from lowest to highest: "))

    match tasks:
        case 1:
            readalgo.read(data)
        case 2: 
            readalgo.sort_value_high_to_low(data)
        case 3:
            readalgo.sort_value_low_to_high(data)
        case 4:
            readalgo.sort_key(data)       
        case 5:
            readalgo.sort_key_reverse(data)

def write():
    tasks = int(input("--------------------------\n1=Write\n2=To plan-to watch list: "))

    match tasks:
        case 1:
            ToBeAdded = {}
            key = input("Enter the Name: ")
            value = float(input("Enter the Rating: "))
            if value >=10:
                print("below 10 please  🔧🎱")
                write()
            ToBeAdded[key] = [value]
            with open(file, "r+") as f:
                data = json.load(f)
                data.update(ToBeAdded)
                f.seek(0)
                json.dump(data, f)
        case 2:
            what_to_watch = input("What do you want plan to watch?: ")
            a_list = []
            with open('plan-to-watch-list.json', "a+") as f:
                data = json.load(f)
                data.a_list.append(what_to_watch)
                json.dump(a_list, f)


try:
    while True:
        print("1 = Write\n2 = Read (q to quit): ", end="")
        what = input('')
        if what == 'q':
            break
        match int(what):
            case 1:
                write()
            case 2:
                read()
except KeyboardInterrupt:
    print("🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥")