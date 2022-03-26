### This is a lister for anything, movies you have watched and their rating (IMDb, MyAnimeList, VNDb, etc). WIP

# To do list:
# Change the value of the value that is already added in .json

# Add QT GUI and a image saving function(probably need to learn C++) 
import json
import read_algo as algo 

file = 'list.json'

with open(file, "r") as f:
    data = json.load(f)

def read():
    tasks = int(input("-----------------\n1=Print all\n2=Sort value from highest to lowest\n\
3=Sort value from lowerst to highest\n4=Sort key from highest to lowest\n: "))

    match tasks:
        case 1:
            algo.read(data)
        case 2: 
            algo.sort_value_high_to_low(data)
        case 3:
            algo.sort_value_low_to_high(data)
        case 4:
            algo.sort_key(data)       

def write():
    ToBeAdded = {}
    key = input("Enter the Name: ")
    value = float(input("Enter the Rating: "))
    if value >=10:
        print("below 10 please 🔧🎱")
        write()
    ToBeAdded[key] = [value]
    with open(file, "r+") as f:
        data = json.load(f)
        data.update(ToBeAdded)
        f.seek(0)
        json.dump(data, f)

def task(choice):
    match choice:
      case 1:
          write()
      case 2:
          read()

try:
    while True:
        print("1 = Write\n2 = Read (q to quit): ", end="")
        what = input('')
        if what == 'q':
            break
        task(int(what))
except KeyboardInterrupt:
    print("🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥")