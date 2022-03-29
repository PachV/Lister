### This is a lister for movies(or databses like IMDb, MyAnimeList, VNDB, etc) you have watched and their rating. WIP
# To do list:
    # Add QT GUI and a image saving/scraping function(probably need to learn C++) 
    # Add plan-to watch list-
    #  plan-to watch list will be in another file (json) as a list datatype, if the user writes the key to the list.json that is
    #  already in the to plan-to watch list file, the list file's index (name) will be deleted  
 
import json
import read_algo as readalgo
import write_algo as writealgo

# test
def read():
    with open("watched_list.json", "r") as f:
        data = json.load(f)
    tasks = int(input("--------------------------\n1 = Print all\n2 = Sort value from highest to lowest\n\
3 = Sort value from lowerst to highest\n4 = Sort key from highest to lowest\n5 = Sort key from lowest to highest\n6 = Print to watch list: "))
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
        case 6:
            readalgo.read_plan() 

def write():
    tasks = int(input("--------------------------\n1 = Write to watched\n2 = To plan-to watch list: "))
    match tasks:
        case 1:
            writealgo.write_file()
        case 2:
            writealgo.plan_watch()

try:
    while True:
        what = input("1 = Write\n2 = Read (q to quit): ")
        if what == 'q':
            break
        match int(what):
            case 1:
                write()
            case 2:
                read()
except KeyboardInterrupt:
    print("🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥")

