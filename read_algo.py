
def read(data):
    print(f"{data}\n----------------------")

def sort_value_high_to_low(data):
    print('---------------\nName Score')
    for key, value in sorted(data.items(), key=lambda kv: kv[1], reverse=True):
        print("%s %s" % (key, value))

def sort_value_low_to_high(data):
    print('---------------\nName Score')
    for key, value in sorted(data.items(), key=lambda kv: kv[1]):
        print("%s %s" % (key, value))

def sort_key(data):
    print('---------------\nName Score')
    for key in sorted(data.keys()):
        print("%s %s" % (key, data[key]))
