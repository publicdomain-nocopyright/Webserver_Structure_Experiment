with open('0_Documentation.md', 'r') as file:
    print(file.read())
    
import os
for filename in os.listdir('.'):
    print(filename)