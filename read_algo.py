# reading algorithm
import json

def read(data):
    print('--------------------------\nName Score')
    for key, value in data.items():
        print("%s %s" % (key, value))

def sort_value_high_to_low(data):
    print('--------------------------\nName Score')
    for key, value in sorted(data.items(), key=lambda kv: kv[1], reverse=True):
        print("%s %s" % (key, value))

def sort_value_low_to_high(data):
    print('--------------------------\nName Score')
    for key, value in sorted(data.items(), key=lambda kv: kv[1]):
        print("%s %s" % (key, value))

def sort_key(data):
    print('--------------------------\nName Score')
    for key in sorted(data.keys()):
        print("%s %s" % (key, data[key]))

def sort_key_reverse(data):
    print('--------------------------\nName Score')
    for key in sorted(data.keys(), reverse=True):
        print("%s %s" % (key, data[key]))

def read_plan():
    with open("plan-to-watch-list.json", "r") as file:
        data = json.load(file)
    print('--------------------------\nTo-watch list')
    for i in data:
        print(i)


        