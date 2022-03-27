# writing algorithm 
import json

def write_file(file):
    ToBeAdded = {}
    key = input("Enter the Name: ")
    value = float(input("Enter the Rating: "))
    if value >=10:
        print("Below 10 please  🔧🎱")
        write_file(file)
    ToBeAdded[key] = [value]
    with open(file, "r+") as f:
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
