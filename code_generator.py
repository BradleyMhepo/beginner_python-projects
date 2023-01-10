import string 
import random
alphabet = list(string.ascii_lowercase) 
code =""
values = input("Please enter the text that you want to encode: ")
for i in values:
    code += (random.choice(alphabet))
print(f"Your generated code is {code}")