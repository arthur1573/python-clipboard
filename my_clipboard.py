import sys
import clipboard
import json





def save_json(filepath, data):
    with open(filepath, "w"):
        json.dump(data, open(filepath, "w"), sort_keys=True, indent=4)


def load_json(filepath):
    try:
        with open(filepath, "r"):
            f2 = open(filepath, "r")                           
            data = json.load(f2)
            return data
    except:    
        print("There is not a data.json file. You need to save something at first\n")
        return {}
        



if len(sys.argv) > 1:    
    command = sys.argv[1]
    print("---------------------------------------------------")
    print("The command has got： " + command +"\n")
    data = load_json("data.json")
    if command == "-save":
        key2 = command = sys.argv[2]
        data[key2] = sys.argv[3]
        save_json("data.json", data)
        print("I have already saved your text.")    
    elif command == "-load":
        key = sys.argv[2]
        if key in data:
            clipboard.copy(data[key])
            print("I have already copied text. \nKey: " + key + "\nValue: " + data[key])
        else:
            print("Key does not exist.")     
        
    elif command == '-list':
        print("I have already listed your text:\n")
        print(data)
        
    elif command == "-help":
        print("")
        print("my_clipboard.py -save 12345 54321")
        print("I will save your text: 54321 in the key: 12345")
        print("") 
        print("my_clipboard.py -load 12345")
        print("I will load&copied your text: 54321")
        print("---------------------------------------------------")
    else:
        print('Aw, It looks like a unkown command.')
else:
    print("---------------------------------------------------")
    print("Tring to use this command: -help, -save, -load, -list")
    print("For instance: \nmy_clipboard.py -hlep")
    print("---------------------------------------------------")



