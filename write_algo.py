# writing algorithm 
import json

def write_file():
    ToBeAdded = {}
    key = input("Enter the Name: ")
    value = float(input("Enter the Rating: "))
    if value >=10:
        print("Under 10 please 🔧")
        write_file()
    ToBeAdded[key] = [value]

    # #If ToBeAdded key matches with the string in plan-to-watch-list.json, it will be deleted
    # with open("plan-to-watch-list.json", "r") as file:
    #     data = json.load(file)
    # with open("plan-to-watch-list.json", "r+") as fi:
    #     for i in data:
    #         if i in ToBeAdded.keys():
    #             data = data.remove(i)
    #             json.dump(data, fi)


    with open("watched_list.json", "r+") as f:
        data = json.load(f)
        data.update(ToBeAdded)
        f.seek(0)
        json.dump(data, f, indent=2)

def plan_watch():
    what_to_watch = input("What do you want plan to watch?: ")
    with open("plan-to-watch-list.json", "r") as file:
        data = json.load(file)
    with open("plan-to-watch-list.json", "w+") as f:
        data.append(what_to_watch)
        json.dump(data, f, indent=2)


