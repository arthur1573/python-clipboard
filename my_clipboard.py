import sys
import clipboard
import json

print("")
print("----------------------------------------------------")
print(sys)
print("")
print(sys.argv)
print("")
print(clipboard)
print("")
print(json)
print("") 
print("----------------------------------------------------")

print("") 
print(sys.argv[1:])

print("") 
print(len(sys.argv))

print("") 
if len(sys.argv) > 1:
    
    command = sys.argv[1]
    print("The command has got..." + command +"\n")
    if command == "-save":
        print("I have already saved your text.")
    elif command == "-load":
        print("I have already loaded your text.")
    elif command == '-list':
        print("I have already listed your text.")
    else:
        print('Unkown command')
else:
    print("Use this command: -save, -load, -list...")





