new_file = open('New_File.txt', 'x')
new_file.close()

import os
print("Checking if My file exists or not....")
if os.path.exists("My_file.txt"):
    os.remove("My_file.txt")
else:
    print("The file does not exist")

My_file = open("My_file.txt", "w")
My_file.write("Hi! I am penguin of 1 yr")
My_file.close()

os.remove('Codingal.txt')