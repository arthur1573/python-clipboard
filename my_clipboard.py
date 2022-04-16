import sys
import clipboard
import json
#import data


# print("")
# print("--------------------------- 1 ------------------------")
# print(sys)
# print("")
# print(sys.argv)
# print("")
# print(clipboard)
# print("")
# print(json)
# print("") 
# print("") 
# print("") 
#print("--------------------------- 2 ------------------------")

# print("") 
# print(sys.argv[1:])

# print("") 
# print(len(sys.argv))

# print("") 
# print("") 
# print("") 
#print("--------------------------- 3 ------------------------")




# SAVE_DATA = "data.json"
# print(SAVE_DATA)


def save_json(filepath, data):
    with open(filepath, "w"):
        # as f
        #f = open(filepath, "w")
        
        #print("* f:", end=" ")
        #print(f)
        #print("")
        
        #print("""* open(filepath, "w"):""", end=" ")
        #print(open(filepath, "w"))
        #print("")
                
        json.dump(data, open(filepath, "w"), sort_keys=True, indent=4)
        # json.dump(data, f)
        #print("* json.dump:", end=" ")
        #print(json.dump)
        
        #print("* json.dump(data, f):", end=" ")
        #print("")


# save_json("data.json", {'key2':'hhh'})


def load_json(filepath):
    try:
        with open(filepath, "r"):
            f2 = open(filepath, "r")
            #print("* f2:", end=" ")
            #print(f2)

            #print("""* open(filepath, "r"):""", end=" ")
            #print(open(filepath, "r"))
            #print("")                             
            data = json.load(f2)
            #print("""* json.load(open(filepath, "r")):""" , end = " ")
            #print(json.load(open(filepath, "r")))
            
            #print("* data:", end = "")
            #print(data)
            return data
    except:    
        print("There is not a data.json file. You need to save something at first\n")
        return {}
        


#print("------------------ 4 ----------------")

# load_json(SAVE_DATA)
#load_json("data.json")



"""


print("") 
print("") 


#data.dictions['eggs'] = 3
print(type(data.dictions))
print(data.dictions)
data.dictions["color"] = "red"
data.dictions.update({'color2' : 'green'})


# value = {'the answer' : 43}
# print(value)
# print(str(value))


print(data.dictions)



# with open('data.py') as f:
    # f.write()


"""



# print("") 
# print("------------------------------------ 5 -----------------") 

if len(sys.argv) > 1:    
    command = sys.argv[1]
    print("---------------------------------------------------")
    print("The command has got： " + command +"\n")
    data = load_json("data.json")
    if command == "-save":
        # key = input("Enter a key: ")
        key2 = command = sys.argv[2]
        #command2 = sys.argv[2]
        #print(command2)
        data[key2] = sys.argv[3]
        #command3 = sys.argv[3]
        #print(command3)
        save_json("data.json", data)
        
        print("I have already saved your text.")
        
    elif command == "-load":
        #key = input("Enter a key: ")
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
